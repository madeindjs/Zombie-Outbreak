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




	def get_random_neighbour_area(self, area_id):
		"""return a new location """
		# return all moves possibles in array
		areas_ids_possibles = [ move+area_id for move in [-10,10,-1,1]]
		areas_ids_possibles = [ area_id for area_id in areas_ids_possibles if area_id >= 0 and area_id <= 100]
		# get a random movement
		area_id = random.choice(areas_ids_possibles)
		return self.areas[area_id]




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