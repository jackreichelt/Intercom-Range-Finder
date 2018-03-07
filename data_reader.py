import json


def load_data(filename):
    try:
        f = open(filename)
    except OSError as e:
        print('The file was unable to be opened due to a system error.')
        print(e)
        return []  # Will result in no customers printed, exiting gracefully.
    customer_data = [json.loads(line) for line in f]
    f.close()
    return customer_data
