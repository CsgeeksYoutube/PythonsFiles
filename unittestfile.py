import unittest
import funofunittest

class TestTheCode(unittest.TestCase):

    def setUp(self):
        self.filename ='textfile.txt'
        with open(self.filename,'r') as f:
            f.readlines()

    def test_function_runs(self):
        funofunittest.text(self.filename)

    def test_line_count(self):
        self.assertEqual(funofunittest.text(self.filename)[0], 10)

    def test_char_count(self):
        self.assertEqual(funofunittest.text(self.filename)[1],444)

if __name__=='__main__':
    unittest.main()