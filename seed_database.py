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
    name,category,image_url,short_descr,botanical_name,seed_type,fruit_color,breed,maturity,life_cycle,sow_method,before_planting,planting,watering,days_to_maturity_text,harvesting,tips=(
        plant_attributes.get("name"),
        plant_attributes.get("category"),
        plant_attributes.get("img_url"),
        plant_attributes.get("short_descr"),
        plant_attributes.get("Botanical Name"),
        plant_attributes.get("Seed Type"),
        plant_attributes.get("Fruit Color"),
        plant_attributes.get("Breed"),
        plant_attributes.get("Maturity"),
        plant_attributes.get("Life Cycle"),
        plant_attributes.get("Sow Method"),
        plant_attributes.get("Before Planting:"),
        plant_attributes.get("Planting:"),
        plant_attributes.get("Watering:"),
        plant_attributes.get("Fertilizer:"),
        plant_attributes.get("Harvesting:"),
        plant_attributes.get("Tips:")
    )

    db_plant = crud.create_plant(name,category,image_url,short_descr,
    botanical_name, seed_type,fruit_color,breed,maturity,life_cycle,
    sow_method,before_planting,planting,watering,
    days_to_maturity_text,harvesting,tips
    )
    plants_in_db.append(db_plant)

model.db.session.add_all(plants_in_db)
model.db.session.commit()


# Create 10 users; each user will make 10 ratings
for n in range(10):
    email = f"user{n}@test.com"
    password = "test"

    user = crud.create_user(email, password)
    model.db.session.add(user)

    for _ in range(10):
        random_plant = choice(plants_in_db)

        favorite = crud.create_favorite(user, random_plant)
        model.db.session.add(favorite)

model.db.session.commit()

# exec sql statement
