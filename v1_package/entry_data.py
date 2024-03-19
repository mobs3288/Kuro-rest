import re
from bs4 import BeautifulSoup
import requests

def get_entry_data(entry_id, page_number):
    url = f"https://myfigurecollection.net/entry/{entry_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract item name and sub-item name
        h1_element = soup.find("h1", itemprop="headline")
        sub_h1_element = soup.find("div", class_="subtitle")
        item_name = h1_element.get_text(strip=True) if h1_element else None
        sub_item_name = sub_h1_element.get_text(strip=True) if sub_h1_element else None

        # Extract company logo URLs
        thumb_main_images = soup.find_all('div', class_='object-picture entry-picture')
        company_logo = [img.img['src'] for img in thumb_main_images]

        data_info_list = []
        data_wrappers = soup.find_all("div", class_="data-wrapper")

        for data_wrapper in data_wrappers:
            links = {}
            for a_tag in data_wrapper.select("a.tbx-tooltip.item-entry.important"):
                link = "https://myfigurecollection.net" + a_tag["href"]
                data_name = a_tag.find("span").get_text(strip=True)
                links[data_name] = link

            data_dict = {"wrapper_links": links}
            for data_field in data_wrapper.find_all("div", class_="data-field"):
                label = data_field.find("div", class_="data-label").get_text(strip=True)
                value = data_field.find("div", class_="data-value").get_text(strip=True)

                if label == "Links":
                    value = re.split(r'\.(com|net|org|info|jp)', value)
                    value = [value[i] + '.' + value[i + 1] for i in range(0, len(value) - 1, 2)]
                elif label == "Aliases":
                    value = value.split("(Also known as)")
                    value = [alias.strip() for alias in value if alias.strip()]

                data_dict[label] = value
            data_info_list.append(data_dict)

        # # Extract figure list Full
        # figure_list = []
        # page_number = 1
        # while True:
        #     get_fig_list_url = f"https://myfigurecollection.net/?_tb=item&orEntries%5B%5D={entry_id}&rootId=0&page={page_number}"
        #     response_fig_list = requests.get(get_fig_list_url)
        #     if response_fig_list.status_code == 200:
        #         soup_fig_list = BeautifulSoup(response_fig_list.content, 'html.parser')
        #         spans = soup_fig_list.find_all('span', class_='item-icon')
        #         if not spans:
        #             break  # No more figures found, exit the loop
        #         for span in spans:
        #             a_tag = span.find('a')
        #             img_tag = a_tag.find('img')
        #             figure_name = img_tag.get('alt', 'No Title Available').strip()
        #             figure_url = a_tag['href']
        #             image_url = img_tag.get('src', 'No Image Available').strip()
        #             figure_list.append({"figure_name": figure_name, "figure_url": figure_url, "image_url": image_url})
        #         page_number += 1
        #     else:
        #         break  # Error occurred, exit the loop

        # Extract figure list Per Page
        figure_list = []
        get_fig_list_url = f"https://myfigurecollection.net/?_tb=item&orEntries%5B%5D={entry_id}&rootId=0&page={page_number}"
        response_fig_list = requests.get(get_fig_list_url)
        if response_fig_list.status_code == 200:
            soup_fig_list = BeautifulSoup(response_fig_list.content, 'html.parser')
            for span in soup_fig_list.find_all('span', class_='item-icon'):
                a_tag = span.find('a')
                img_tag = a_tag.find('img')
                figure_name = img_tag.get('alt', 'No Title Available').strip()
                figure_url = 'https://myfigurecollection.net' + a_tag['href']
                image_url = img_tag.get('src', 'No Image Available').strip()
                figure_list.append({"figure_name": figure_name, "figure_url": figure_url, "image_url": image_url})

        return {
            "entry_name": item_name,
            "sub_entry_name": sub_item_name,
            "company_logo": company_logo,
            "enty_info_list": data_info_list,
            "figure_list": figure_list
        }

def get_entry_max_page_number(entry_id):
    url = f"https://myfigurecollection.net/?_tb=item&orEntries%5B%5D={entry_id}&rootId=0"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Check if the results-count-pages class is found
    results_count_pages_div = soup.find('div', class_='results-count-pages')
    if results_count_pages_div:
        # Find the last page link
        page_links = results_count_pages_div.find_all('a')
        
        if page_links:
            last_page_link = page_links[-1]
            max_page_number = int(last_page_link['href'].split('=')[-1])
            return max_page_number
    
    return 1  # You can adjust this default value as needed
