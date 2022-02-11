import json
import requests
from random import randint
from time import sleep
from bs4 import BeautifulSoup

##TODO 
    # add on image url, carrot at the top?
    # try / except


headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

def find_all_veg_pages():
## to find all the veg pages
## FYI approx 1.1k objects, so assume 15 pages
## https://www.ufseeds.com/vegetables?sz=72&start=72
    veg_dict = {}
    page_num = 1
    product_num = 0

    while page_num <= 1: 
        product_page = requests.get(f"https://www.ufseeds.com/fruits?start=0&sz=72")
        product_page_src = product_page.content
        product_soup = BeautifulSoup(product_page_src, 'lxml')

        for product in product_soup.find_all("div", {"class": "product"}):
            for link in product.find_all("a", {"class": "link"}, href=True):
                cleaned_link = ("https://www.ufseeds.com" + link['href']).strip()
                link_name = cleaned_link.replace("https://www.ufseeds.com/product/", "").split("/")[0].strip()
                veg_dict[link_name] = {"id":product_num, "link":cleaned_link }
                product_num+=1
        page_num+=1
        sleep(randint(2,5))
    print(len(veg_dict))
    return(veg_dict)

all_the_veg = find_all_veg_pages()

for key, value in all_the_veg.items():
    print(value['id'], ' ',key, '->', value['link'])
    try:
        product_page = requests.get(value['link'])
        product_page_src = product_page.content
        product_page_soup = BeautifulSoup(product_page_src, 'lxml')
        path = f'/home/hackbright/src/project/beautifulsoup/bs_fruit/bs_fruit_files/{key}.txt'
        with open(path, 'w', encoding='utf-8') as f_out:
            f_out.write(product_page_soup.prettify())

        sleep(randint(2,10))
    except Exception:
                pass