# -*- coding: utf-8 -*-

guest_name = input("Please type your name here: ")

with open('GuestName.txt', 'a') as file_object:
	file_object.write(guest_name)
	file_object.write("\n")

while True:
	guest = input("Please input your name here: ")
	print("Welcome " + guest.title() + "!")

	with open('guest_book.txt', 'a') as file_object:
		file_object.write(guest)
		file_object.write("\n")

