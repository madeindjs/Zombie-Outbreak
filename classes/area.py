#!/usr/bin/python
# -*- coding: utf-8 -*-

class Area():
	"""an area is just a 1*1 square in a grid"""


	def __init__(self, x, y):
		self.x , self.y = x, y
		self.humans = 0
		self.zombies = 0


	def __str__(self):
		return '<Area {}>'.format(self.position)

	@property
	def position(self):
		return '{}*{}'.format(self.x,self.y)

	@property
	def status(self):
		return '{}/{}'.format(self.humans,self.zombies)
