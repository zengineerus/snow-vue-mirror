import unittest
from pizzeria.pizzeria import Pizzeria
from pizzeria.pizzeria import Size
from pizzeria.pizzeria import Topping


class TestPizzeria(unittest.TestCase):
    def test_small_pepperoni(self):
        self.assertEqual(Pizzeria().order(Size.SMALL, [Topping.PEPPERONI]), 12)

    def test_large_mushrooms(self):
        self.assertEqual(Pizzeria().order(Size.LARGE, [Topping.MUSHROOMS]), 21)

    def test_medium_olives(self):
        self.assertEqual(Pizzeria().order(Size.MEDIUM, [Topping.OLIVES]), 16)

    def test_small_pepperoni_and_sausage(self):
        self.assertEqual(Pizzeria().order(
            Size.SMALL, [Topping.SAUSAGE, Topping.PEPPERONI]), 14)

    def test_small_olive_and_mushroom(self):
        self.assertEqual(Pizzeria().order(
            Size.SMALL, [Topping.OLIVES, Topping.MUSHROOMS]), 12)

    def test_medium_olive_and_pepperoni(self):
        self.assertEqual(Pizzeria().order(
            Size.MEDIUM, [Topping.OLIVES, Topping.PEPPERONI]), 18)

    def test_large_sausage_and_pepperoni(self):
        self.assertEqual(Pizzeria().order(
            Size.LARGE, [Topping.PEPPERONI, Topping.SAUSAGE]), 24)


if __name__ == '__main__':
    unittest.main()
