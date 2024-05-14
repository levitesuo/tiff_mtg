import requests
import json


def getUrl(cardname, set_abriviation):
    def helper(char):
        if char == " ":
            return "+"
        return char
    search_term = ''.join([helper(char) for char in cardname])
    base_url = f'https://api.scryfall.com/cards/named?fuzzy={search_term}&set={set_abriviation.lower()}'
    return base_url


def getCardImage(cardname, set_abriviation):
    print(f"Getting data from: {getUrl(cardname, set_abriviation)}")
    response = requests.get(getUrl(cardname, set_abriviation))
    image_url = response.json()['image_uris']['png']
    print(f"Getting data from: {image_url}")
    response = requests.get(image_url)
    return response.content


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    response_data = getCardImage('Island', 'pip')
    image = mpimg.imread(response_data)
    plt.imshow(image)
    plt.show()
