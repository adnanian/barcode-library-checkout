from flask import request  # pyright: ignore[reportMissingImports]

from config import db, api, app
from models.checkout import Checkout


@app.route("/checkout_book/<string:serial_no>", methods=["PATCH"])
def checkout_book(serial_no):
    try:
        data = request.get_json()
        user_id = data.get("user_id")
        checkout_date = data.get("checkout_date")

        checkout_record = Checkout.query.filter_by(serial_no=serial_no).first()
        if not checkout_record:
            return {"message": "Checkout record not found."}, 404

        checkout_record.user_id = user_id
        checkout_record.checkout_date = checkout_date
        db.session.commit()

        return {"message": "Checkout record updated successfully."}, 200
    except Exception as e:
        db.session.rollback()
        return {"message": f"An error occurred: {str(e)}"}, 500
