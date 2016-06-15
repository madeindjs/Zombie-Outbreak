import unittest

from classes.area import Area

class AreaTest(unittest.TestCase):

	def test_check_add_zombies(self):
		"""add a 10 zombie and count the total zombie in this area"""
		area = Area(1,1)
		area.add_zombies(5)
		self.assertEqual(len(area.zombies), 5)

if __name__ == '__main__':
	unittest.main()