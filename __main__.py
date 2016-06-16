#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os

from classes.grid import Grid
from classes.human import Human
from classes.zombie import Zombie


if __name__ == '__main__':
	grid = Grid()
	grid.add_humans(1)

	def turn():
		# clear terminal
		os.system('cls' if os.name == 'nt' else 'clear')

		# get all areas and move all guys in theses areas
		for human in Human.instances:
			human.move()
			
		for zombie in Zombie.instances:
			zombie.move()


		# display map and status
		print(grid.view_map())
		print('status: {} zombies and {} humans left'.format(Zombie.total, Human.total))



	while Human.total > 0 :
		turn()
		time.sleep(1)

