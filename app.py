from flask import Flask, render_template, jsonify, request
from game import Game

app = Flask(__name__)
game = Game(4)


@app.route('/')
def game_main():
    return render_template('game.html', card_on_table=game.card_on_table, player_deck=game.player_cards,
                           players_cards=game.ai_players)


@app.route('/cardChose', methods=['POST'])
def card_chose():
    chosen_card = int(request.json)
    game.put_card(chosen_card)

    return jsonify({'player_cards': render_template('playercards.html', player_deck=game.player_cards),
                    'table_card': render_template('cardOnTable.html', card_on_table=game.card_on_table)})


@app.route('/drawCard', methods=['POST'])
def draw_card():
    game.draw_card(game.player_cards)
    return jsonify({'player_cards': render_template('playercards.html', player_deck=game.player_cards)})


if __name__ == '__main__':
    app.run(debug=True)
