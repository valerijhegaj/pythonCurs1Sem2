class Interaction:
	def read(self, path):
	    file = open(path, 'r')
	    data = file.read()
	    file.close()
	    return data

	def write(self, path, data):
	    file = open(path, 'w')
	    for i in data:
	        file.write(i)
	    file.close()
