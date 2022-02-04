import json
import requests
import os
from bs4 import BeautifulSoup
import re

directory = 'beautifulsoup_files'

product_id_counter = 1
veg_dict = {}

## define id, plant, file location, soup
for filename in os.scandir(directory):
    if filename.is_file():
        with open(filename.path) as f:
            soup = BeautifulSoup(f.read(), 'lxml')
        name_str = str(soup.find("h1", {"class": "product-name"}).text.strip()).replace(" ", "_")
        name_r = re.findall(r"\w", name_str)
        name_id = "".join(name_r).lower()
        veg_dict[name_id] = {"id":product_id_counter, "dir":filename.path }
        
        print("#" + str(product_id_counter) + " " + name_id + " -> " + filename.path)

        ##  Grab the name of the product + key info
        name = soup.find("h1", {"class": "product-name"}).text.strip().replace("Seeds", "")
        category = soup.find("p", {"class": "product-category"}).text.strip()
        short_descr = soup.find("div", {"class": "col-12 read-more__container"}).text.strip()
        img = soup.find(itemprop="image")

        veg_dict[name_id]['name'] = name.replace("Seed", "").strip()
        veg_dict[name_id]['category'] = category
        veg_dict[name_id]['short_descr'] = short_descr
        veg_dict[name_id]['img_url'] = img["src"]


        ## Grab the first set of dimensions from the product page
        for items in soup.find_all(class_="attribute-label"):
            attribute_label = items.text.strip()
            attribute_value = items.find_next("strong").text.strip()

            veg_dict[name_id][attribute_label] = attribute_value

        ## Grab the 2nd set of dimensions from the product page
        growing_instructions = ["Before Planting:","Planting:",
                                "Watering:","Fertilizer:","Days to Maturity:",
                                "Harvesting:","Tips:","AVG. Direct Seeding Rate:"] 

        for blurb in growing_instructions:
                try:
                    blurb_data = soup.find("strong", text=blurb).next_sibling
                    instruction_label = blurb
                    instruction_value = blurb_data.strip()
                    veg_dict[name_id][instruction_label] = instruction_value
                except Exception:
                    pass
        product_id_counter += 1

print(" **** THE DATA IS DONE ****")

# # print(veg_dict)
with open('/home/hackbright/src/project/data/veg_data.json', 'w') as fp:
    json.dump(veg_dict, fp,  indent=4)