# -*- coding: utf-8 -*-

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jessi'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['john'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + ".")

