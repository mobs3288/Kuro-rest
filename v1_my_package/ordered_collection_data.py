from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests

def get_ordered_figure_by_uname(username, page_number):
    url = f"https://myfigurecollection.net/profile/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        content_headline_div = soup.find("div", class_="content-headline")
        h1_element = content_headline_div.find("h1", itemprop="headline")

        thumb_img = soup.find("img", class_="thumbnail")
        if thumb_img:
            thumb_image_source = thumb_img["src"]
            full_image_source = thumb_image_source.replace("64", "200")

        data_fields = soup.find_all("div", class_="data-field")

        data = {}
        for field in data_fields:
            label = field.find("div", class_="data-label").get_text(strip=True)
            value = field.find("div", class_="data-value").get_text(strip=True)
            data[label] = value

        # Extract figure list Per Page
        figure_list = []
        get_fig_list_url = f"https://myfigurecollection.net/?mode=view&username={username}&tab=collection&status=1&current=keywords&rootId=0&categoryId=-1&output=2&sort=category&order=asc&_tb=user&page={page_number}"
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
            "username": h1_element.get_text() if h1_element else None,
            "thumb_image_user": thumb_image_source,
            "full_image_user" : full_image_source,
            "about": data,
            "ordered_figure_list": figure_list,
        }

def get_ordered_collection_max_page(username):
    url = f"https://myfigurecollection.net/?_tb=user&mode=view&username={username}&tab=collection&rootId=0&status=1"
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
