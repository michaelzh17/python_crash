# -*- coding: utf-8 -*-

import json

def r_number():
	"""Read a number from a file; return the number or return None"""

	filename = 'fav_number.json'

	try:
		with open(filename) as file_obj:
			number = json.load(file_obj)

	except FileNotFoundError:
		return None
	else:
		print("I know your favorite number! It's " + number + ".")

r_number()