import webbrowser

import requests
import click

from random import choice

from .credentials import API_KEY
from .neo import NEO, NEO_API
from .image import IMAGE_API, Image

KEY = {'api_key': API_KEY}
NUM = 12


def phone_home(url, params):

	communique = requests.get(url, params=params)
	response = communique.json()
	return response


def run_neo():

	neo_response = phone_home(NEO_API, KEY)
	neo_data = choice(neo_response['near_earth_objects'])
	neo = NEO(**neo_data)
	return neo


def print_neo():
	neo_response = phone_home(NEO_API, KEY)
	total_amount = neo_response['page']['total_elements']
	print(f'There are {total_amount} total near earth objects at this time')

	print('Let\'s look @ a random one')
	neo_data = choice(neo_response['near_earth_objects'])
	neo = NEO(**neo_data)
	print(neo)


def run_image(keyword):
	params = {'q': keyword, 'media_type': 'image'}
	image_response = phone_home(IMAGE_API, params=params)
	image_data = choice(image_response['collection']['items'])
	image = Image(**image_data)
	webbrowser.open(image.url)


@click.command()
@click.option('--mode', default='neo')
@click.option('--keyword', default='moon')
def cli(mode, keyword):
	if mode == 'neo':
		print_neo()

	elif mode == 'image':
		run_image(keyword)


if __name__ == '__main__':
	cli()
