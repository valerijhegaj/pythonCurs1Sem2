class RSS:
	def count(referenceValues, receivedValues):
		RSS = 0;
		for i in range(len(receivedValues)):
			RSS += (receivedValues[i] - referenceValues[i]) ** 2
		return RSS
