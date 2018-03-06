import unittest
from dataReader import *

class TestDataReadMethods(unittest.TestCase):
    
    def test_samePosition(self):
        self.assertIsNotNone(loadData('sampleData.txt'))
        
if __name__ == '__main__':
    unittest.main()
