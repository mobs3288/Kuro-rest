from bs4 import BeautifulSoup
import requests

def get_releases_date_figure(year, month, page_number):
    figure_list = []
    get_fig_list_url = f"https://myfigurecollection.net/?tab=calendar&rootId=0&status=-1&categoryId=-1&contentLevel=-1&excludeContentLevel=0&domainId=-1&noReleaseDate=0&releaseTypeId=0&ratingId=0&isCastoff=0&hasBootleg=0&tagId=0&noBarcode=0&clubId=0&excludeClubId=0&listId=0&isDraft=0&year={year}&month={month}&acc=0&separator=0&sort=insert&output=2&current=categoryId&order=desc&page={page_number}&_tb=item"
    response = requests.get(get_fig_list_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for group_div in soup.find_all('div', class_='item-group-by'):
            date_heading = group_div.find('h3').text.strip()  # Extract the date
            for item_icon in group_div.find_all('span', class_='item-icon'):
                figure_name = item_icon.find('img')['alt']  # Extract the figure name
                figure_url = "https://myfigurecollection.net" + item_icon.find('a')['href']  # Extract the figure URL
                image_url = item_icon.find('img')['src']  # Extract the image URL
                category = item_icon.find('a')['class'][-1].split('-')[-1]  # Extract the category
                figure_list.append({
                    "date": date_heading,
                    "figure_name": figure_name,
                    "figure_url": figure_url,
                    "image_url": image_url,
                    "category": category
                })

    return {
        "figure_list": figure_list,
    }

def get_releases_date_max_page_number(year, month, page_number):
    url = f"https://myfigurecollection.net/?tab=calendar&rootId=0&status=-1&categoryId=-1&contentLevel=-1&excludeContentLevel=0&domainId=-1&noReleaseDate=0&releaseTypeId=0&ratingId=0&isCastoff=0&hasBootleg=0&tagId=0&noBarcode=0&clubId=0&excludeClubId=0&listId=0&isDraft=0&year={year}&month={month}&acc=0&separator=0&sort=insert&output=2&current=categoryId&order=desc&page={page_number}&_tb=item"
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
