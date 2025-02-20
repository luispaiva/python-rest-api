from database import db_connection

def get_all_books():
    conn = db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return books

def get_book_by_id(book_id):
    conn = db_connection()
    book = conn.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
    conn.close()
    return book

def create_book(data):
    conn = db_connection()
    result = conn.execute('INSERT INTO books (title, author, description) VALUES (?, ?, ?)', (data['title'], data['author'], data['description']))
    book = conn.execute('SELECT * FROM books WHERE id = ?', (result.lastrowid,)).fetchone()
    conn.commit()
    conn.close()
    return book

def update_book(book_id, data):
    conn = db_connection()
    conn.execute('UPDATE books SET title = ?, author = ?, description = ? WHERE id = ?', (data['title'], data['author'], data['description'], book_id))
    conn.commit()
    book = conn.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
    conn.close()
    return book

def delete_book(book_id):
    conn = db_connection()
    book = conn.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
    if book:
        conn.execute('DELETE FROM books WHERE id = ?', (book_id,))
        conn.commit()
    conn.close()
    return book