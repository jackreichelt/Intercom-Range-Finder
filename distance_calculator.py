from math import acos, cos, sin, radians

RADIUS = 6371  # Assuming a spherical earth.
OFFICE = {'latitude': 53.339428, 'longitude': -6.257664}  # Intercom location


# Returns the angle between two points on the earth.
def angle_between_points(point_a, point_b):
    phi1 = radians(point_a['latitude'])
    phi2 = radians(float(point_b['latitude']))
    lam1 = radians(point_a['longitude'])
    lam2 = radians(float(point_b['longitude']))

    longitude_difference = abs(lam1 - lam2)

    return acos(sin(phi1) * sin(phi2)
                + cos(phi1) * cos(phi2) * cos(longitude_difference))


def great_circle_distance(target_point):
    return RADIUS * angle_between_points(OFFICE, target_point)
