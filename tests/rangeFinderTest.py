import unittest
import io
import sys
from rangeFinder import *

class TestRangeFinder(unittest.TestCase):

    def test_outputIsCorrect(self):
        # Capture the test output for comparison
        testOutput = io.StringIO()
        sys.stdout = testOutput

        findNearbyCustomers("sampleData.txt")
        self.assertIsNotNone(testOutput)
        numberOfCustomers = len(testOutput.getvalue().split('\n'))
        self.assertEqual(numberOfCustomers, 17) #16 customers + the blank line after printing

        # set stdout back to default
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
