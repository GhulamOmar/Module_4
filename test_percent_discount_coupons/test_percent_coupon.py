import unittest

from percent_discount_coupons import percent_coupon
class MyTestCase(unittest.TestCase):
    def test_something(self):
       self.assertAlmostEquals(14.14458, percent_coupon.calculate_order(15.99))


if __name__ == '__main__':
    unittest.main()
