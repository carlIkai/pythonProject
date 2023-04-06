import unittest
from ClassTestProject2 import MenuItem

class TestMenuItem(unittest.TestCase):

    def test_1(self):
        menu1 = MenuItem("Lime Ricky", 2.50, 3.50)
        self.assertEqual(menu1.get_name(), "Lime Ricky")

    def test_2(self):
        menu1 = MenuItem("Lime Ricky", 2.50, 3.50)
        self.assertAlmostEqual(menu1.get_wholesale_cost(), 2.50)

    def test_3(self):
        menu1 = MenuItem("Lime Ricky", 2.50, 3.50)
        self.assertAlmostEqual(menu1.get_selling_price(), 3.50)


