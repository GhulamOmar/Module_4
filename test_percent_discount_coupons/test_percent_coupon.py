"""
Program: test_percent_coupon.py
Author: Ghulam Omar
Last date modified: 09/17/19

this program is a test file for percent_coupon.py.
"""
import unittest
from percent_discount_coupons import percent_coupon


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertAlmostEqual(17.12, percent_coupon.calculate_order(20))  # first test
        self.assertAlmostEquals(23.798, percent_coupon.calculate_order(29))  # second test
        self.assertAlmostEquals(24.54, percent_coupon.calculate_order(30))  # third test
        self.assertAlmostEquals(46.80, percent_coupon.calculate_order(60))  # fourth test


if __name__ == '__main__':
    unittest.main()
