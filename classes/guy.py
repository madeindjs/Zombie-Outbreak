#!/usr/bin/python
# -*- coding: utf-8 -*-
import random


class Guy():
	"""a guy is a parent of a Zombie and a Human"""

	total = 0
	


	def __init__(self, area_id):
		self.area_id = area_id
		self.__class__.total += 1 # increment number of instance of this object



	def __del__(self):
		# increment number of instance of this object
		self.__class__.total -= 1




	def move(self, grid):
		# add it to the new area_id
		new_area = grid.get_random_neighbour_area(self.area_id)
		new_area.guys.append(self)
		# remove it from the old area
		old_area = grid.find_area(self.area_id)
		old_area.guys.remove(self)
		self.area_id = new_area.id
		# print('{} moved from {} to {}'.format(self, old_area, new_area))


