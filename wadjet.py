import requests

from faker import Faker
from random import choice
from credentials import API_KEY

# hardcoding to near earth orbit stuff api for now
HOUSTON = "https://api.nasa.gov/neo/rest/v1/neo/browse"
KEY = {'api_key': API_KEY}
NUM = 12


def phone_home():

	communique = requests.get(HOUSTON, params=KEY)
	neo_data = communique.json()
	return neo_data


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


def main():
	neo_data = phone_home()
	total_amount = neo_data['page']['total_elements']
	print(f'There are {total_amount} total near earth objects at this time')
	print(f'Lets check out {NUM} of them')
	neos = []

	counter = 0

	for neo in neo_data['near_earth_objects']:
		neos.append(NEO(**neo))
		counter += 1
		if counter > NUM:
			break

	print('Digging further let\'s look @ a random one')
	print(choice(neos))


main()
