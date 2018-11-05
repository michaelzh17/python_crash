# -*- coding: utf-8 -*-

#file_name = 'text_files/pi_digits.txt'
file_name = 'text_files/pi_million_digits.txt'
with open(file_name) as file_object:
	#contents = file_object.read()
	#print(contents)
	lines = file_object.readlines()

#print(lines)	
#for line in lines:
	#print(line.rstrip())	

pi_string = ''
for line in lines:
	pi_string += line.strip()

#print(pi_string)
print(pi_string[:50] + "...")
print(len(pi_string))

my_btd = input("Enter your birthday date, in the format of mmddyy: ")

if my_btd in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else: 
	print("Your birthday does not appears in the first million digits of pi!")



