#!/usr/bin/env python3
#server/seed.py
from random import choice as rc
from app import app,db
from models import Pet
from faker import Faker


with app.app_context():
    fake = Faker()  
    Pet.query.delete()
    pets = []
    species = ["Dog","Cat","Hamster","Snake"]
    for i in range(10):
        pets.append(Pet(name = fake.first_name(), species = rc(species) ))

    db.session.add_all(pets)
    db.session.commit()