# -*- coding: utf-8 -*-

class User():
	"""Describe a general user"""

	def __init__(self, first_name, last_name, age, sex, city):
		"""Initialize attributes to describe a car."""

		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.sex = sex
		self.city = city
		self.login_attempts = 0

	def describe_user(self):
		"""Print out a summary of the user's information"""
		print("This user's name is " + self.first_name + " " + self.last_name + ", at the" +
			" age of " + str(self.age) + " with sex of " + self.sex + " living at " + self.city + ".")


	def greet_user(self):
		"""To greet the user"""
		print("Congratulations! " + self.first_name + ". Welcome to the community!" )

	def increment_login_attempts(self):
		"""Increments the value of login_attempts by 1"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Reset login_attempts value to 0"""
		self.login_attempts = 0















