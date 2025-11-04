from flask import request  # pyright: ignore[reportMissingImports]
from flask_restful import Resource  # pyright: ignore[reportMissingImports]
from server.models.user import User
from sqlalchemy.exc import IntegrityError  # pyright: ignore[reportMissingImports]

from config import db, api, app


@app.route("/signup", methods=["POST"])
def signup():
    pass
    try:
        data = request.get_json()
        new_user = User(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
        )
        new_user.password_hash = data["password"]
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict(), 201
    except (IntegrityError, ValueError) as e:
        return {"message": str(e)}, 422


@app.route("/login", methods=["POST"])
def login():
    pass


@app.route("/logout", methods=["DELETE"])
def logout():
    pass


class UserResourceById(Resource):
    pass

    def patch(self, id):
        user = User.query.get_or_404(id)
        data = request.get_json()

        if not user.authenticate(data.pop("current_password")):
            return {"message": "Authentication failed. Incorrect password."}, 401

        try:

            for attr in data:
                value = data.get(attr)
                if getattr(user, attr) != value:
                    setattr(user, attr, value)
            db.session.add(user)
            db.session.commit()
            return user.to_dict(), 200
        except (IntegrityError, ValueError) as e:
            db.session.rollback()
            return {"message": str(e)}, 422

    def delete(self, id):
        user = User.query.get_or_404(id)

        # if not user.authenticate(data.pop("current_password")):
        #     return {"message": "Authentication failed. Incorrect password."}, 401

        db.session.delete(user)
        db.session.commit()
        return {}, 204


api.add_resource(UserResourceById, "/users/<int:user_id>")
