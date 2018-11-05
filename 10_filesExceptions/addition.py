# -*- coding: utf-8 -*-

print("Please give two numbers.")
print("Enter q to quit the program.")

while True:
	try:
		first_number = input("\nFirst number: ")
		if first_number == 'q':
			break
		second_number = input("Second number:")
		if second_number == 'q':
			break

		addition = int(first_number) + int(second_number)

	except ValueError:
		print("Part of your input is not integer. Please double check.")

	else:
		print(addition)

