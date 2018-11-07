from flask import Flask, render_template
import cards
from game import Game

app = Flask(__name__)
game = Game(4)


@app.route('/')
def game_main():
    deckImg = [cards.images[game.players_cards[0][i]] for i in range(5)]
    aiplayers = game.ai_players
    return render_template('game.html', card_on_table=cards.images[game.card_on_table], player_deck=deckImg,
                           players_cards=aiplayers)


if __name__ == '__main__':
    app.run()
