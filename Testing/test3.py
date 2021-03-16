# Test file for script3.py

import unittest
import script2


class TestMain(unittest.TestCase):
    def setUp(self):
        print('Hello')
    def test_random_guess(self):
        guess = 5
        answer =5
        result = script2.randg(guess, answer)
        self.assertTrue(result)

    def test_random_guess2(self):
        result = script2.randg(5, 0)
        self.assertFalse(result)

    def test_random_guess3(self):
        result = script2.randg(5, '0')
        self.assertFalse(result)


if __name__=='__main__':
    unittest.main()
