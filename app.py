from flask import Flask, render_template, jsonify, request
from game import Game
from player import *
import random

app = Flask(__name__)
game = Game(2)


@app.route('/')
def game_main():

    return render_template('game.html', card_on_table=game.card_on_table, player_deck=game.player.playing_cards,
                           players_cards=game.ai_players)


@app.route('/AImove', methods=['POST'])
def ai_make_move():
    if game.turn != 0:
        ai_player = game.ai_players[game.turn - 1]
        game.check_wait_turn(ai_player)
        if ai_player.turns_to_wait == 0:
            game.take_cards(ai_player)
            put_card = False
            for card in ai_player.playing_cards:
                if game.is_compatible(card.id):
                    game.put_card(card.id, ai_player.playing_cards, ai_player.name)
                    if game.is_ace(card.id):
                        game.change_suit(random.choice(['diamonds', 'hearts', 'clubs', 'spades']), ai_player.name)
                    put_card = True
                    game.next_turn()
                    break
            if not put_card:
                print('draw card')
                game.draw_card(ai_player.playing_cards, ai_player.name)

        else:
            game.skip_turn(ai_player)

        return jsonify({
            'console_text': render_template('console.html', console_messages=game.console),
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
                game.put_card(player_chosen_card, game.player.playing_cards, game.player.name)
                if game.is_ace(player_chosen_card):
                    return jsonify({
                        'player_cards': render_template('playercards.html', player_deck=game.player.playing_cards),
                        'table_card': render_template('cardOnTable.html', card_on_table=game.card_on_table),
                        'console_text': render_template('console.html', console_messages=game.console),
                        'ace': True,
                        'turnsToMake': len(game.ai_players)
                    })
                else:
                    game.next_turn()
                    return jsonify({
                        'player_cards': render_template('playercards.html', player_deck=game.player.playing_cards),
                        'table_card': render_template('cardOnTable.html', card_on_table=game.card_on_table),
                        'console_text': render_template('console.html', console_messages=game.console),
                        'turnsToMake': len(game.ai_players)
                    })

            else:
                return jsonify({'result': 'failed'})

        except ValueError:
            print('Clicked on screen')
            return jsonify({'result': 'failed'})

    else:
        return jsonify({'result': 'failed'})


@app.route('/drawCard', methods=['POST'])
def draw_card():
    if game.turn == PLAYER_0:
        game.draw_card(game.player.playing_cards, game.player.name)

        return jsonify({'player_cards': render_template('playercards.html', player_deck=game.player.playing_cards),
                        'console_text': render_template('console.html', console_messages=game.console),
                        'turnsToMake': len(game.ai_players)})
    else:
        return jsonify({'result': 'failed'})


@app.route('/changeSuit', methods=['POST'])
def change_suit():
    game.change_suit(request.json, game.player.name)
    game.next_turn()
    return jsonify({
        'console_text': render_template('console.html', console_messages=game.console),
        'turnsToMake': len(game.ai_players)
    })


@app.route('/playerTakeCards', methods=['POST'])
def player_take_cards():
    if game.player.turns_to_wait == 0:  #TODO: AND user has no bulge cards
        game.take_cards(game.player)
        return jsonify({
            'console_text': render_template('console.html', console_messages=game.console),
            'player_cards': render_template('playercards.html', player_deck=game.player.playing_cards)
        })

@app.route('/playerWaitTurn', methods=['POST'])
def player_wait_turn():
    game.check_wait_turn(game.player)
    skip_player = False
    if game.player.turns_to_wait > 0:
        game.skip_turn(game.player)
        skip_player = True
        print("Game skip: {0}".format(skip_player))

    return jsonify({
        'console_text': render_template('console.html', console_messages=game.console),
        'turnsToMake': len(game.ai_players),
        'skipPlayer': skip_player
    })


if __name__ == '__main__':
    app.run()
