# -*- coding: utf8 -*-
import random
import json

# Read values from a Json file
def read_value_from_json():
    # Create a new empty list
    values = []
    # Open a json file with my objects
    with open('characters.json') as f: 
        # Load all the data contained in my file. data = entries
     data = json.load(f)
    for entry in data:
        # Add each item in my list
        values.append(entry["character"])
        # Return my completed list
    return values   

def message(character, quote):
    n_character = character.capitalize()
    n_quote = quote.capitalize()
    return "{} a dit : {}".format(n_character, n_quote)  

def get_random_item_in(my_list):
    rand_numb = random.randint(0, len(my_list) - 1)
    item = my_list[rand_numb] # get a quote from a list
    return item # return the item

def get_random_quote():
    all_values = read_values_from_json('quotes.json', 'quote')
    return get_random_item_in(all_values)

def random_character():
    all_values = read_values_from_json()
    return get_random_item(all_values)

# Programm
user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')

while user_answer != "B":
    print(message(random_character(), random_character()))
    user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')

