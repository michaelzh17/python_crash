# -*- coding: utf-8 -*-

from city_functions import print_city_country
import unittest

class CityCountryTestCase(unittest.TestCase):
	"""Test city_functions.py"""

	def city_country_test(self):
		"""test city country as 'Beijing China' """
		city_country = print_city_country('beijing', 'china')
		self.assertequal(city_country, 'Beijing China')

unittest.main()
