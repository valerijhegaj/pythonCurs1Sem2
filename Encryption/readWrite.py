def read(way):
    file = open(way, 'r')
    data = file.read()
    file.close()
    return data

def write(way, data):
    file = open(way, 'w')
    for i in data:
        file.write(i)
    file.close()
