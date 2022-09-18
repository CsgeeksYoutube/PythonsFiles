import unittest
import pdbfunctionfile




class Tests(unittest.TestCase):
    
    def test_negative(self):
        
        self.assertFalse(pdbfunctionfile.palindrome(1234))

    def test_positive(self):
        
        self.assertTrue(pdbfunctionfile.palindrome(1234321))


if __name__ == '__main__':
    unittest.main()

