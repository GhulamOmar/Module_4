import unittest

from percent_discount_coupons import percent_coupon
class MyTestCase(unittest.TestCase):
    def test_something(self):
       self.assertAlmostEquals(17.12,percent_coupon.calculate_order(20))
       self.assertAlmostEquals(18.604, percent_coupon.calculate_order(22))
       self.assertAlmostEquals(24.54, percent_coupon.calculate_order(30))


if __name__ == '__main__':
    unittest.main()
