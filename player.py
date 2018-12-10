import random

# MAX PLAYERS = 6
PLAYER_0 = 0
PLAYER_1 = 1
PLAYER_2 = 2
PLAYER_3 = 3
PLAYER_4 = 4
PLAYER_5 = 5

class Player:

    def __init__(self, name, player_cards):
        self.name = name
        self.playing_cards = player_cards
        self.turns_to_wait = 0
        self.won = False

    @property
    def cards_left(self):
        return len(self.playing_cards)


class AIPlayer(Player):

    def __init__(self, name, player_cards):
        super().__init__(name, player_cards)

    def make_move(self, game):
        game.take_cards(self)
        put_card = False
        for card in self.playing_cards:
            if game.is_compatible(card.id):
                game.put_card(card.id, self.playing_cards, self.name)
                if game.is_ace(card.id):
                    game.change_suit(random.choice(['diamonds', 'hearts', 'clubs', 'spades']), self.name)
                put_card = True
                game.next_turn()
                break
        if not put_card:
            print('draw card')
            game.draw_card(self.playing_cards, self.name)

