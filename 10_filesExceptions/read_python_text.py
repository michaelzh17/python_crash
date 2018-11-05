# -*- coding: utf-8 -*-

file_add = 'text_files/learning_python.txt'

with open(file_add) as file_object:

	#for line in file_object:
		#print(line.rstrip())
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())





