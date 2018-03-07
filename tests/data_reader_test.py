import unittest
import io
import sys

from data_reader import load_data


class TestDataReadMethods(unittest.TestCase):

    def test_correct_load(self):
        self.assertIsNotNone(load_data('sampleData.txt'))

    def test_empty_file(self):
        self.assertEqual(load_data('tests/empty.txt'), [])

    def test_non_existant_file(self):
        # Capture the test output for comparison.
        test_output = io.StringIO()
        sys.stdout = test_output

        self.assertEqual(load_data('fake.txt'), [])
        self.assertTrue(test_output.getvalue().startswith('The file was'))

        # Set stdout back to default.
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
