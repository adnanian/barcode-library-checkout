from sqlalchemy_serializer import (  # pyright: ignore[reportMissingImports]
    SerializerMixin,
)  # pyright: ignore[reportMissingImports]
from sqlalchemy.orm import validates  # pyright: ignore[reportMissingImports]
from config import db


class Book(db.Model, SerializerMixin):
    """
    A book signifies that at least one physical copy of a book exists in the library.
    Each book copy is represented by a BookCopy instance.
    This model holds bibliographic information about the book.
    """

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "TO BE IMPLEMENTED"
