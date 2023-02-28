from random import randint

from flask import Flask

app = Flask(__name__)


@app.route("/")
def guess_number():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp">'


if __name__ == "__main__":
    app.run(debug=True)
