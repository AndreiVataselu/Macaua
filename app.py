from flask import Flask, render_template, jsonify, request
from game import Game

app = Flask(__name__)
game = Game(2)


@app.route('/')
def game_main():
    return render_template('game.html', card_on_table=game.card_on_table, player_deck=game.player_cards,
                           players_cards=game.ai_players)


@app.route('/chosenCard', methods=['POST'])
def chosen_card():
    try:
        player_chosen_card = int(request.json)
        if game.is_compatible(player_chosen_card):
            game.put_card(player_chosen_card)
            if game.is_ace(player_chosen_card):
                return jsonify({
                    'player_cards': render_template('playercards.html', player_deck=game.player_cards),
                    'table_card': render_template('cardOnTable.html', card_on_table=game.card_on_table),
                    'console_text': render_template('console.html', console_text=game.console_text,
                                                    player_name=game.player_name),
                    'ace': True
                })
            else:
                return jsonify({
                    'player_cards': render_template('playercards.html', player_deck=game.player_cards),
                    'table_card': render_template('cardOnTable.html', card_on_table=game.card_on_table),
                    'console_text': render_template('console.html', console_text=game.console_text,
                                                                player_name=game.player_name)
                })

        else:
            print("card not compatible")
            print("{0} on table, you tried {1}".format(game.card_on_table.id, player_chosen_card))
            print(game.current_suit)
            return jsonify({'result': 'failed'})

    except ValueError:
        print('Clicked on screen')
        return jsonify({'result': 'failed'})


@app.route('/drawCard', methods=['POST'])
def draw_card():
    game.draw_card(game.player_cards)

    return jsonify({'player_cards': render_template('playercards.html', player_deck=game.player_cards),
                    'console_text': render_template('console.html', console_text=game.console_text,
                                                    player_name=game.player_name)})


@app.route('/changeSuit', methods=['POST'])
def change_suit():
    game.current_suit = request.json

    return jsonify({
        'console_text': render_template('console.html', console_text=game.console_text, player_name=game.player_name)
    })


if __name__ == '__main__':
    app.run(debug=True)
