import main
import unittest

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'String'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff4(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def test_do_stuff3(self):
        test_param = True
        result = main.do_stuff(test_param)
        self.assertEqual(result, 6)

if __name__=='__main__':
    unittest.main()
