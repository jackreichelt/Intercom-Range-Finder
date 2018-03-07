import unittest
from dataReader import *

class TestDataReadMethods(unittest.TestCase):

    def test_correctLoad(self):
        self.assertIsNotNone(loadData('sampleData.txt'))

    def test_emptyFile(self):
        self.assertEqual(loadData('tests/empty.txt'), [])

    def test_nonExistantFile(self):
        self.assertEqual(loadData('fake.txt'), [])

if __name__ == '__main__':
    unittest.main()
