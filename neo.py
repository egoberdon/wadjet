"""Classes and functions that interact w/ Nasa's Near Earth Object API"""
from faker import Faker

from .system import System

NEO_API = "https://api.nasa.gov/neo/rest/v1/neo/browse"


class NEO:
	# instantiates the object of a near earth object
	# an object object if you will heh

	def __init__(self, neo_reference_id, designation, name, absolute_magnitude_h, estimated_diameter, is_potentially_hazardous_asteroid, is_sentry_object, **kwargs):

		# pre loading stuff

		self.system = System('metric')
		self.fake = Faker('es_MX')

		self.neo_id = neo_reference_id
		self.designation = designation
		self.name = name
		self.better_name = self.get_better_name()
		self.magnitude = absolute_magnitude_h
		self.diameter = self.system.ingest(estimated_diameter)
		self.sentry = is_sentry_object
		self.nerd_stuff = kwargs

		if is_potentially_hazardous_asteroid:
			self.friend_or_foe = '☄️ uh oh, this space fella might be a foe '
		else:
			self.friend_or_foe = '🌚 nice, this near earth object is a superb friend '

	def __repr__(self):

		return self.better_name

	def __str__(self):
		key = 'kilometers' if self.system.metric else 'miles'

		return f"""
			~ 💫 Hello my real name is {self.name} ~\n
			~ 🦄 But you can call me {self.better_name} ~ \n
			~ 🐛 My number is {self.neo_id} ~ \n
			~ 🐲 It has been said of me ~ \n
			~ ️{self.friend_or_foe} ~ \n
			~ ⛳ Check out some of my stats: ~ \n
			~ 📤 Max Diameter: {self.diameter[key]['estimated_diameter_max']} {key} ~ \n
			~ 📥 Min Diameter: {self.diameter[key]['estimated_diameter_min']} {key} ~ \n
		"""

	def get_better_name(self):
		first = self.fake.last_name()
		second = self.fake.city()
		return f'{first} {second} {len(second) - len(first)}'

	def list(self):
		return self.__str__().splitlines()
