import unittest


def func():
    raise Exception('lets see if this works')


class ExampleTest(unittest.TestCase):
    # testowanie przechwycenia błędu musi odbywać się
    # za pomocą wyrażenia 'with'
    def test_error(self):
        with self.assertRaises(Exception):
            func()

    def test_nonsens(self):
        self.assertTrue(True)

    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(Exception, func)

if __name__ == '__main__':
    unittest.main()