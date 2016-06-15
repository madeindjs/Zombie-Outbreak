#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

from classes.grid import Grid
from classes.human import Human


if __name__ == '__main__':
	grid = Grid()
	grid.add_humans(1)

	def turn():
		for area in grid.areas:
			for human in area.humans:
				human.move(grid)
			for zombie in area.zombies:
				zombie.move(grid)
		
		print(grid.view_map())

	while Human.total > 0 :
		turn()
		time.sleep(.5)

