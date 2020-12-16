from ..find import NotFoundError

def save_to_file(fileName, content):
    with open(fileName, 'w') as file:
        file.write(content)

def read_from_file(fileName):
    with open(fileName, 'r') as file:
        return file.readlines()


print(__name__)