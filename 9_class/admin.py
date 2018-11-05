# -*- coding: utf-8 -*-
from user import User

class Privileges():
	"""A simple attempt to model privileges user has"""

	def __init__(self):
		"""Initialize attributes to describe privileges"""
		self.privileges = ["can add post", "can delete post", "can ban user"]

	def show_privileges(self):
		"""Present the privileges an administrator has"""
		print("An administrator has following privileges: ")
		for item in self.privileges:
			print(item)

class Admin(User):
	"""Describe one kind of users: administrator."""

	def __init__(self, first_name, last_name, age, sex, city):
		"""Initialize an administrator user"""
		super().__init__(first_name, last_name, age, sex, city)
		self.privileges = Privileges()
