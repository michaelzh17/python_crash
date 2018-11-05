# -*- coding: utf-8 -*-

class Dog():
	"""A simple attempt to model a dog."""

	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command"""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")


my_dog = Dog("Doggy", 7)
your_dog = Dog("Lucy", 5)


print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's age is " + str(my_dog.age) + ".")

print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog's age is " + str(your_dog.age) + ".")

my_dog.sit()
my_dog.roll_over()

your_dog.sit()
