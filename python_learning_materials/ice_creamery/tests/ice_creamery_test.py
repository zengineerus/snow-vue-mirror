import unittest
from ice_creamery.ice_creamery import IceCreamery


class TestIceCreamery(unittest.TestCase):
    def test_order_TwoScoops_TwoToppings(self):
        self.assertEqual(IceCreamery().order(2, ['hot fudge', 'sprinkles']), 5)

    def test_order_ThreeScoops_TwoToppings(self):
        self.assertEqual(IceCreamery().order(3, ['hot fudge', 'sprinkles']), 6)

    def test_order_OneScoop_NoToppings(self):
        self.assertEqual(IceCreamery().order(1, []), 3)

    def test_order_OneScoop_OneTopping(self):
        self.assertEqual(IceCreamery().order(1, ['hot fudge']), 3.50)


if __name__ == '__main__':
    unittest.main()
