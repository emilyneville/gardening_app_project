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
for plant, plant_attributes in plant_data:
    name,category,image_url = (
        plant_attributes["name"],
        plant_attributes["category"],
        plant_attributes["image_url"],
    )

    db_plant = crud.create_plant(name,category,image_url)
    plants_in_db.append(db_plant)

model.db.session.add_all(plants_in_db)
model.db.session.commit()