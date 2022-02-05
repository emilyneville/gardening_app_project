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


# Load movie data from JSON file
# with open("data/movies.json") as f:
#     movie_data = json.loads(f.read())