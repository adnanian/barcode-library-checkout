from sqlalchemy.ext.hybrid import (  # pyright: ignore[reportMissingImports]
    hybrid_property,
)  # pyright: ignore[reportMissingImports]
from sqlalchemy_serializer import (  # pyright: ignore[reportMissingImports]
    SerializerMixin,
)  # pyright: ignore[reportMissingImports]
from sqlalchemy.ext.associationproxy import (  # pyright: ignore[reportMissingImports]
    association_proxy,
)  # pyright: ignore[reportMissingImports]
from sqlalchemy.orm import validates  # pyright: ignore[reportMissingImports]
from config import db, bcrypt
from models.checkout import Checkout


class User(db.Model, SerializerMixin):
    """
    Person that is physically using the Barcode Library Scanner.
    A user can check out books and return them.
    """

    serialize_rules = (
        "-checkouts.user",
        "-checkouts.book_copy.checkouts",
        "-book_copies.checkouts",
        "-_password_hash",
    )

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    last_updated = db.Column(db.DateTime, onupdate=db.func.now())

    # Relationships

    checkouts = db.relationship(
        "Checkout", back_populates="user", cascade="all, delete-orphan", lazy=True
    )

    # Association Proxies

    book_copies = association_proxy(
        "checkouts", "book_copy", creator=lambda bc: Checkout(book_copy=bc)
    )

    @hybrid_property
    def password_hash(self):
        """Restriction for user. Prevents user from accessing password hash.

        Raises:
            AttributeError: if an attempt to access the password hash has been made.
        """
        raise AttributeError("Password hash cannot be viewed.")

    @password_hash.setter
    def password_hash(self, password):
        """Sets a new password for user and rehashes it.

        Args:
            password (str): the new password.
        """
        # print("Setting new password", flush=True)
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")
        # print("Password set successful!", flush=True)

    def __repr__(self):
        return "TO BE IMPLEMENTED"
