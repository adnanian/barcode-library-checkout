from sqlalchemy_serializer import (  # pyright: ignore[reportMissingImports]
    SerializerMixin,
)  # pyright: ignore[reportMissingImports]
from sqlalchemy.orm import validates  # pyright: ignore[reportMissingImports]
from config import db


class BookCopy(db.Model, SerializerMixin):
    """
    A book copy represents a specific instance of a book in the library.
    Each copy of a book is serialized individually to track its availability.
    """

    serialize_rules = ()

    __tablename__ = "book_copies"

    id = db.Column(db.Integer, primary_key=True)
    serial_no = db.Column(db.String, unique=True, nullable=False)
    added_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    last_updated = db.Column(db.DateTime, onupdate=db.func.now())
    # barcode = db.Column(db.String, unique=True, nullable=False)

    # Relationships

    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    book = db.relationship("Book", back_populates="book_copies")

    checkouts = db.relationship(
        "Checkout", back_populates="book_copy", cascade="all, delete-orphan", lazy=True
    )

    def __repr__(self):
        return "TO BE IMPLEMENTED"
