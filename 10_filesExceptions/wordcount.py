# -*- coding: utf-8 -*-

def count_word(filename, word):
	"""Count the number of ‘word' in file"""

	with open(filename) as file_object:
		contents = file_object.read()
		count_word = contents.lower().count(word)

	print(word + " appears in file " + filename + " " + str(count_word) + " times.")

	#print(type(contents))

filename = 'Emma.txt'
count_word(filename, 'emma')
count_word(filename, 'the')
count_word(filename, 'love')