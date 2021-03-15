from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# @TODO: setup mongo connection

# @TODO: connect to mongo db and collection


if __name__ == "__main__":
    app.run(debug=True)