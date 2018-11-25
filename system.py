class System:
	# represents a measurement system
	# Metric or British

	def __init__(self, name):
		metric = name.lower() == 'metric'
		if not metric:
			british = name.lower() in ['british', 'imperial']
			if not british:
				print(f"{name} system not found, using metric")
				metric = True

		self.metric = metric

		if self.metric:
			self.valid = ['kilometers', 'meters']
		else:
			self.valid = ['miles', 'feet']

	def ingest(self, payload):
		# takes a dict and returns in valid system

		new_dict = {}

		for k, v in payload.items():

			if k in self.valid:

				new_dict[k] = v

		return new_dict
