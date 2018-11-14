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
        self.lost = False

    @property
    def cards_left(self):
        return len(self.playing_cards)


class AIPlayer(Player):
    def __init__(self, name, player_cards):
        super().__init__(name, player_cards)
