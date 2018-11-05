# -*- coding: utf-8 -*-

from random import randint

class Die():
	"""Describe a die."""
	def __init__(self, sides = 6):
		"""Initialize the die."""
		self.sides = sides

	def roll_die(self):
		"""The method to print out a random number between 1 and the number of sides the die has"""
		print(str(randint(1, self.sides)))


new_die = Die(20)

for i in range(0,10):
	new_die.roll_die()


