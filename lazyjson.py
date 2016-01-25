from json import loads

def load(file):
    buffer = ""
    for line in file:
        buffer += line
        try:
            yield loads(buffer)
            buffer = ""
        except ValueError:
            pass
