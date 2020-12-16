# import Utils.InMemoryDataBase as database
# import Utils.FileDataBase as database
# import Utils.JSONFile as database
import Utils.DataBase as database



USR_CHOICE = """
Enter: 
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """

def menu() -> None:
    database.create_data_table()

    user_input = input(USR_CHOICE)

    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print(f'Invalid input!!!!')
        
        user_input = input(USR_CHOICE)

def prompt_add_book() -> None:
    name = input('Please enter book name: ')
    author = input('Please enter book author: ')

    database.add_book(name, author)


def list_books() -> None:
    books = database.get_all_books()
    print('\n')
    for book in books:
        read = 'read' if book['read'] else 'unread'
        print(f'{book["name"]} from {book["author"]} is {read}')


def prompt_read_book() -> None:
    name = input('Enter the name of the book you just finished reading: ')

    database.mark_book_as_read(name)


def prompt_delete_book() -> None:
    name = input('Enter the name of the book you want to delete: ')

    database.delete_book(name)

menu()