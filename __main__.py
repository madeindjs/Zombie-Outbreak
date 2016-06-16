#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os

from classes.grid import Grid
from classes.human import Human
from classes.zombie import Zombie


if __name__ == '__main__':
	grid = Grid()
	grid.add_humans(5)
	grid.add_zombies(1)

	days = 0


	def turn():
		# clear terminal
		os.system('cls' if os.name == 'nt' else 'clear')

		# get all humans/zombies and move all them
		for human in Human.instances:
			human.move()

		for zombie in Zombie.instances:
			zombie.move()

		# check all areas and find what to do
		for area in grid.areas:

			# they fight if there are zombies & humans in area 
			if area.zombies !=0 and area.humans!=0:
				pass

			# a child born if there are at least two humans and no zombies
			if area.zombies == 0 and area.humans > 1:
				pass





	while Human.total > 0 :
		turn()
		days+=.25

		# display map and status
		print(grid.view_map())
		print("status:\t{} zombies and {} humans left".format(Zombie.total, Human.total))
		print("\t{} days spend".format(days))

		time.sleep(.1)

