from flask import request  # pyright: ignore[reportMissingImports]
from flask_restful import Resource  # pyright: ignore[reportMissingImports]

from config import db, api
from models.book_copy import BookCopy


class BookCopyResource(Resource):

    def get(self):
        book_copies = [book_copy.to_dict() for book_copy in BookCopy.query.all()]
        return book_copies, 200

    def post(self):
        try:
            data = request.get_json()
            book_copy = BookCopy(
                serial_no=data["serial_no"],
                book_id=data["book_id"],
            )
            db.session.add(book_copy)
            db.session.commit()
            return book_copy.to_dict(), 201
        except Exception as e:
            return {"error": str(e)}, 422


class BookCopyResourceById(Resource):

    def get(self, id):
        book_copy = BookCopy.query.get_or_404(id)
        return book_copy.to_dict(), 200

    # NOT NEEDED, BUT COMMENTED JUST IN CASE
    # def patch(self, id):
    #     book_copy = BookCopy.query.get_or_404(id)
    #     data = request.get_json()

    #     try:
    #         for attr in data:
    #             value = data.get(attr)
    #             if getattr(book_copy, attr) != value:
    #                 setattr(book_copy, attr, value)
    #         db.session.add(book_copy)
    #         db.session.commit()
    #         return book_copy.to_dict(), 200
    #     except Exception as e:
    #         return {"error": str(e)}, 400

    def delete(self, id):
        book_copy = BookCopy.query.get_or_404(id)
        db.session.delete(book_copy)
        db.session.commit()
        return {}, 204


api.add_resource(BookCopyResource, "/api/book_copies")
api.add_resource(BookCopyResourceById, "/api/book_copies/<int:id>")
