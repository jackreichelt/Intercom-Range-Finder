import unittest
from distanceCalculator import *

RADIUS = 6371 #assuming a spherical earth
OFFICE = {'latitude': 53.339428, 'longitude': -6.257664} #Intercom location

class TestDistanceMethods(unittest.TestCase):
    
    def test_samePosition(self):
        self.assertEqual(greatCircleDistance(OFFICE), 0)
        self.assertEqual(angleBetweenPoints(OFFICE, OFFICE), 0) #shouldn't pass if the previous failed
        
    def test_nearbyPosition(self):
        NEARBY = {'name': 'St Stevens Green', #The dead centre of St Stevens Green. approx 200m
                  'latitude': 53.338158,
                  'longitude': -6.259138} 
        self.assertLess(greatCircleDistance(NEARBY), .250)
        self.assertLess(angleBetweenPoints(OFFICE, NEARBY), .250) #shouldn't pass if the previous failed
    
    def test_distancePosition(self):
        NEARBY = {'name': 'My apartment', #My apartment in Sydney, approx 17,215 km
                  'latitude': -33.883449,
                  'longitude': 151.181398} 
        self.assertGreater(greatCircleDistance(NEARBY), 17200)
    
if __name__ == '__main__':
    unittest.main()
