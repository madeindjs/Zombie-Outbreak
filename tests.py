import unittest

from classes.grid import Grid
from classes.area import Area
from classes.human import Human
from classes.zombie import Zombie

class ZombieTest(unittest.TestCase):

	def test_number_zombies(self):
		old_count = Zombie.total
		qty_zombies = 5
		new_area = Area(1,Grid())
		new_area.add_zombies(qty_zombies)
		self.assertEqual(Zombie.total, old_count + qty_zombies)

	def test_number_humans_when_zombie_added(self):
		"""verify that number of human stay the same"""
		old_count = Human.total
		Area(1,Grid()).add_zombies(1)
		self.assertEqual(old_count, Human.total)

	def test_number_instances_of_humans_when_zombie_added(self):
		"""verify that number of human stay the same with instances porportie"""
		old_count = len(list(Human.instances))
		Zombie(Area(1,Grid()))
		self.assertEqual(old_count, len(list(Human.instances)))

	def test_move_function(self):
		"""check if the area before & after move is different"""
		birth_area = Area(1,Grid())
		zombie = Zombie(birth_area)
		zombie.move()
		self.assertNotEqual(birth_area.id, zombie.area.id)

	def test_zombie_die(self):
		"""check if when a zombie die is correctly removed from instances"""
		old_count = len(list(Zombie.instances))
		new_zombie = Zombie(Area(1,Grid()))
		new_zombie.die()
		self.assertEqual(old_count, len(list(Zombie.instances)))



class HumanTest(unittest.TestCase):

	def test_number_humans(self):
		old_count = Human.total
		qty_humans = 5
		new_area = Area(1,Grid())
		new_area.add_humans(qty_humans)
		self.assertEqual(Human.total, old_count + qty_humans)

	def test_number_zombies_when_human_added(self):
		"""verify that number of zombie stay the same"""
		old_count = Zombie.total
		Area(1,Grid()).add_humans(1)
		self.assertEqual(old_count, Zombie.total)

	def test_move_function(self):
		"""check if the area before & after move is different"""
		birth_area = Area(1,Grid())
		human = Human(birth_area)
		human.move()
		self.assertNotEqual(birth_area.id, human.area.id)

	def test_human_die(self):
		"""check if when a zombie die is correctly removed from instances"""
		old_count = len(list(Human.instances))
		new_human = Human(Area(1,Grid()))
		new_human.die()
		self.assertEqual(old_count, len(list(Human.instances)))

	def test_zombie_birth_when_human_die(self):
		"""check if when a zombie die, a new zombie birth"""
		old_count = len(list(Zombie.instances))
		new_human = Human(Area(1,Grid()))
		new_human.die()
		self.assertEqual(old_count+1	, len(list(Zombie.instances)))


class AreaTest(unittest.TestCase):

	def test_add_zombies(self):
		"""add a 5 zombie and count the total zombie in this area"""
		new_area = Area(1,Grid())
		new_area.add_zombies(5)
		self.assertEqual(len(list(new_area.zombies)) , 5)

	def test_count_zombies(self):
		"""add a 1 zombie and count the total zombie in this area"""
		new_area = Area(2,Grid())
		Zombie(new_area)
		self.assertEqual(len(list(new_area.zombies)) , 1)

	def test_number_zombies_when_human_added(self):
		"""verify that number of zombie stay the same in this area"""
		new_area = Area(3,Grid())
		old_count = len(list(new_area.zombies))
		Human(new_area)
		self.assertEqual(old_count, len(list(new_area.zombies)))



class GridTest(unittest.TestCase):

	def test_number_area(self):
		"""check the number of area"""
		grid = Grid()
		self.assertEqual(len(grid.areas), grid.size)

if __name__ == '__main__':
	unittest.main()