# -*- coding: utf-8 -*-

import json

def store_number():
	"""Ask user for a favorite number and store it in json file"""

	fav_number = input("Give me one of your favorite number: ")

	filename = 'fav_number.json'

	with open(filename, 'w') as file_obj:
		json.dump(fav_number, file_obj)




store_number()