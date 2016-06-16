#!/usr/bin/python
# -*- coding: utf-8 -*-
from classes.guy import Guy
from classes.zombie import Zombie

class Human(Guy):
	"""a Human is a survivor herited from Guy"""
	instances = list()



	def die(self):
		"""when a Human die, 
		he is removed from an instances and a new zombie birth"""
		self.__class__.total -= 1
		self.__class__.instances.remove(self)
		Zombie(self.area)
		del(self)
