import json

REQUIRED_KEYS = {'latitude', 'user_id', 'name', 'longitude'}


def load_data(filename):
    try:
        f = open(filename)
    except OSError as e:
        raise FileNotFoundError(f'The file {filename} cannot be opened.')

    customer_data = []

    for line in f:
        parsed_line = json.loads(line)
        if REQUIRED_KEYS.issubset(set(parsed_line)):
            customer_data.append(parsed_line)
        else:
            f.close()
            raise KeyError(f'The file {filename} has bad data.')

    f.close()
    return customer_data
