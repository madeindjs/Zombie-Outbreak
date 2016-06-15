import unittest

from classes.grid import Grid
from classes.area import Area
from classes.human import Human
from classes.zombie import Zombie

class ZombieTest(unittest.TestCase):

	def test_number_zombies(self):
		old_count = Zombie.total
		qty_zombies = 5
		new_area = Area(1)
		new_area.add_zombies(qty_zombies)
		self.assertEqual(Zombie.total, old_count + qty_zombies)

	def test_number_humans_when_zombie_added(self):
		"""verify that number of human stay the same"""
		old_count = Human.total
		Area(1).add_zombies(1)
		self.assertEqual(old_count, Human.total)


class HumanTest(unittest.TestCase):

	def test_number_humans(self):
		old_count = Human.total
		qty_humans = 5
		new_area = Area(1)
		new_area.add_humans(qty_humans)
		self.assertEqual(Human.total, old_count + qty_humans)

	def test_number_zombies_when_human_added(self):
		"""verify that number of zombie stay the same"""
		old_count = Zombie.total
		Area(1).add_humans(1)
		self.assertEqual(old_count, Zombie.total)


class AreaTest(unittest.TestCase):

	def test_add_zombies(self):
		"""add a 5 zombie and count the total zombie in this area"""
		new_area = Area(1)
		new_area.add_zombies(5)
		self.assertEqual(len(list(new_area.zombies)) , 5)



class GridTest(unittest.TestCase):

	def test_number_area(self):
		"""check the number of area"""
		self.assertEqual(len(Grid().areas), 100)

if __name__ == '__main__':
	unittest.main()