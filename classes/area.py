#!/usr/bin/python
# -*- coding: utf-8 -*-
from classes.zombie import Zombie
from classes.human import Human


class Area():
	"""an area is just a 1*1 square in a grid"""


	def __init__(self, x, y):
		self.x , self.y = x, y
		self.humans = list()
		self.zombies = list()


	def __str__(self):
		return '<Area {}>'.format(self.position)

	@property
	def position(self):
		return '{}*{}'.format(self.x,self.y)

	@property
	def status(self):
		"""retrun `I` if this area have a majority of Human"""
		if len(self.humans) == 0 and len(self.zombies) == 0:
			return str()

		elif len(self.humans) > len(self.zombies):
			return 'H'

		elif len(self.humans) < len(self.zombies):
			return 'Z'


	def add_humans(self, qty=1):
		# add zombies
		for i in range(0, qty):
			self.humans.append(Human())
			print('1 guy inserted on {}'.format(self))

	def add_zombies(self, qty=1):
		# add zombies
		for i in range(0, qty):
			self.zombies.append(Zombie())
			print('1 zombie inserted on {}'.format(self))