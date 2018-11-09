from cards import *
from random import shuffle, sample


class Game:

    def __init__(self, players_number):
        self.ainames = ['Elvie', 'Mac', 'Lida', 'Todd', 'Soledad', 'Valarie', 'Sylvester',
                        'Ericka', 'Nicolette', 'Clay', 'Claretha', 'Kit', 'Myron', 'Susanne',
                        'Miriam', 'Casimira', 'Zena', 'Hae', 'Chanell', 'Ione']
        self.ainames_index = sample(range(len(self.ainames)), players_number)

        self.deck = [Card(i) for i in range(54)]
        self.shuffle_cards()
        self.handed_cards = [[self.deck.pop() for _ in range(5)] for _ in range(players_number)]
        self.ai_players = [AIPlayer(self.handed_cards[i], self.ainames[self.ainames_index[i]])
                           for i in range(1, players_number)]
        self.player_cards = self.handed_cards[0]

        self.card_on_table = self.deck.pop()

        # No bulge card or wait turn card from beginning of game
        while self.is_bulge_card(self.card_on_table.id) or self.is_wait_turn_card(self.card_on_table.id):
            self.deck.insert(0, self.card_on_table)
            self.card_on_table = self.deck.pop()

    # Basic cards functions
    def shuffle_cards(self):
        return shuffle(self.deck)

    def draw_card(self, player_deck):
        player_deck.append(self.deck.pop())

    def put_card(self, card):
        self.deck.insert(0, self.card_on_table)

        for player_card in self.player_cards:
            if player_card.id == card:
                self.card_on_table = self.player_cards.pop(self.player_cards.index(player_card))

    # Game functions

    # Checks if the card is a bulge
    def is_bulge_card(self, card):
        if (card == CLUBS_2 or card == CLUBS_3 or card == DIAMONDS_2 or card == DIAMONDS_3 or card == HEARTS_2 or
                card == HEARTS_3 or card == SPADES_2 or card == SPADES_3 or card == JOKER_BLACK or card == JOKER_RED):
            return True
        return False

    # Check if the card is a wait turn card
    def is_wait_turn_card(self, card):
        if card == CLUBS_4 or card == DIAMONDS_4 or card == HEARTS_4 or card == SPADES_4:
            return True
        return False

    def is_same_type(self, card):
        for i in range(4):
            if self.card_on_table.id + i*13 == card or self.card_on_table.id - i*13 == card:
                return True
        return False

    def is_compatbile(self, card):
        # Clubs (0,11) ; # Diamonds (13,24) ; # Hearts (26, 37) ; # Spades (39,50)
        if self.card_on_table.id in range(CLUBS_2, CLUBS_K+1) and card in range(CLUBS_2, CLUBS_K+1):
            return True
        elif self.card_on_table.id in range(DIAMONDS_2, DIAMONDS_K+1) and card in range(DIAMONDS_2, DIAMONDS_K+1):
            return True
        elif self.card_on_table.id in range(HEARTS_2, HEARTS_K+1) and card in range(HEARTS_2, HEARTS_K+1):
            return True
        elif self.card_on_table.id in range(SPADES_2, SPADES_K+1) and card in range(SPADES_2, SPADES_K+1):
            return True
        elif self.is_bulge_card(self.card_on_table.id) and self.is_bulge_card(card):
            return True
        elif self.is_wait_turn_card(self.card_on_table.id) and self.is_wait_turn_card(card):
            return True
        elif self.is_same_type(card):
            return True
        return False


class AIPlayer:

    def __init__(self, aicards, name):
        self.playing_cards = aicards
        self.name = name

    @property
    def cards_left(self):
        return len(self.playing_cards)


