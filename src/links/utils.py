import requests
from bs4 import BeautifulSoup
import json


def get_link_data(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    s = soup.find('script', type='application/ld+json')
    toJson = json.loads(s.string)

    price = toJson["offers"]["highPrice"]
    name = toJson["name"]
    image = toJson["image"]

    return name, price, image
