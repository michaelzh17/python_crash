# -*- coding: utf-8 -*-

import json

numbers = [3, 7, 5, 8, 0]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)

