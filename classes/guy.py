#!/usr/bin/python
# -*- coding: utf-8 -*-


class Guy():
	"""a guy is a parent of a Zombie and a Human

	a guy have an specified area and he can move from nieghbour area"""

	total = 0
	


	def __init__(self, area):
		self.area = area
		self.__class__.total += 1 # increment number of instance of this object
		self.__class__.instances.append(self)




	def move(self):
		"""move this guy to a neighbourg area"""
		try:
			old_area = self.area.id
			grid = self.area.grid
			new_area = grid.get_random_neighbour_area(self.area)
			# new_area = grid._get_random_area()
			self.area = new_area
			# print('{} moved from {} to {}'.format(self, old_area, new_area))
		except AttributeError:
			# if something goes wrong, we kill it!!
			del(self)



