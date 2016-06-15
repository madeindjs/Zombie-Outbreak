#!/usr/bin/python
# -*- coding: utf-8 -*-

class Area():
	"""an area is just a 1*1 square in a grid"""


	def __init__(self, x, y):

		self.name = '{}*{}'.format(x,y)

		self.humans = 0
		self.zombies = 0

		print(self)



	def __str__(self):
		return '<Area {}>'.format(self.name)
