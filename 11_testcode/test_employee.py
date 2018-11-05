# -*- coding: utf-8 -*-

import unittest
from employee import Employee 

class Test_Employee_Function(unittest.TestCase):
	"""Test employee.py"""

	def setUp(self):
		"""set up employee instance test data"""
		self.new_employee = Employee('Lily',' Stone', 500)
		#self.new_employee.give_raise()
		#print(self.new_employee.salary)

	def test_give_default_raise(self):
		"""test default raise"""
		self.new_employee.give_raise()

		self.assertEqual(5500, self.new_employee.salary)

	def test_give_custom_raise(self):
		"""Test give custom raise case"""
		self.new_employee.give_raise(1000)
		self.assertEqual(1500, self.new_employee.salary)

unittest.main()