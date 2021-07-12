# Create virtual environment
# $ python3 -m pip install flask

from flask import Flask, jsonify, request
app = Flask(__name__)

# Data
players = [
    {
        'id': 1,
        'name': 'Harry Kane',
        'country': 'England'
    },
    {
        'id': 2,
        'name': 'Kevin De Bruyne',
        'country': 'Belgium'
    },
    {
        'id': 3,
        'name': 'Toni Kroos',
        'country': 'Germany'
    }
]

# GET ALL PLAYERS


@app.route('/', methods=['GET'])
def get_players():
    #------------------------ Player Get Logic Here -------------------------#
    return jsonify(players)

# CREATE A PLAYER


@app.route('/', methods=['POST'])
def create_player():
    # Get New Player data from request
    new_player = request.get_json()

    id = new_player['id']
    name = new_player['name']
    country = new_player['country']

    #------------------------ Player Creation Logic Here -------------------------#
    print(new_player)

    players.append(
        {
            'id': id,
            'name': name,
            'country': country
        }
    )


    return jsonify({'message': 'player created'})

# UPDATE A PLAYER


@app.route('/<int:id>', methods=['PUT'])
def update_player(id):
    # Get New Player data from request
    new_player = request.get_json()
    new_name = new_player['name']
    new_country = new_player['country']

    for player in players:
        if player['id'] == id:
            #------------------------ Player Update Logic Here -------------------------#
            player['name'] = new_name
            player['country'] = new_country
            return jsonify({'message': 'player updated'})

    return jsonify({'message': f'Player with id {id} does not exist'})


# DELETE A PLAYER
@app.route('/<int:id>', methods=["DELETE"])
def delete_player(id):
    for player in players:
        if player["id"] == id:
            #------------------------ Delete player logic-------------------------#
            players.remove(player)
            return jsonify({'message': 'player deleted'})

    return jsonify({'message': f'Player with id {id} does not exist'})


# GET PLAYER BY ID
@app.route('/<int:id>', methods=["GET"])
def get_player_by_id(id):
    for player in players:
        if player["id"] == id:
            #------------------------ Single Player Get Logic Here -------------------------#
            return jsonify(player)

    return jsonify({'message': f'Player with id {id} does not exist'})


if __name__ == '__main__':
    app.run(port=5001, debug=True)
