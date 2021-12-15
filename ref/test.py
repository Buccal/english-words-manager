import pymongo
from config import *
import json

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
template_words = db["TEMPLATE_WORDS"]
user = db["User"]

users_info = [
    {
        "username": "alice",
        "email": "alice@example.com",
        "hashed_password": "NWewxd6IvYXCTmHKNPzpbkjJdVXQ/pW7H2GaZwSQCTiXYUGK7uhMUCYVCl4tPaxOVR7XEZ2n0MjIe1GyHvRRUoLmcYUFVadYc2+eM5CmPIfzl5P5RnymgJpCPolT1P3jiN0O/ruatofIwQfBOSC+k+mfP5x/i2DmwJH4ZfepXes=",
        "disabled": False,
    },
    {
        "username": "johndoe",
        "email": "johndoe@example.com",
        "hashed_password": "Mnxt8KgRjkSerQTOxwhMEJoVXj4P92x4aBWAFAHRafLvm5XQhC1M5B993DlaJe5KHtjYAmX1yiKJnOXzLFJL75ff6i+dUgCYYk2Iq8TYL72kOe4RRJGcvefmvdAhI/qzNRsLaBvR//K3ZWjAlN+jCfMmYAWtu71Z4gtstcBDg8Y=",
        "disabled": True,
    }
]

user.insert_many(users_info)

# from decrypt_data import decrypt_data

# encode_password = "mO34nsfRHnyKj4tj4Mah4F5AzXRjFHhg/DtacwiJJRdmxyLsECkEKX57e0jaSKZPdFNtgpaW9q0ruODaIKVy8HnUFa2Gk1JwXjR1i1bS0w+CV9Iq2zkgkJkEp5yf/0oM95mkF4MQs/NKaQyEEoedeULghqgw0G+RSuJkK8x8Rm4="
# print(decrypt_data(encode_password))