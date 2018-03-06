import dataReader
import distanceCalculator

TARGET_DISTANCE = 100

def findNearbyCustomers(filename):
    nearbyCustomers = {}

    for customer in dataReader.loadData(filename):
        if distanceCalculator.greatCircleDistance(customer) <= 100:
            nearbyCustomers[customer['user_id']] = customer['name']
    
    for customerId in sorted(nearbyCustomers):
        print(customerId, nearbyCustomers[customerId])
        
if __name__ == '__main__':
    findNearbyCustomers('sampleData.txt')