import sqlite3

# conn = sqlite3.connect('my_database.db')
# cursor = conn.cursor()
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS users (
#
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT,
# age INTEGER
#
# )
# ''')
#
# cursor.execute("INSERT INTO users (name,age) VALUES ('Alice',25)")
# conn.commit()
# cursor.execute("SELECT*FROM users")
# print(cursor.fetchall())
# conn.close()

books_db = sqlite3.connect("my_store_books.db")
cursor = books_db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
author TEXT,
year  INTEGER,
price  INTEGER,
count  INTEGER
)
''')
books = [("Hamlet", 'William Shakespeare', 1623, 2100,5),
         ("Romeo and Juliet", 'William Shakespeare', 1587, 1000,70),
         ('The Tragedy of Macbeth', "William Shakespeare", 1623, 2130,4)]


#
# cursor.executemany('''
# INSERT INTO books (title, author, year, price, count )
# VALUES (?,?,?,?,?)
# ''',books)
# books_db.commit()

cursor.execute('''
SELECT * FROM books  ''')
print(cursor.fetchall())

books_db.close()