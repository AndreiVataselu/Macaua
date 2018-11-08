from flask import Flask, render_template, jsonify
from game import Game

app = Flask(__name__)
game = Game(4)


@app.route('/')
def game_main():
    return render_template('game.html', card_on_table=game.card_on_table, player_deck=game.player_cards,
                           players_cards=game.ai_players)


@app.route('/cardChose', methods=['POST'])
def card_chose():
    print("Updating card here")
    return jsonify({'result': 'success'})


@app.route('/drawCard', methods=['POST'])
def draw_card():
    game.draw_card(game.player_cards)

    # Had to return 'player_deck' as a list of a single element so the AJAX script can iterate
    # through it and append to existing cards.
    return jsonify({'data': render_template('playercards.html', player_deck=game.player_cards)})


if __name__ == '__main__':
    app.run()
