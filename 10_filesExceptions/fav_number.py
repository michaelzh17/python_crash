# -*- coding: utf-8 -*-


import json


def r_number():
	"""Read a number from a file; return the number or return None"""

	filename = 'fav1_number.json'

	try:
		with open(filename) as file_obj:
			number = json.load(file_obj)

	except FileNotFoundError:
		return None
	else:
		return number
		

def store_number():
	"""Ask user for a favorite number and store it in json file"""

	fav_number = input("Give me one of your favorite number: ")

	filename = 'fav1_number.json'

	with open(filename, 'w') as file_obj:
		json.dump(fav_number, file_obj)


def rem_number():
	"""Check stored number, if fail, ask user for their favorite number"""

	read_number = r_number()

	if read_number:
		print("I know your favorite number! It's " + read_number + ".")
	else:
		store_number()

rem_number()	




