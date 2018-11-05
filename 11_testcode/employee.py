# -*- coding: utf-8 -*-

class Employee():
	"""Represent an employee"""

	def __init__(self, f_name, l_name, salary):
		"""Initialize attributes to represent an employee"""

		self.f_name = f_name
		self.l_name = l_name
		self.salary = salary

	def give_raise(self, add_raise = 5000):
		"""Give raise to an employee's salary"""
		
		self.salary += add_raise

	



