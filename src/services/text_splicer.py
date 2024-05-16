def line_processor(s):
    amount = 0
    name = ""
    set = ""
    for i, c in enumerate(s):
        if c == " ":
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
    id = s[1:].strip()
    name = name[1:-1]
    set = set[1:]
    return {'name': name, 'amount': amount, 'set': set, 'id': id}


def text_processor(text):
    lines = text.split('\n')
    data = [line_processor(line) for line in lines][:-1]
    return data
