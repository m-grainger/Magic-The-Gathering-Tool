# magic price fetcher
# time.sleep() method is called at the request of the 
# scrython dev team.  This is to keep their service healthy.

import scrython
import time

card_list = []

def list_generator(*args):
	while True:
		card  = input("Please enter a card name to add to your list.  When you are done adding items, type 'done': ")
		card_list.append(card.title())	
		if "done" in card_list or "Done" in card_list:
			card_list.pop()
			
			return 

def name_and_price():
	for x in card_list:
		card = scrython.cards.Named(fuzzy=x)
		time.sleep(.20)
		# TO DO - add a try block here
		final_list = [card.name(), card.currency("usd")]
		print(final_list)

if __name__ == "__main__":
	list_generator()
	print("Here is a current list of your cards: ")
	print(card_list)
	name_and_price()

