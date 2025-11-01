from sqlalchemy_serializer import (  # pyright: ignore[reportMissingImports]
    SerializerMixin,
)  # pyright: ignore[reportMissingImports]
from sqlalchemy.orm import validates  # pyright: ignore[reportMissingImports]
from config import db


class Checkout(db.Model, SerializerMixin):
    """
    A checkout represents the action of a user borrowing a specific book copy from the library.
    It tracks which user has checked out which book copy and relevant timestamps.
    """

    serialize_rules = (
        "-user.checkouts",
        "-book_copy.checkouts",
    )

    __tablename__ = "checkouts"

    id = db.Column(db.Integer, primary_key=True)
    checkout_date = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime, nullable=True)
    last_updated = db.Column(db.DateTime, onupdate=db.func.now())

    # Relationships

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", back_populates="checkouts")

    book_copy_id = db.Column(
        db.Integer, db.ForeignKey("book_copies.id"), nullable=False
    )
    book_copy = db.relationship("BookCopy", back_populates="checkouts")

    def __repr__(self):
        return "TO BE IMPLEMENTED"
