# Create virtual environment
# $ python3 -m pip install flask
# $ python3 -m pip install requests

from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

app.config.from_pyfile('config')

API_KEY = app.config['API_KEY']


@app.route('/books', methods=['GET'])
def get_books():
    # Get books from api : https://the-one-api.dev/v2/book
    response = requests.get("https://the-one-api.dev/v2/book")
    

    return jsonify()
    # return render_template('table.html', type="Books", data=books)


@app.route('/movies', methods=["GET"])
def get_movies():
    # Set Authentication Header

    headers = {"Authorization": f'Bearer {API_KEY}'}

    # Get Movies from api: https://the-one-api.dev/v2/movie
    response = requests.get("https://the-one-api.dev/v2/movie",
                            headers=headers)

    extracted_data = response.json()
    movies = extracted_data["docs"]

    return jsonify()
    # return render_template('table.html', type="Movies", data=movies)


@app.route('/characters', methods=["GET"])
def get_characters():

    # Set Authentication Header

    headers = {"Authorization": f'Bearer {API_KEY}'}


    # Get Characters from api: https://the-one-api.dev/v2/character

    response = requests.get("https://the-one-api.dev/v2/character",
                            headers=headers)
    
    extracted_data = response.json()
    characters = extracted_data["docs"]

    return jsonify()
    # return render_template('table.html', type='Characters', data=characters)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
