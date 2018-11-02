import requests

from credentials import API_KEY



# hardcoding to near earth orbit stuff api for now
HOUSTON = "https://api.nasa.gov/neo/rest/v1/neo/browse/"
KEY = {'api_key': API_KEY}
communique = requests.get(HOUSTON, data=KEY)
import pdb; pdb.set_trace()