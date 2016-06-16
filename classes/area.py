#!/usr/bin/python
# -*- coding: utf-8 -*-
from classes.zombie import Zombie
from classes.human import Human


class Area():
	"""an area is just a 1*1 square in a grid"""


	def __init__(self, id, grid):
		self.id = id
		self.grid = grid 



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
			return '|'

		elif len(list(self.humans)) < len(list(self.zombies)):
			return 'Z'

		else:
			return '{}.{}'.format(len(list(self.humans)), len(list(self.zombies)) )



	@property
	def humans(self):
		"""search in all Humans, who is in this area"""
		for human in Human.instances:
			try:
				if human.area.id == self.id:
					yield human 
			except AttributeError:
				pass




	@property
	def zombies(self):
		"""returns zombies in this area"""
		for zombie in Zombie.instances:
			try:
				if zombie.area.id == self.id:
					yield zombie 
			except AttributeError:
				pass


	def add_humans(self, qty=1):
		"""add humans on this area""" 
		for i in range(0, qty):
			Human(self)



	def add_zombies(self, qty=1):
		"""add zombies on this area""" 
		for i in range(0, qty):
			Zombie(self)


