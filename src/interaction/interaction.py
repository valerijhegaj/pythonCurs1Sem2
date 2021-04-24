class interaction:
	def read(path):
	    file = open(path, 'r')
	    data = file.read()
	    file.close()
	    return data

	def write(path, data):
	    file = open(path, 'w')
	    for i in data:
	        file.write(i)
	    file.close()
