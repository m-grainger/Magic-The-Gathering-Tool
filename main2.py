from math import ceil
import scrython
import time

from pymongo import MongoClient

card_list = []

client = MongoClient()
db = client.mtg
collection = db.cards
posts = collection

def list_generator(*args):
	while True:
		card  = input("Please enter a card.  When you are done adding items, type 'done': ")
		card_list.append(card.title())	
		if "done" in card_list or "Done" in card_list:
			card_list.pop()
			
			return 

def generate_card_details():
	for x in card_list:
		insert_dict = {}
		card = scrython.cards.Named(fuzzy=x)
		try:
			card_name = card.name()
			insert_dict.update({"Card Name":card_name})
		except:
			pass
		time.sleep(.1)	
		try:
			card_value = card.currency("usd")
			insert_dict.update({"Card Value (USD)":f"${float(card_value)}"})
		except:
			pass
		time.sleep(.1)
		try:
			card_rarity = card.rarity()
			insert_dict.update({"Rarity":card_rarity})
		except:
			pass
		time.sleep(.1)				
		try:
			card_mana_cost = card.mana_cost()
			insert_dict.update({"Mana Cost":card_mana_cost})
		except:
			pass
		time.sleep(.1)
		try:
			card_type_line = card.type_line()
			insert_dict.update({"Type Line":card_type_line})
		except:
			pass
		time.sleep(.1)			
		try:
			card_power = card.power() # won't work if the card is not a creature
			insert_dict.update({"Power":card_power})
		except:
			pass
		time.sleep(.1)
		try:
			card_toughness = card.toughness() # only works for creature cards
			insert_dict.update({"Toughness":card_toughness})
		except:
			pass
		time.sleep(.1)
		try:
			card_loyalty = card.loyalty() # only works for planeswalkers
			insert_dict.update({"Loyalty":card_loyalty})
		except:
			pass
		time.sleep(.1)
		try:
			card_oracle_text = card.oracle_text()
			insert_dict.update({"Oracle Text":card_oracle_text})
		except:
			pass
		time.sleep(.1)
		try:
			card_flavor_text = card.flavor_text()
			insert_dict.update({"Flavor Text":card_flavor_text})
		except:
			pass
		time.sleep(.1)		
		try:
			card_set_code = card.set_code()
			insert_dict.update({"Set Code":card_set_code})
		except:
			pass
		time.sleep(.1)
		try:
			card_set_name = card.set_name()
			insert_dict.update({"Set Name":card_set_name})
		except:
			pass
		time.sleep(.1)											
		try:
			card_artist = card.artist()
			insert_dict.update({"Artist":card_artist})
		except:
			pass
		time.sleep(.1)	
		try:
			card_border_color = card.border_color()
			insert_dict.update({"Border Color":card_border_color})
		except:
			pass
		time.sleep(.1)	
		try:
			card_color_identity = card.color_identity()
			insert_dict.update({"Color Identity":card_color_identity})
		except:
			pass
		time.sleep(.1)
		try:
			card_color_indicator = card.color_indicator()
			insert_dict.update({"Color Indicator":card_color_indicator})
		except:
			pass
		time.sleep(.1)
		try:
			card_colors = card.colors()
			insert_dict.update({"Colors":card_colors})
		except:
			pass
		time.sleep(.1)
		try:
			card_edhrec_rank = card.edhrec_rank()
			insert_dict.update({"EDH Rank":card_edhrec_rank})
		except:
			pass
		time.sleep(.1)			
		try:
			card_layout = card.layout()
			insert_dict.update({"Layout":card_layout})
		except:
			pass
		time.sleep(.1)
		try:
			card_object = card.object()
			insert_dict.update({"Card Object":card_object})
		except:
			pass
		time.sleep(.1)		
		try:
			card_faces = card.card_faces()
			insert_dict.update({"Card Faces":card_faces})
		except:
			pass
		time.sleep(.1)
		try:
			card_color_indicator = card.color_indicator()
			insert_dict.update({"Color Indicator":card_color_indicator})
		except:
			pass
		time.sleep(.1)	
		try:
			card_printed_text = card.printed_text()
			insert_dict.update({"Printed Text":card_printed_text})
		except:
			pass
		time.sleep(.1)
		try:
			card_story_spotlight = card.story_spotlight()
			insert_dict.update({"Story Spotlight":card_story_spotlight})
		except:
			pass
		time.sleep(.1)
		try:
			card_legalities = card.legalities()
			insert_dict.update({"Legalitity":card_legalities})
		except:
			pass
		time.sleep(.1)
		try:
			card_id = card.id()
			insert_dict.update({"Card ID":card_id})
		except:
			pass
		time.sleep(.1)
		try:
			card_illustration_id = card.illustration_id()
			insert_dict.update({"Illustration ID":card_illustration_id})
		except:
			pass
		time.sleep(.1)
		try:
			card_scryfall_set_uri = card.scryfall_set_uri()
			insert_dict.update({"Scryfall Set URI":card_scryfall_set_uri})
		except:
			pass	
		time.sleep(.1)				
		
##################################################
		try:
			card_uri = card.uri()
			insert_dict.update({"Card URI":card_uri})
		except:
			pass
		time.sleep(.1)
		try:
			card_scryfall_uri = card.scryfall_uri()
			insert_dict.update({"Scryfall URI":card_scryfall_uri})
		except:
			pass
		time.sleep(.1)		
		try:
			card_set_uri = card.set_uri()
			insert_dict.update({"Card Set URI": card_set_uri})
		except:
			pass
		time.sleep(.1)		
		try:
			card_multiverse_ids = card.card_multiverse_ids()
			insert_dict.update({"Multiverse IDs":card_multiverse_ids})
		except:
			pass
		time.sleep(.1)
		try:
			card_oracle_id = card.card_oracle_id()
			insert_dict.update({"Oracle ID":card_oracle_id})
		except:
			pass
		time.sleep(.1)
		try:
			card_image_uris = card.image_uris()
			insert_dict.update({"Image URIs":card_image_uris})
		except:
			pass
		time.sleep(.1)
		try:
			card_rulings_uri = card.rulings_uri()
			insert_dict.update({"Rulings URI":card_rulings_uri})
		except:
			pass
		time.sleep(.1)				
		try:
			card_purchase_uris = card.purchase_uris()
			insert_dict.update({"Purchase URIs":card_purchase_uris})
		except:
			pass

##################################################
		
		print("\n")
		for k,v in insert_dict.items():print(f"{k}:{v}")
		print("\n")

		# insert into mongodB
		post_id = posts.insert_one(insert_dict).inserted_id


def price_checker():
	total_price = 0
	for x in card_list:
		card = scrython.cards.Named(fuzzy=x)
		card_value = float(card.currency("usd"))
		print(f"{card.name()} - ${card_value}")
		total_price += card_value
		time.sleep(.1)
	total_price = ceil(total_price * 100) / 100.0	
	print(f"Total value of cards entered: ${total_price}")

if __name__ == "__main__":
	
	list_generator()
	init_price_checker = input("Would you like to enter these card(s) into MongoDB? (type y or n)")
	if init_price_checker == "y" or init_price_checker == "Y":
		generate_card_details()
	else:	
		price_checker()
	# print("Here is a current list of your cards: ")
	# print(card_list)
