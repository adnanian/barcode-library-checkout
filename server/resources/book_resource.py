from flask import request  # pyright: ignore[reportMissingImports]
from flask_restful import Resource  # pyright: ignore[reportMissingImports]

from config import db, api
from models.book import Book


class BookResource(Resource):

    def get(self):
        books = [book.to_dict() for book in Book.query.all()]
        return books, 200

    def post(self):
        try:
            data = request.get_json()
            book = Book(
                title=data["title"],
                author=data["author"],
                year=data["year"],
                isbn=data["isbn"],
            )
            db.session.add(book)
            db.session.commit()
            return book.to_dict(), 201
        except Exception as e:
            return {"error": str(e)}, 422


class BookResourceById(Resource):

    def get(self, id):
        book = Book.query.get_or_404(id)
        return book.to_dict(), 200

    def patch(self, id):
        book = Book.query.get_or_404(id)
        data = request.get_json()

        try:
            data = request.get_json()
            for attr in data:
                value = data.get(attr)
                if getattr(book, attr) != value:
                    setattr(book, attr, value)
            db.session.add(book)
            db.session.commit()
            return book.to_dict(), 200
        except Exception as e:
            return {"error": str(e)}, 400

    def delete(self, id):
        book = Book.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        return {}, 204


api.add_resource(BookResource, "/api/books")
api.add_resource(BookResourceById, "/api/books/<int:id>")
