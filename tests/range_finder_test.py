import unittest
import io
import sys

from range_finder import find_nearby_customers


class TestRangeFinder(unittest.TestCase):

    def test_output_is_correct(self):
        # Capture the test output for comparison.
        test_output = io.StringIO()
        sys.stdout = test_output

        find_nearby_customers("sampleData.txt")
        self.assertIsNotNone(test_output)
        number_of_customers = len(test_output.getvalue().split('\n'))
        # 16 customers + the blank line after printing.
        self.assertEqual(number_of_customers, 17)

        # Set stdout back to default.
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
