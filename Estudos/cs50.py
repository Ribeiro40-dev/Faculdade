'''words= set()

def check(words):
    return words.lower() in words

def load(dictionary):
    with open (dictionary) as file:
        words.update(file.read().splitlines())
    return True


def size():
    return len(words)

def unload():
    return True'''



answer = get_string("What's yor name?")
print("Hello ," + answer)

