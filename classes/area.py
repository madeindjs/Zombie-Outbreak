#!/usr/bin/python
# -*- coding: utf-8 -*-
from classes.zombie import Zombie
from classes.human import Human


class Area():
	"""an area is just a 1*1 square in a grid"""


	def __init__(self, id):
		self.id = id
		self.guys = list()


	def __str__(self):
		return '<Area {}>'.format(self.id)



	@property
	def status(self):
		"""Return the status of the area:

		- ` ` : empty
		- `Z` : this area have a majority of Zombies
		- `H` : this area have a majority of Humans """
		if len(list(self.humans)) == 0 and len(list(self.zombies)) == 0:
			return ' '

		elif len(list(self.humans)) > len(list(self.zombies)):
			return 'O'

		elif len(list(self.humans)) < len(list(self.zombies)):
			return 'Z'



	@property
	def humans(self):
		"""returns humans in this area"""
		for guy in self.guys:
			if isinstance(guy,Human):
				yield guy 
		# yield [guy for guy in self.guys if isinstance(guy,Human)]
	


	@property
	def zombies(self):
		"""returns zombies in this area"""
		for guy in self.guys:
			if isinstance(guy,Zombie):
				yield guy 
		# yield [guy for guy in self.guys if isinstance(guy,Zombie)]


	def add_humans(self, qty=1):
		"""add humans on this area""" 
		for i in range(0, qty):
			self.guys.append(Human(self.id))



	def add_zombies(self, qty=1):
		"""add zombies on this area""" 
		for i in range(0, qty):
			self.guys.append(Zombie(self.id))


