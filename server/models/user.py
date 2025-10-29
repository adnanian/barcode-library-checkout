from sqlalchemy_serializer import (  # pyright: ignore[reportMissingImports]
    SerializerMixin,
)  # pyright: ignore[reportMissingImports]
from sqlalchemy.orm import validates  # pyright: ignore[reportMissingImports]
from config import db, bcrypt


class User(db.Model, SerializerMixin):
    """
    Person that is physically using the Barcode Library Scanner.
    A user can check out books and return them.
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    last_updated = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return "TO BE IMPLEMENTED"
