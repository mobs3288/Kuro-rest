from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

def get_fig_data(item_id):
    url = f"https://myfigurecollection.net/item/{item_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    req = Request(url, headers=headers)
    page = urlopen(req)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    content_headline_div = soup.find("div", class_="content-headline")
    h1_element = content_headline_div.find("h1", itemprop="headline")
    main_links = soup.find_all("a", class_="main", _index="0")
    main_image_sources = [link.img['src'].replace("/items/1", "/items/2") for link in main_links]
    thumb_main_image_sources = [link.img['src'] for link in main_links]
    more_links = soup.find_all("a", class_="more")
    thumb_image_info_list = []
    image_info_list = []
    data_info_list = []
    
    for link in more_links:
        index = link.get("_index")
        style_attribute = link['style']
        thumb_image_url = re.search(r'url\((.*?)\)', style_attribute).group(1)
        thumb_image_info_list.append({"Thumbnails index": index, "image_url": thumb_image_url})
        image_url = re.search(r'url\((.*?)\)', style_attribute).group(1)
        image_url = image_url.replace("/thumbnails/", "/")
        image_info_list.append({"index": index, "image_url": image_url})

    data_wrappers = soup.find_all("div", class_="data-wrapper")
    for data_wrapper in data_wrappers:
        # Get all links associated with the wrapper
        links = {}
        a_tags = data_wrapper.find_all("a", class_="tbx-tooltip item-entry important")
        for a_tag in a_tags:
        # link = a_tag["href"]
            link = a_tag["href"]
            # Get the name associated with the link, which is the text inside the <span> tag
            data_name = a_tag.find("span").text.strip()
            full_link = "https://myfigurecollection.net" + link  # Concatenate base URL with link
            links[data_name] = full_link
        
        data_fields = data_wrapper.find_all("div", class_="data-field")
        data_dict = {"wrapper_links": links}
        for data_field in data_fields:
            label_element = data_field.find("div", class_="data-label")
            value_element = data_field.find("div", class_="data-value")
            
            label = label_element.text.strip() if label_element else ""
            value = value_element.text.strip() if value_element else ""

            if label == "Releases":
                # Split the releases and prices based on "As"
                releases_and_prices = value.split("As")
                
                releases = releases_and_prices[0].strip()
                # Extract release date
                release_date = releases.split("(")[0].strip()
                
                prices = releases_and_prices[1].strip()
                # Extract price using regular expression
                price_match = re.search(r'([\d,]+(?:\.\d+)?)\s*(\w+)', prices)
                if price_match:
                    price = price_match.group(1)
                    currency = price_match.group(2)
                else:
                    price = None
                    currency = None
                
                data_dict[label] = {"Releases": release_date, "Price": price + " " + currency}
            else:
                data_dict[label] = value
        data_info_list.append(data_dict)

    return {
        "item_name": h1_element.get_text() if h1_element else None,
        "figure_info_list": data_info_list,
        "full_image_sources": main_image_sources,
        "full_image_list": image_info_list,
        "thumb_main_image_sources": thumb_main_image_sources,
        "thumb_image": thumb_image_info_list,
    }
