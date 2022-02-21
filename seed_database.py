"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb plants")
os.system("createdb plants")

model.connect_to_db(server.app)
model.db.create_all()


# Load plant data from JSON file
with open("data/veg_data.json") as f:
    plant_data = json.loads(f.read())

plants_in_db = []
for plant, plant_attributes in plant_data.items():
    name =  plant_attributes.get("name", "No name found")
    plant_type =  plant_attributes.get("cat_1")
    category =  plant_attributes.get("cat_2")
    image_url = plant_attributes.get("img_url")
    short_descr = plant_attributes.get("short_descr")
    botanical_name = plant_attributes.get("Botanical Name")
    seed_type = plant_attributes.get("Seed Type")
    fruit_color = plant_attributes.get("Fruit Color")
    breed = plant_attributes.get("Breed")
    maturity = plant_attributes.get("Maturity")
    sun = plant_attributes.get("Sun")
    life_cycle = plant_attributes.get("Life Cycle")
    sow_method = plant_attributes.get("Sow Method")
    before_planting = plant_attributes.get("before_planting")
    planting = plant_attributes.get("planting")
    watering = plant_attributes.get("watering")
    days_to_maturity_text = plant_attributes.get("days_to_maturity")
    fertilizer = plant_attributes.get("fertilizer")
    harvesting = plant_attributes.get("havesting")
    tips = plant_attributes.get("tips")
    sub_category = plant_attributes.get("cat_3")
    days_to_maturity = plant_attributes.get("Days To Maturity (# Days)")
    fruit_weight_oz = plant_attributes.get("Fruit Weight")
    row_spacing_in = plant_attributes.get("Row Spacing")
    sow_depth_in = plant_attributes.get("Sow Depth"),
    plant_spacing_in = plant_attributes.get("Plant Spacing")
    plant_weight_in = plant_attributes.get("Weight")
    plant_depth_in = plant_attributes.get("Depth")
    plant_height_in = plant_attributes.get("Height")
    plant_width_in = plant_attributes.get("Width")
    zone_list = plant_attributes.get("Zones")
    
    print(plant_attributes.get("name", "No name found"))
    db_plant = crud.create_plant(name,plant_type, category,image_url,short_descr,
    botanical_name, seed_type,fruit_color,breed,maturity,sun,life_cycle,
    sow_method,before_planting,planting,days_to_maturity_text, watering,
    harvesting,tips, sub_category, days_to_maturity,fruit_weight_oz,row_spacing_in, sow_depth_in,
    plant_spacing_in,plant_weight_in,plant_depth_in,plant_height_in,plant_width_in,zone_list
    )
    plants_in_db.append(db_plant)

model.db.session.add_all(plants_in_db)
model.db.session.commit()

# Load plant data from JSON file
with open("data/herb_data.json") as f:
    herb_data = json.loads(f.read())

herbs_in_db = []
for plant, plant_attributes in herb_data.items():
    name =  plant_attributes.get("name", "No name found")
    plant_type =  plant_attributes.get("cat_1")
    category =  plant_attributes.get("cat_2")
    image_url = plant_attributes.get("img_url")
    short_descr = plant_attributes.get("short_descr")
    botanical_name = plant_attributes.get("Botanical Name")
    seed_type = plant_attributes.get("Seed Type")
    fruit_color = plant_attributes.get("Fruit Color")
    breed = plant_attributes.get("Breed")
    maturity = plant_attributes.get("Maturity")
    sun = plant_attributes.get("Sun")
    life_cycle = plant_attributes.get("Life Cycle")
    sow_method = plant_attributes.get("Sow Method")
    before_planting = plant_attributes.get("before_planting")
    planting = plant_attributes.get("planting")
    watering = plant_attributes.get("watering")
    days_to_maturity_text = plant_attributes.get("days_to_maturity")
    fertilizer = plant_attributes.get("fertilizer")
    harvesting = plant_attributes.get("havesting")
    tips = plant_attributes.get("tips")
    sub_category = plant_attributes.get("cat_3")
    days_to_maturity = plant_attributes.get("Days To Maturity (# Days)")
    fruit_weight_oz = plant_attributes.get("Fruit Weight")
    row_spacing_in = plant_attributes.get("Row Spacing")
    sow_depth_in = plant_attributes.get("Sow Depth"),
    plant_spacing_in = plant_attributes.get("Plant Spacing")
    plant_weight_in = plant_attributes.get("Weight")
    plant_depth_in = plant_attributes.get("Depth")
    plant_height_in = plant_attributes.get("Height")
    plant_width_in = plant_attributes.get("Width")
    zone_list = plant_attributes.get("Zones")
    
    
    db_plant = crud.create_plant(name,plant_type, category,image_url,short_descr,
    botanical_name, seed_type,fruit_color,breed,maturity,sun,life_cycle,
    sow_method,before_planting,planting,days_to_maturity_text, watering,
    harvesting,tips, sub_category, days_to_maturity,fruit_weight_oz,row_spacing_in, sow_depth_in,
    plant_spacing_in,plant_weight_in,plant_depth_in,plant_height_in,plant_width_in,zone_list
    )
    plants_in_db.append(db_plant)
    print(plant_attributes.get("name", "No name found"))
model.db.session.add_all(herbs_in_db)
model.db.session.commit()



# Load plant data from JSON file
with open("data/fruit_data.json") as f:
    fruit_data = json.loads(f.read())

fruits_in_db = []
for plant, plant_attributes in fruit_data.items():
    name =  plant_attributes.get("name", "No name found")
    plant_type =  plant_attributes.get("cat_1")
    category =  plant_attributes.get("cat_2")
    image_url = plant_attributes.get("img_url")
    short_descr = plant_attributes.get("short_descr")
    botanical_name = plant_attributes.get("Botanical Name")
    seed_type = plant_attributes.get("Seed Type")
    fruit_color = plant_attributes.get("Fruit Color")
    breed = plant_attributes.get("Breed")
    maturity = plant_attributes.get("Maturity")
    sun = plant_attributes.get("Sun")
    life_cycle = plant_attributes.get("Life Cycle")
    sow_method = plant_attributes.get("Sow Method")
    before_planting = plant_attributes.get("before_planting")
    planting = plant_attributes.get("planting")
    watering = plant_attributes.get("watering")
    days_to_maturity_text = plant_attributes.get("days_to_maturity")
    fertilizer = plant_attributes.get("fertilizer")
    harvesting = plant_attributes.get("havesting")
    tips = plant_attributes.get("tips")
    sub_category = plant_attributes.get("cat_3")
    days_to_maturity = plant_attributes.get("Days To Maturity (# Days)")
    fruit_weight_oz = plant_attributes.get("Fruit Weight")
    row_spacing_in = plant_attributes.get("Row Spacing")
    sow_depth_in = plant_attributes.get("Sow Depth"),
    plant_spacing_in = plant_attributes.get("Plant Spacing")
    plant_weight_in = plant_attributes.get("Weight")
    plant_depth_in = plant_attributes.get("Depth")
    plant_height_in = plant_attributes.get("Height")
    plant_width_in = plant_attributes.get("Width")
    zone_list = plant_attributes.get("Zones")
    
    print(plant_attributes.get("name", "No name found"))
    db_plant = crud.create_plant(name,plant_type, category,image_url,short_descr,
    botanical_name, seed_type,fruit_color,breed,maturity,sun,life_cycle,
    sow_method,before_planting,planting,days_to_maturity_text, watering,
    harvesting,tips, sub_category, days_to_maturity,fruit_weight_oz,row_spacing_in, sow_depth_in,
    plant_spacing_in,plant_weight_in,plant_depth_in,plant_height_in,plant_width_in,zone_list
    )
    plants_in_db.append(db_plant)

model.db.session.add_all(fruits_in_db)
model.db.session.commit()


#super user profile :) 
email = f"emily@emily.emily"
password = "emily"
user = crud.create_user(email, password)
model.db.session.add(user)

# Create 10 users; each user will make 10 ratings
for n in range(10):
    email = f"user{n}@test.com"
    password = "test"

    user = crud.create_user(email, password)
    model.db.session.add(user)



model.db.session.commit()

