#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from classes.area import Area

class Grid():
	"""a 10*10 grid with population and zombay"""

	width = 80
	height = 10



	def __init__(self):
		self.areas = list()
		# build all areas [0,1],[1,1],[0,0], (....)
		self.number_areas = self.width * self.height
		for id in range(0,self.number_areas):
			self.areas.append( Area(id) )



	def view_map(self):
		"""create a view map"""
		map_view = '_'*self.width
		# fetch all areas from `self.areas`
		for x in range(0,self.height):
			for y in range(0,self.width):
				area_id = x*self.width+y
				map_view += '{}'.format(self.areas[area_id].status)
			map_view += "\r\n"
		map_view += '_'*self.width

		return map_view




	def _get_random_area(self):
		position = random.randint(0,len(self.areas))
		return self.find_area(position)




	def get_random_neighbour_area(self, area_id=50):
		"""return a new location """
		try:
			# return all moves possibles in array
			moves_possible = [self.width*-1,self.width,-1,1]
			moves_result = [ move+area_id for move in moves_possible]
			areas_ids_possibles = [ result for result in moves_result if result >= 0 and result <= self.number_areas]
			# get a random movement
			area_id = random.choice(areas_ids_possibles)
			return self.areas[area_id]
		except IndexError:
			self._get_random_area()





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