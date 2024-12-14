from flask import Flask, jsonify, request
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)


books = [
    {"id": 1, "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"id": 2, "title": "Wings of fire", "author": "Dr.APJ Abdul Kalam"}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    new_book['id'] = max([b['id'] for b in books] + [0]) + 1
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        book.update(request.json)
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({"message": "Book deleted"})

if __name__ == '__main__':
    app.run(debug=True)

                                                                                                                                                                                                                                                                                   