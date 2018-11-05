# -*- coding: utf-8 -*-


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nfirst number: ")
	if first_number.title() == 'Q':
		break
	second_number = input("second number: ")
	if second_number.title() == 'Q':
		break

	try:
		division = int(first_number)/int(second_number)

	except ZeroDivisionError:
		print("You can't divide by zero.")
	else:
		print(division)


try:
	print(5/3)
except ZeroDivisionError:
	print("You can't divide by zero!")