from cards import *
from random import shuffle, sample


class Game:

    def __init__(self, players_number):
        self.ainames = ['Elvie', 'Mac', 'Lida', 'Todd', 'Soledad', 'Valarie', 'Sylvester',
                        'Ericka', 'Nicolette', 'Clay', 'Claretha', 'Kit', 'Myron', 'Susanne',
                        'Miriam', 'Casimira', 'Zena', 'Hae', 'Chanell', 'Ione']
        self.ainames_index = sample(range(len(self.ainames)), players_number)


        self.deck = [i for i in range(54)]
        self.shuffle_cards()
        self.players_cards = [[self.deck.pop() for _ in range(5)] for _ in range(players_number)]
        self.ai_players = [AIPlayer(self.players_cards[i], self.ainames[self.ainames_index[i]])
                           for i in range(1, players_number)]
        self.card_on_table = self.deck.pop()

        # No bulge card or wait turn card from beginning of game
        while self.bulge_card(self.card_on_table) or self.wait_turn_card(self.card_on_table):
            self.deck.insert(0, self.card_on_table)
            self.card_on_table = self.deck.pop()

    def shuffle_cards(self):
        return shuffle(self.deck)

    # Checks if the card is a bulge
    def bulge_card(self, card):
        if (card == CLUBS_2 or card == CLUBS_3 or card == DIAMONDS_2 or card == DIAMONDS_3 or card == HEARTS_2 or
                card == HEARTS_3 or card == SPADES_2 or card == SPADES_3 or card == JOKER_BLACK or card == JOKER_RED):
            return True
        return False

    # Check if the card is a wait turn card
    def wait_turn_card(self, card):
        if card == CLUBS_4 or card == DIAMONDS_4 or card == HEARTS_4 or card == SPADES_4:
            return True
        return False


class AIPlayer:

    def __init__(self, aicards, name):
        self.playing_cards = aicards
        self.name = name

    @property
    def cards_left(self):
        return len(self.playing_cards)


