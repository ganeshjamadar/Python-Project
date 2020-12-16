import json

books_filename = 'data.json'

def create_data_table():
    with open(books_filename, 'w') as file:
        json.dump([], file)


def add_book(name, author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    __save_to_file(books)

def get_all_books():
    with open(books_filename,'r') as file:
        return json.load(file)


def __save_to_file(books):
    with open(books_filename, 'w') as file:
        json.dump(books, file)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    __save_to_file(books)




def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    __save_to_file(books)