import unittest

from distance_calculator import angle_between_points, great_circle_distance

RADIUS = 6371  # Assuming a spherical earth
OFFICE = {'latitude': 53.339428, 'longitude': -6.257664}  # Intercom location


class TestDistanceMethods(unittest.TestCase):

    def test_same_position(self):
        self.assertEqual(angle_between_points(OFFICE, OFFICE), 0)
        # Shouldn't pass if the previous failed.
        self.assertEqual(great_circle_distance(OFFICE), 0)

    def test_nearby_position(self):
        # The centre of St Stephen's Green. approx 200m.
        nearby = {
            'name': "St Stephen's Green",
            'latitude': '53.338158',
            'longitude': '-6.259138'
            }
        self.assertLess(great_circle_distance(nearby), .250)

    def test_distant_position(self):
        # My apartment in Sydney, approx 17,215 km.
        distant = {
            'name': 'My apartment',
            'latitude': '-33.883449',
            'longitude': '151.181398'
            }
        self.assertGreater(great_circle_distance(distant), 17215)
        self.assertLess(great_circle_distance(distant), 17300)

    def test_zero_position(self):
        # 0 lat and long, approx 5,959 km.
        zero = {
            'latitude': '0',
            'longitude': '0'
            }
        self.assertGreater(great_circle_distance(zero), 5900)
        self.assertLess(great_circle_distance(zero), 6000)


if __name__ == '__main__':
    unittest.main()
