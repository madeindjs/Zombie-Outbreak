#!/usr/bin/python
# -*- coding: utf-8 -*-

from classes.grid import Grid


if __name__ == '__main__':
	grid = Grid()
	grid.add_zombies(20)
	print(grid.view_map())

