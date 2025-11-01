import os

from config import db, app
from models._models import *


def clear_tables():
    pass
    for table in reversed(db.metadata.sorted_tables):
        try:
            # Use the db.session.execute() method provided by Flask-SQLAlchemy
            db.session.execute(table.delete())
            print(f"Truncated table: {table.name}")
        except Exception as e:
            print(f"Error truncating table {table.name}: {e}")
            db.session.rollback()  # Rollback on error


def seed_users():
    """Seeds the users table with initial data."""
    from seed_data.user_seed import USER_SEED  # type: ignore

    for user_data in USER_SEED:
        user = User(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            email=user_data["email"],
            password_hash=os.getenv("SEED_PASSWORD"),
        )
        db.session.add(user)
    db.session.commit()
    print("Seeded users table.")


def seed_books():
    """
    Seeds the books table with initial data.
    Goal is to seed at least 20 books.
    """
    from seed_data.book_seed import BOOK_SEED  # type: ignore

    for book_data in BOOK_SEED:
        book = Book(
            title=book_data["title"],
            author=book_data["author"],
            year=book_data["year"],
            isbn=book_data["isbn"],
        )
        db.session.add(book)
    db.session.commit()

    print("Seeded books table.")


def seed_book_copies():
    pass  # Implement book copy seeding logic here


def seed_checkouts():
    pass  # Implement checkout seeding logic here


if __name__ == "__main__":
    with app.app_context():
        if not os.getenv("SEED_PASSWORD"):
            raise ValueError("SEED_PASSWORD environment variable is not set.")
        # Clear all tables in the database
        clear_tables()
        # Seed the database with initial data
        seed_users()
        seed_books()
        seed_book_copies()
        seed_checkouts()
