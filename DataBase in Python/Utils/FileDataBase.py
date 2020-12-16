
books_filename = 'data.txt'

def add_book(name, author):
    with open(books_filename, 'a') as file:
        file.write(f'{name},{author},{"0"}\n')


def get_all_books():
    with open(books_filename,'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
        books = [{'name': line[0], 'author': line[1], 'read': line[2]} for line in lines]
        return books



def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = "1"
    __save_to_file(books)

def __save_to_file(books):
    str = ''
    with open(books_filename, 'w') as file:
        for book in books:
            str += f'{book["name"]},{book["author"]},{book["read"]}\n'
        file.write(str)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    __save_to_file(books)