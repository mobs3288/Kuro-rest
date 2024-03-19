from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests

def get_most_rated_figure():
    figure_list = []
    get_fig_list_url = f"https://myfigurecollection.net/?tab=top&rootId=0&top=bestRated&extra=0&_tb=item"
    response_fig_list = requests.get(get_fig_list_url)
    if response_fig_list.status_code == 200:
        soup_fig_list = BeautifulSoup(response_fig_list.content, 'html.parser')
        for div in soup_fig_list.find_all('div', class_='result'):
            meta_div = div.find('div', class_='result-meta')  # Find the meta div containing figure metadata
            figure_rank = meta_div.text.strip()  # Extract figure rank
            a_tag = div.find('a')  # Find the figure link
            if a_tag is not None:  # Check if <a> tag is found
                img_tag = a_tag.find('img')  # Find the image tag
                if img_tag is not None:  # Check if <img> tag is found
                    figure_name = img_tag.get('alt', 'No Title Available').strip()  # Extract figure name
                    figure_url = 'https://myfigurecollection.net' + a_tag['href']  # Extract figure URL
                    image_url = img_tag.get('src', 'No Image Available').strip()  # Extract image URL
                    category_div = div.find('div', class_='stamp-category')  # Find the category div
                    category = category_div.text.strip()  # Extract category
                    figure_list.append({
                        "figure_rank": figure_rank,
                        "figure_name": figure_name,
                        "figure_url": figure_url,
                        "image_url": image_url,
                        "category": category
                    })

    return {
        "figure_list": figure_list,
    }


