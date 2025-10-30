# /usr/bin/env python3
from config import app
from models._models import *


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
