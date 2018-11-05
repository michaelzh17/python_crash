# -*- coding: utf-8 -*-


def content(filename):
	"""Print out the content in a file"""

	try: 
		with open(filename) as object_file:
			contents = object_file.read()

	except FileNotFoundError:
		pass
		#print("File " + filename + " can't be found!")

	else:
		print("Content from " + filename + ":")
		print(contents)


filenames = ['cats.txt', 'dogs.txt', 'turtle.txt']

for filename in filenames:
	content(filename)