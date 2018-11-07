from flask import Flask, render_template
import cards
from game import Game

app = Flask(__name__)


@app.route('/')
def hello_world():
    game = Game(2)
    deckImg = [cards.images[game.players_cards[0][i]] for i in range(5)]
    return render_template('game.html', card_on_table=cards.images[game.card_on_table], player_deck=deckImg)


if __name__ == '__main__':
    app.run()
