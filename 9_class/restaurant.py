# -*- coding: utf-8 -*-

class Restaurant():
	"""A restaurant class"""
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize attributes to describe a restaurant."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 10

	def describe_restaurant(self):
		"""Print out restaurant_name and cuisine_type"""
		print("My restaurant name is " + self.restaurant_name + ", the cuisine type is " 
			+ self.cuisine_type)

	def open_restaurant(self):
		"""Indicate that the restaurant is open"""
		print("My restaurant " + self.restaurant_name + " is open.")

	def set_number_served(self, number):
		"""Set number of customers served"""
		self.number_served = number
	def increment_number_served(self, number_add):
		"""Add the given number of customers to number of served customers in a daily base"""
		self.number_served += number_add

class IceCreamStand(Restaurant):
	"""Represent ice cream stand, a special kind of resaurant"""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize ice cream stand class"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['vanila', 'strawberry', 'stone']

	def describe_flavor(self):
		"""Present the flavors of the ice cream stand"""
		print("We have " + str(len(self.flavors)) + " flavors of ice cream to choose from:")
		for item in self.flavors:
			print(item)


my_icecream = IceCreamStand("Summer", "Italian")

my_icecream.describe_flavor()




my_restaurant = Restaurant("Stella", "Cajun")
print("The name of my restaurant is " + my_restaurant.restaurant_name)
print("The type of my cuisine is " + my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

new_restaurant = Restaurant("Lily Pizza", "Italian")
print("We have served " + str(new_restaurant.number_served) + " customers.")

new_restaurant.set_number_served(20)
print("Customers served " + str(new_restaurant.number_served))

new_restaurant.increment_number_served(5)
print("customers served " + str(new_restaurant.number_served))






