#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from classes.guy import Guy
from classes.zombie import Zombie

class Human(Guy):
	"""a Human is a survivor herited from Guy"""
	instances = list()



	def have_sex(self):
		"""Have a sex with another human. 

		* if True, a new human birth"""
		baby = random.choice([True, False, False])
		if baby:
			Human(self.area)



	def die(self):
		"""when a Human die, 
		he is removed from an instances and a new zombie birth"""
		try:
			self.__class__.total -= 1
			self.__class__.instances.remove(self)
		except ValueError:
			pass
		Zombie(self.area)
		del(self)
