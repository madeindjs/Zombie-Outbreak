#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from classes.area import Area

class Grid():
	"""a 10*10 grid with population and zombay"""



	def __init__(self):
		self.areas = list()
		# build all areas [0,1],[1,1],[0,0], (....)
		for id in range(0,100):
			self.areas.append( Area(id) )



	def view_map(self):
		"""create a view map"""
		map_view = '_'*80
		# fetch all areas from `self.areas`
		for x in range(0,10):
			for y in range(0,10):
				map_view += '{}\t'.format(self.areas[x*10+y].status)
			map_view += "\r\n"
		map_view += '_'*80

		return map_view




	def _get_random_area(self):
		position = random.randint(0,len(self.areas))
		return self.find_area(position)




	def get_random_neighbour_area(self, area):
		"""return a new location """
		# return all moves possibles in array
		locations_possibles = [move+area for move in [-10,10,-1,1] if move+area >= 0 and move+area <= 100]
		# get a random movement
		new_area_id = random.choice(locations_possibles)
		return self.areas[new_area_id]




	def find_area(self, id):
		"""find an area with a id """
		return self.areas[id]




	def add_zombies(self, qty=1 ):
		"""add a zombies in a random area"""
		for i in range(0,qty):
			born_area = self._get_random_area()
			born_area.add_zombies()
			



	def add_humans(self, qty=1 ):
		"""add a humans in a random area"""
		for i in range(0,qty):
			born_area = self._get_random_area()
			born_area.add_humans()