import unittest

from percent_discount_coupons import percent_coupon
class MyTestCase(unittest.TestCase):
    def test_something(self):
       self.assertAlmostEquals(19,percent_coupon.calculate_order(23))


if __name__ == '__main__':
    unittest.main()
