import sqlite3
from .database_connection import DataBaseConnection
from typing import List, Dict, Union, Type

book = Dict[str,Union[str, int]]

def create_data_table() -> None:
    with DataBaseConnection('data.db') as connection:
        cursor = connection.cursor()
        
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text, author text, read integer)')


def add_book(name: str, author: str) -> None:
    with DataBaseConnection('data.db') as connection:
        cursor = connection.cursor()
        
        cursor.execute(f'INSERT INTO books VALUES ( ?, ?, 0)', (name,author))


def get_all_books() -> List[book]:
    with DataBaseConnection('data.db') as connection:
        cursor = connection.cursor()
        
        cursor.execute(f'SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    return books


def mark_book_as_read(name: str) -> None:
    with DataBaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'UPDATE books SET read = 1 WHERE name = ?', (name,))


def delete_book(name: str) -> None:
    with DataBaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'DELETE FROM books WHERE name = ?', (name,))