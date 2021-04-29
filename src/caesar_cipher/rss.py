class RSS:
	def count(reference_values, received_values):
		RSS = 0
		for i in range(len(received_values)):
			RSS += (received_values[i] - reference_values[i]) ** 2
		return RSS
