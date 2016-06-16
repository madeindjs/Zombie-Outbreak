#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os
import random

from classes.grid import Grid
from classes.human import Human
from classes.zombie import Zombie




def main():
	grid = Grid()
	grid.add_humans(10)
	grid.add_zombies(20)

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

			zombies = list(area.zombies)
			humans = list(area.humans)

			# they fight if there are zombies & humans in area 
			if len(zombies) !=0 and len(humans)!=0:
				for zombie in zombies:
					random_human = random.choice(humans)
					zombie.attack(random_human)


			# a child may born if there are at least two humans and no zombies
			if len(zombies) == 0 and len(humans) > 1:
				humans[0].have_sex()




	
	while Human.total > 0 :
		turn()
		days+=.25

		# display map and status
		print(grid.view_map())
		print("status:\t{} zombies and {} humans left".format(Zombie.total, Human.total))
		print("\t{} days spend".format(days))

		time.sleep(.5)



if __name__ == '__main__':
	main()