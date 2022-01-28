import requests
from bs4 import BeautifulSoup

## find all the pages

# result = requests.get("https://www.ufseeds.com/vegetables")
# src = result.content
# soup = BeautifulSoup(src, 'lxml')

# for items in soup.find_all(class_="attribute-label")


 ## specific page
result = requests.get("https://www.ufseeds.com/product/cal-sweet-bush-f1-watermelon-seeds/WACSB.html")
src = result.content
soup = BeautifulSoup(src, 'lxml')


for items in soup.find_all(class_="attribute-label"):
    data = items.find_next("strong").text
    print(items.text.strip())
    print(f"- {data}")

growing_instructions = ["Before Planting:","Planting:","Watering:","Fertilizer:","Days to Maturity:","Harvesting:","Tips:","AVG. Direct Seeding Rate:"]



for blurb in growing_instructions:
    blurb_data = soup.find("strong", text=blurb).next_sibling
    print(blurb)
    print(f"- {blurb_data.strip()}")
    # print(f"- {data}")


#### SANDBOX ####

# result = requests.get("https://www.ufseeds.com/vegetables")
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