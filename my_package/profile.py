from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests

def get_profile_data(username):
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
        owned_figure_list = []
        get_fig_list_url = f"https://myfigurecollection.net/?mode=view&username={username}&tab=collection&status=2&current=keywords&rootId=0&categoryId=-1&output=2&sort=category&order=asc&_tb=user&page=1"
        response_fig_list = requests.get(get_fig_list_url)
        if response_fig_list.status_code == 200:
            soup_fig_list = BeautifulSoup(response_fig_list.content, 'html.parser')
            for span in soup_fig_list.find_all('span', class_='item-icon'):
                a_tag = span.find('a')
                img_tag = a_tag.find('img')
                figure_name = img_tag.get('alt', 'No Title Available').strip()
                figure_url = 'https://myfigurecollection.net' + a_tag['href']
                image_url = img_tag.get('src', 'No Image Available').strip()
                owned_figure_list.append({"figure_name": figure_name, "figure_url": figure_url, "image_url": image_url})

        ordered_figure_list = []
        get_fig_list_url = f"https://myfigurecollection.net/?mode=view&username={username}&tab=collection&status=1&current=keywords&rootId=0&categoryId=-1&output=2&sort=category&order=asc&_tb=user&page=1"
        response_fig_list = requests.get(get_fig_list_url)
        if response_fig_list.status_code == 200:
            soup_fig_list = BeautifulSoup(response_fig_list.content, 'html.parser')
            for span in soup_fig_list.find_all('span', class_='item-icon'):
                a_tag = span.find('a')
                img_tag = a_tag.find('img')
                figure_name = img_tag.get('alt', 'No Title Available').strip()
                figure_url = 'https://myfigurecollection.net' + a_tag['href']
                image_url = img_tag.get('src', 'No Image Available').strip()
                ordered_figure_list.append({"figure_name": figure_name, "figure_url": figure_url, "image_url": image_url})

        wished_figure_list = []
        get_fig_list_url = f"https://myfigurecollection.net/?mode=view&username={username}&tab=collection&status=0&current=keywords&rootId=0&categoryId=-1&output=2&sort=category&order=asc&_tb=user&page=1"
        response_fig_list = requests.get(get_fig_list_url)
        if response_fig_list.status_code == 200:
            soup_fig_list = BeautifulSoup(response_fig_list.content, 'html.parser')
            for span in soup_fig_list.find_all('span', class_='item-icon'):
                a_tag = span.find('a')
                img_tag = a_tag.find('img')
                figure_name = img_tag.get('alt', 'No Title Available').strip()
                figure_url = 'https://myfigurecollection.net' + a_tag['href']
                image_url = img_tag.get('src', 'No Image Available').strip()
                wished_figure_list.append({"figure_name": figure_name, "figure_url": figure_url, "image_url": image_url})

        return {
            "username": h1_element.get_text() if h1_element else None,
            "thumb_image_user": thumb_image_source,
            "full_image_user" : full_image_source,
            "about": data,
            "owned_figure_list": owned_figure_list,
            "ordered_figure_list": ordered_figure_list,
            "wished_figure_list": wished_figure_list,
        }