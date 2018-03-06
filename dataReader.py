import json
    
def loadData(filename):
    f = open(filename)
    return [json.loads(line) for line in f]
