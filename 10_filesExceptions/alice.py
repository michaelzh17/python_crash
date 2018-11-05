# -*- coding: utf-8 -*-
def count_words(filename):
	"""Count the approximate number of words in a file."""

	try:

		with open(filename, encoding='utf-8') as f_obj:
			contents = f_obj.read()

	except FileNotFoundError:
		pass	
		#msg = "sorry, the file name " + filename + " can't be found."
		#print(msg)

	else:
		#Count the number of words in the file.
		words = contents.split()
		lengh = len(words)

		print("The total number of words in file " + filename + " is " + str(lengh) + ".")



#filename = 'text_files/alice.txt'

filenames = ['text_files/alice.txt', 'alice.txt']

for filename in filenames:
	count_words(filename)



