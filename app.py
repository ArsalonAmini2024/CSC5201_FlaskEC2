# CSC5201 Flask Application running on EC2 Server
# Student: Arsalon Amini - Hajibashi

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>CSC5201 Flask Application</title>
        <style>
            h1 {
                color: blue;
            }
        </style>
    </head>
    <body>
        <h1>CSC5201 Spring 2024</h1>
        <h2>Digital Ocean - Platform as a service</h2>
        <p>Flask Application running on Digital Ocean</p>
        <p>Student: Arsalon Amini - Hajibashi</p>
    </body>
    </html>
    '''
    return html_content


if __name__ == "__main__":
    app.run()
