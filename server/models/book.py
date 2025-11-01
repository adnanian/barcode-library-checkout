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

    serialize_rules = (
        "-book_copies.checkouts",
        "-book_copies.book",
    )

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    isbn = db.Column(db.String, unique=True, nullable=False)

    # Relationships

    book_copies = db.relationship(
        "BookCopy", back_populates="book", cascade="all, delete-orphan", lazy=True
    )

    def __repr__(self):
        return "TO BE IMPLEMENTED"
