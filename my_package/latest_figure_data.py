from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests

def get_latest_figure(page_number):
        figure_list = []
        get_fig_list_url = f"https://myfigurecollection.net/?_tb=item&mode=browse&rootId=0&page={page_number}"
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
            "figure_list": figure_list,
        }

def get_latest_max_page():
    url = f"https://myfigurecollection.net/?_tb=item&mode=browse&rootId=0&page=1"
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
