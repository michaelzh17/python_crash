# -*- coding: utf-8 -*-

file_addr = 'text_files/learning_python.rtf'

with open(file_addr) as file_object:
	for line in file_object:
		print(line.replace('Python', 'C').rstrip())



