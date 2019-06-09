import unittest
from myapp import num_multiply


class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        arguments = [1, 2, 3]
        result = num_multiply(arguments)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()