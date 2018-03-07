import data_reader
import distance_calculator

TARGET_DIST = 100


def find_nearby_customers(filename):
    nearby_customers = {}

    for customer in data_reader.load_data(filename):
        if distance_calculator.great_circle_distance(customer) <= TARGET_DIST:
            nearby_customers[customer['user_id']] = customer['name']

    for customer_id in sorted(nearby_customers):
        print(customer_id, nearby_customers[customer_id])


if __name__ == '__main__':
    find_nearby_customers('sampleData.txt')
