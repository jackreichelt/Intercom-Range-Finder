import json
    
def loadData(filename):
    try:
        f = open(filename)
    except OSError as e:
        print('The file was unable to be opened due to a system error.')
        print(e)
        return [] #will result in no customers printed, exiting gracefully.
    customerData = [json.loads(line) for line in f]
    f.close()
    return customerData
