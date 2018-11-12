from flask import Flask, render_template, jsonify, request
from game import Game
from player import *
import random

app = Flask(__name__)
game = Game(3)


@app.route('/')
def game_main():

    return render_template('game.html', card_on_table=game.card_on_table, player_deck=game.player.playing_cards,
                           players_cards=game.ai_players)


@app.route('/AImove', methods=['POST'])
def ai_make_move():
    if game.turn != 0:
        put_card = False
        ai_name = game.ai_players[game.turn - 1].name
        for card in game.ai_players[game.turn - 1].playing_cards:
            if game.is_compatible(card.id):
                print('found compatible {0}'.format(card.id))
                game.put_card(card.id, game.ai_players[game.turn - 1].playing_cards)
                put_card = True
                if game.is_ace(card.id):
                    game.current_suit = random.choice(['diamonds', 'hearts', 'clubs', 'spades'])
                break
        if not put_card:
            print('draw card')
            game.draw_card(game.ai_players[game.turn - 1].playing_cards)

        return jsonify({
            'console_text': render_template('console.html', console_text=game.console_text,
                                            player_name=ai_name),
            'table_card': render_template('cardOnTable.html', card_on_table=game.card_on_table),
            'aiPlayers': render_template('aiPlayersCards.html', players_cards=game.ai_players),
            'turnsToMake': len(game.ai_players)
        })


@app.route('/chosenCard', methods=['POST'])
def chosen_card():
    if game.turn == PLAYER_0:
        try:
            player_chosen_card = int(request.json)
            if game.is_compatible(player_chosen_card):
                game.put_card(player_chosen_card, game.player.playing_cards)
                if game.is_ace(player_chosen_card):
                    return jsonify({
                        'player_cards': render_template('playercards.html', player_deck=game.player.playing_cards),
                        'table_card': render_template('cardOnTable.html', card_on_table=game.card_on_table),
                        'console_text': render_template('console.html', console_text=game.console_text,
                                                        player_name=game.player.name),
                        'ace': True,
                        'turnsToMake': len(game.ai_players)
                    })
                else:
                    return jsonify({
                        'player_cards': render_template('playercards.html', player_deck=game.player.playing_cards),
                        'table_card': render_template('cardOnTable.html', card_on_table=game.card_on_table),
                        'console_text': render_template('console.html', console_text=game.console_text,
                                                        player_name=game.player.name),
                        'turnsToMake': len(game.ai_players)
                    })

            else:
                print("card not compatible")
                print("{0} on table, you tried {1}".format(game.card_on_table.id, player_chosen_card))
                print(game.current_suit)
                return jsonify({'result': 'failed'})

        except ValueError:
            print('Clicked on screen')
            return jsonify({'result': 'failed'})
    else:
        return jsonify({'result': 'failed'})


@app.route('/drawCard', methods=['POST'])
def draw_card():
    if game.turn == PLAYER_0:
        game.draw_card(game.player.playing_cards)

        return jsonify({'player_cards': render_template('playercards.html', player_deck=game.player.playing_cards),
                        'console_text': render_template('console.html', console_text=game.console_text,
                                                        player_name=game.player.name),
                        'turnsToMake': len(game.ai_players)})
    else:
        return jsonify({'result': 'failed'})


@app.route('/changeSuit', methods=['POST'])
def change_suit():
    game.current_suit = request.json

    return jsonify({
        'console_text': render_template('console.html', console_text=game.console_text, player_name=game.player.name),
        'turnsToMake': len(game.ai_players)})


if __name__ == '__main__':
    app.run(debug=True)
