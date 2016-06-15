#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from classes.area import Area

class Grid():
	"""a 10*10 grid with population and zombay"""
	def __init__(self):
		self.areas = list()
		# build all areas [0,1],[1,1],[0,0], (....)
		for x in range(0,10):
			for y in range(0,10):
				self.areas.append( Area(x,y) )



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


	def add_zombies(self, qty=1 ):
		"""add a zombies in a random area"""
		for i in range(0,qty):
			position = random.randint(0,len(self.areas))
			born_area = self.areas[position]
			born_area.add_zombies()
			

