from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)

@app.route('/api/books', methods=['GET'])
def get_all_books():
    try:
        books = Book.query.all()
        book_list = [{'title': book.title, 'author': book.author, 'genre': book.genre} for book in books]
        return jsonify(book_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/books', methods=['POST'])
def add_new_book():
    data = request.get_json()
    if not data or 'title' not in data or 'author' not in data or 'genre' not in data:
        return jsonify({'error': 'Invalid request payload'}), 400

    try:
        new_book = Book(title=data['title'], author=data['author'], genre=data['genre'])
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'message': 'Book added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book_details(book_id):
    data = request.get_json()
    if not data or 'title' not in data or 'author' not in data or 'genre' not in data:
        return jsonify({'error': 'Invalid request payload'}), 400

    try:
        book = Book.query.get(book_id)
        if not book:
            return jsonify({'error': 'Book not found'}), 404

        book.title = data['title']
        book.author = data['author']
        book.genre = data['genre']
        db.session.commit()

        return jsonify({'message': 'Book details updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
