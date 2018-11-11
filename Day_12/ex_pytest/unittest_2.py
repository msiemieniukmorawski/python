import unittest
from Day_12.ex_pytest.unnecessary_math import multiply


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_strings_a_3(self):
        self.assertEqual(multiply('a', 3), 'aaa')

    def test_strings_3_5(self):
        self.assertNotEqual(multiply(3, 4), 15)


if __name__ == '__main__':
    unittest.main()