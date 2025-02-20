from flask import request, jsonify
from models import get_all_books, get_book_by_id, create_book, update_book, delete_book

def routes(app):
    @app.route('/books', methods=['GET'])
    def all():
        books = get_all_books()
        return jsonify([dict(book) for book in books])

    @app.route('/books', methods=['POST'])
    def create():
        data = request.json
        book = create_book(data)
        return jsonify(dict(book))

    @app.route('/books/<int:id>', methods=['GET'])
    def show(id):
        book = get_book_by_id(id)
        if book is None:
            return jsonify({'error': 'Book not found'}), 404
        return jsonify(dict(book))

    @app.route('/books/<int:id>', methods=['PUT'])
    def update(id):
        data = request.json
        book = get_book_by_id(id)
        if book is None:
            return jsonify({'error': 'Book not found'}), 404
        updated_book = update_book(id, data)
        return jsonify(dict(updated_book))

    @app.route('/books/<int:id>', methods=['DELETE'])
    def delete(id):
        book = get_book_by_id(id)
        if book is None:
            return jsonify({'error': 'Book not found'}), 404
        delete_book(id)
        return jsonify(dict(book))