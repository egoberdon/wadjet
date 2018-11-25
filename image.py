"""a file for working with the images nasa api"""

IMAGE_API = "https://images-api.nasa.gov/search"


class Image:

	def __init__(self, links, href, data, use_original=False):
		self.url = links[0]['href']

		if use_original:
			self.url = self.url.replace('thumb', 'orig')

		self.json_url = href
		data = data[0]
		self.nasa_id = data['nasa_id']
		self.date_created = data['date_created']
		self.keywords = data['keywords']
		self.title = data['title']
		self.description = data['description']
		self.center = data['center']

	def __repr__(self):
		return f'<NASA Image Object>'

	def __str__(self):
		return f'NASA Image: {self.nasa_id}'
