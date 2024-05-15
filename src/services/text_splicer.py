from repository.card import getCardImages
from PIL import Image


def line_processor(s):
    amount = 0
    name = ""
    set = ""
    for i, c in enumerate(s):
        if c == " ":
            print(s[:i])
            amount = int(s[:i])
            s = s[i:]
            break
    for i, c in enumerate(s):
        if c == "(":
            name = s[:i]
            s = s[i:]
            break
    for i, c in enumerate(s):
        if c == ")":
            set = s[:i]
            s = s[i:]
            break
    id = int(s[1:])
    name = name[1:-1]
    set = set[1:]
    return {'name': name, 'amount': amount, 'set': set, 'id': id}


def text_processor(text):
    lines = text.split('\n')
    data = [line_processor(line) for line in lines]
    return data
