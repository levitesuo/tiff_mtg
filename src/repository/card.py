import requests
import io
from PIL import Image


def strFormater(char):
    if char == " ":
        return "+"
    return char


def getCardUrl(card_data):
    base_url = f"https://api.scryfall.com/cards/{card_data['set'].lower()}/{card_data['id']}"
    return base_url


def getImage(url):
    response = requests.get(url, timeout=100)
    data = io.BytesIO(response.content)
    im = Image.open(data)
    return im


def getCardImages(card_data):
    response = requests.get(getCardUrl(
        card_data), timeout=100).json()
    images = []
    if 'card_faces' in response.keys():
        images.append(getImage(response['card_faces'][0]['image_uris']['png']))
        images.append(getImage(response['card_faces'][1]['image_uris']['png']))
        return images
    images.append(getImage(response['image_uris']['png']))
    return images


if __name__ == '__main__':
    card_list = [('Arlinn Kord', 'soi'), ('Island', 'pip')]
    print(getCardUrl({'set': 'neo', 'id': 295}))
    getCardImages({'set': 'neo', 'id': 295})[0].show()
