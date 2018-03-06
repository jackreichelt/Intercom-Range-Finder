from math import acos, cos, sin, radians

RADIUS = 6371 #assuming a spherical earth
OFFICE = {'latitude': 53.339428, 'longitude': -6.257664} #Intercom location

# Returns the angle between two points on the earth
def angleBetweenPoints(pointA, pointB):
    phi1 = pointA['latitude']
    phi2 = float(pointB['latitude'])
    lam1 = pointA['longitude']
    lam2 = float(pointB['longitude'])
    
    longitudeDifference = abs(lam1 - lam2)
    
    return acos(sin(phi1) * sin(phi2) + cos(phi1) * cos(phi2) * cos(longitudeDifference))

def greatCircleDistance(targetPoint):
    return RADIUS * radians(angleBetweenPoints(OFFICE, targetPoint))
