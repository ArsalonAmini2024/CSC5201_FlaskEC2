# CSC5201 Flask Application running on EC2 Server
# Student: Arsalon Amini - Hajibashi

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'CSC5201 Flask Application - Hello World'


if __name__ == "__main__":
    app.run()
