#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from classes.guy import Guy

class Zombie(Guy):
	"""a Zombie is a human infected herited from Guy"""
	instances = list()



	def attack(self, enemy):
		"""attack the enemy with a random choice. 

		* if True, this guy kill is enemy
		* if False, he die"""
		kill = random.choice([True, False])

		if kill:
			enemy.die()
		else:
			self.die()




	def die(self):
		"""when a Zombie die, he is remove from an instances"""
		try:
			self.__class__.total -= 1
			self.__class__.instances.remove(self)
		except ValueError:
			pass

		del(self)