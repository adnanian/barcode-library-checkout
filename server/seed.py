import os

from config import db, app
from models._models import *


def clear_tables():
    """Clears all tables in the database."""
    success = True
    for table in reversed(db.metadata.sorted_tables):
        try:
            # Use the db.session.execute() method provided by Flask-SQLAlchemy
            db.session.execute(table.delete())
            print(f"Truncated table: {table.name}")
        except Exception as e:
            print(f"Error truncating table {table.name}: {e}")
            db.session.rollback()  # Rollback on error
            success = False
    if success:
        db.session.commit()
        print("All tables cleared successfully.")
    else:
        print("Some tables could not be cleared. See errors above.")
        exit(1)


def seed_users():
    """Seeds the users table with initial data."""
    if not (seed_password := os.getenv("SEED_PASSWORD")):
        raise ValueError("SEED_PASSWORD environment variable is not set.")
    from seed_data.user_seed import USER_SEED

    for user_data in USER_SEED:
        user = User(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            email=user_data["email"],
        )

        user.password_hash = seed_password
        db.session.add(user)
    db.session.commit()
    print("Seeded users table.")


def seed_books():
    """
    Seeds the books table with initial data.
    Goal is to seed at least 20 books.
    """
    from seed_data.book_seed import BOOK_SEED

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
    """Seeds the book_copies table with initial data."""
    copies = []
    from seed_data.copy_seed import COPY_SEED

    for copy_data in COPY_SEED:
        book = Book.query.filter_by(isbn=copy_data["isbn"]).first()
        if book:
            for i in range(copy_data["copies"]):
                copy = BookCopy(
                    serial_no=f"{book.isbn}-C-{i+1}",
                    book_id=book.id,
                )
                copies.append(copy)
    db.session.add_all(copies)
    db.session.commit()

    print("Seeded book copies table.")


def seed_checkouts():
    """Seeds the checkouts table with initial data."""
    checkouts = []
    from seed_data.checkout_seed import CHECKOUT_SEED

    for checkout_data in CHECKOUT_SEED:
        user = User.query.filter_by(email=checkout_data["email"]).first()
        book_copy = BookCopy.query.filter_by(
            serial_no=checkout_data["book_copy_serial"]
        ).first()
        if user and book_copy:
            checkout = Checkout(
                checkout_date=checkout_data["checkout_date"],
                due_date=checkout_data["due_date"],
                return_date=checkout_data["return_date"],
                user_id=user.id,
                book_copy_id=book_copy.id,
            )
            checkouts.append(checkout)
    db.session.add_all(checkouts)
    db.session.commit()

    print("Seeded checkouts table.")


if __name__ == "__main__":
    with app.app_context():
        # Clear all tables in the database
        clear_tables()
        # Seed the database with initial data
        seed_users()
        seed_books()
        seed_book_copies()
        seed_checkouts()
        print("Database seeding completed.")
