import unittest

from data_reader import load_data


class TestDataReadMethods(unittest.TestCase):

    def test_correct_load(self):
        loadedData = load_data('sampleData.txt')
        self.assertIsNotNone(loadedData)
        self.assertGreater(len(loadedData), 0)

    def test_bad_json(self):
        self.assertRaises(KeyError, load_data, 'tests/badJson.txt')

    def test_empty_file(self):
        self.assertEqual(load_data('tests/empty.txt'), [])

    def test_non_existant_file(self):
        self.assertRaises(FileNotFoundError, load_data, 'fake.txt')


if __name__ == '__main__':
    unittest.main()
