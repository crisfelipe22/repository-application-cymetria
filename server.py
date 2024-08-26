from flask import Flask
from database.db import *

app = Flask(__name__)

from routes.router import *

if __name__ == "__main__":
    host = "0.0.0.0"
    port = "80"
    app.run(host, port)