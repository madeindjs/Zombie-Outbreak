#!/usr/bin/python
# -*- coding: utf-8 -*-

class Guy():
	"""a guy is a parent of a Zombie and a Human"""

	total = 0
	
	def __init__(self):
		# increment number of instance of this object
		self.__class__.total += 1
		print(self.__class__.total)

	def __del__(self):
		# increment number of instance of this object
		self.__class__.total -= 1