import json
import requests
from random import randint
from time import sleep
from bs4 import BeautifulSoup

##TODO 
    # get the image URLs and rerun 
    # figure out why not all of them are going at the same time


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

    while page_num <= 15: 
        product_page = requests.get(f"https://www.ufseeds.com/vegetables?start={product_num}&sz=72")
        product_page_src = product_page.content
        product_soup = BeautifulSoup(product_page_src, 'lxml')

        for product in product_soup.find_all("div", {"class": "product"}):
            for link in product.find_all("a", {"class": "link"}, href=True):
                cleaned_link = ("https://www.ufseeds.com" + link['href']).strip()
                link_name = cleaned_link.replace("https://www.ufseeds.com/product/", "").split("/")[0].strip()
                veg_dict[link_name] = {"id":product_num, "link":cleaned_link }
                product_num+=1
        page_num+=1
        sleep(randint(2,10))

    print(len(veg_dict))
    # veg_urls = []

    # for key, value in veg_dict.items():
    #     name = key
    #     link = value["link"]
    #     veg_urls.append(link)

    # df = pd.DataFrame(veg_urls)
    # df.to_csv (r'veg_dict_urls.csv', index = False, header=False)
    # return print(f'updated veg_dict_urls.csv with {len(veg_dict)} records')
    return(veg_dict)

all_the_veg = find_all_veg_pages()

for key, value in all_the_veg.items():
    print(key, '->', value['link'])

######### specific page #########
    # 1) Define the page from veg_product_links
    product_page = requests.get(value['link'])
    product_page_src = product_page.content
    product_page_soup = BeautifulSoup(product_page_src, 'lxml')

    # 2) Grab the name of the product
    name = product_page_soup.find("h1", {"class": "product-name"}).text.strip()
    category = product_page_soup.find("p", {"class": "product-category"}).text.strip()
    short_descr = product_page_soup.find("div", {"class": "col-12 read-more__container"}).text.strip()

    all_the_veg[key]['name'] = name
    all_the_veg[key]['category'] = category
    all_the_veg[key]['short_descr'] = short_descr


    # 3) Grab the first set of dimensions from the product page
    for items in product_page_soup.find_all(class_="attribute-label"):
        attribute_label = items.text.strip()
        attribute_value = items.find_next("strong").text

        all_the_veg[key][attribute_label] = attribute_value

    # 4) Grab the 2nd set of dimensions from the product page
    growing_instructions = ["Before Planting:","Planting:",
                            "Watering:","Fertilizer:","Days to Maturity:",
                            "Harvesting:","Tips:","AVG. Direct Seeding Rate:"] 

    for blurb in growing_instructions:
            try: 
                blurb_data = product_page_soup.find("strong", text=blurb).next_sibling
                instruction_label = blurb
                instruction_value = blurb_data.strip()
                all_the_veg[key][instruction_label] = instruction_value
            except Exception:
                pass

    sleep(randint(2,15))

# print(all_the_veg)
with open('data.json', 'w') as fp:
    json.dump(all_the_veg, fp,  indent=4)

print("**** your data is readyyyyy ****")

#### SANDBOX ####

# result = requests.get("https://wwwcle.ufseeds.com/vegetables")
# print(result.status_code)
# src = result.content
# # print(src)
# soup = BeautifulSoup(src, 'lxml')
# range_of_page_header = soup.find_all("div", {"class":"range-of-page-footer"})
# # print(range_of_page_header)

# result = requests.get("https://www.ufseeds.com/product/cal-sweet-bush-f1-watermelon-seeds/WACSB.html")

# print(result.status_code)
# # print(result.headers)
# src = result.content
# # print(src)
# soup = BeautifulSoup(src, 'lxml')
# soup = BeautifulSoup(src, "html.parser")
# details = soup.find_all("p", {"class":"attribute-label"})
# # print(links)
# attributes_1 = []
# for detail in details:
#     attributes_1.append(detail.text.strip())
# print(attributes_1)

# for attribute in attributes_1:
#     label = soup.find("label", text="Botanical Name")
#     print(label.next_sibling.strip())