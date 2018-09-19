import pprint
import pymongo
from pymongo import MongoClient
import scrython


client = MongoClient()
db = client.mtg
collection = db.cards
posts = collection

example_card = { "card_name" : "Example Card Name",
				 "mana_cost" : ["Blue", "Red"],
				 "card_rarity" : "common",
				 "card_text" : "This is an example card that does stuff",
				 "card_attributes" : ["Vigilance","Menace"],
				 "atk_def": "5 / 5"}

post_id = posts.insert_one(example_card).inserted_id

pprint.pprint(posts.find_one())
