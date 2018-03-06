import unittest
from distanceCalculator import *

RADIUS = 6371 #assuming a spherical earth
OFFICE = {'latitude': 53.339428, 'longitude': -6.257664} #Intercom location

class TestDistanceMethods(unittest.TestCase):
    
    def test_samePosition(self):
        self.assertEqual(angleBetweenPoints(OFFICE, OFFICE), 0)
        self.assertEqual(greatCircleDistance(OFFICE), 0) #shouldn't pass if the previous failed
        
    def test_nearbyPosition(self):
        NEARBY = {'name': 'St Stevens Green', #The dead centre of St Stevens Green. approx 200m
                  'latitude': 53.338158,
                  'longitude': -6.259138} 
        self.assertLess(greatCircleDistance(NEARBY), .250) #shouldn't pass if the previous failed
    
    def test_distantPosition(self):
        DISTANT = {'name': 'My apartment', #My apartment in Sydney, approx 17,215 km
                  'latitude': -33.883449,
                  'longitude': 151.181398} 
        self.assertGreater(greatCircleDistance(DISTANT), 17215)
        self.assertLess(greatCircleDistance(DISTANT), 17300)
        
    def test_zeroPosition(self):
        ZERO = {'latitude': 0, #0 lat and long, approx 5,959 km
                'longitude': 0}
        self.assertGreater(greatCircleDistance(ZERO), 5900)
        self.assertLess(greatCircleDistance(ZERO), 6000)
    
if __name__ == '__main__':
    unittest.main()
