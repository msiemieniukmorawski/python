import unittest

from Day_12.unnecessary_math import multiply


# Moduł unittest jest wbudowanym w pythona modułem do testów.
# Każdy test powinen być zawarty w klasie dziedziczącej po unittest.TestCase.
# Dzięki temu możemy łączyć testy, oraz wykonywać pewne kawałki
# kodu przed (setUp) i po wykonaniu testu (tearDown).
class TestUM(unittest.TestCase):
    def setUp(self):
        self.a = 1
        print('na poczatku testów')

    def tearDown(self):
        print('Na końcu testów')

    def test_numbers_3_4(self):
        print('test_numbers_3_4')
        self.assertEqual(multiply(3, 4), 12)
        self.a = 7

    def test_numbers_3_4_with_fixture(self):
        print('test_numbers_3_4_with_fixture')
        self.assertEqual(multiply(3, self.a), 3)

    def test_numbers_not_equal(self):
        pass
        # print('test_numbers_not_equal')
        # self.assertNotEqual(multiply(3, 4), 16)

    def test_strings_a_3(self):
        print('test_strings_a_3')
        self.assertEqual(multiply('a', 3), 'aaa')


if __name__ == '__main__':
    unittest.main()