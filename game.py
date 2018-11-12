from cards import *
from random import shuffle, sample
from player import *


class Game:

    def __init__(self, players_number):
        self.ainames = ['Elvie', 'Mac', 'Lida', 'Todd', 'Soledad', 'Valerie', 'Sylvester',
                        'Ericka', 'Nicolette', 'Clay', 'Claretha', 'Kit', 'Myron', 'Susanne',
                        'Miriam', 'Casimira', 'Zena', 'Hae', 'Chanell', 'Ione']
        self.ainames_index = sample(range(len(self.ainames)), players_number)

        self.console_text = ""
        # The current suit will never be ace unless it's the first card of the game so the player can put down
        # whatever card he wants, so we set it 'ace' as default.
        self._current_suit = 'ace'
        self.deck = [Card(i) for i in range(54)]
        self.shuffle_cards()
        self.handed_cards = [[self.deck.pop() for _ in range(5)] for _ in range(players_number)]
        self.ai_players = [AIPlayer(player_cards=self.handed_cards[i], name=self.ainames[self.ainames_index[i]],
                                    player_index=i) for i in range(1, players_number)]

        self.player = Player(name="Michael", player_cards=self.handed_cards[0], player_index=0)

        self._turn = [i for i in range(players_number)]
        self.turn = None
        self.next_turn()

        self.card_on_table = self.deck.pop()

        # No bulge card or wait turn card from beginning of game
        while self.is_bulge_card(self.card_on_table.id) or self.is_wait_turn_card(self.card_on_table.id):
            self.deck.insert(0, self.card_on_table)
            self.card_on_table = self.deck.pop()

    @property
    def current_suit(self):
        if self.card_on_table.suit != 'ace':
            self._current_suit = self.card_on_table.suit
        return self._current_suit

    @current_suit.setter
    def current_suit(self, suit):
        self.console_text = "changes the suit to {0}".format(suit.title())
        self._current_suit = suit

    # Cycle through a list
    def next_turn(self):
        self.turn = self._turn.pop(0);
        self._turn.append(self.turn)

    # Basic cards functions
    def shuffle_cards(self):
        return shuffle(self.deck)

    def draw_card(self, player_deck):
        player_deck.append(self.deck.pop())
        self.console_text = "draws a card!"
        self.next_turn()

    def put_card(self, card, playing_cards):
        self.deck.insert(0, self.card_on_table)

        for player_card in playing_cards:
            if player_card.id == card:
                self.card_on_table = playing_cards.pop(playing_cards.index(player_card))
                self.console_text = "places a card of {0}".format(names[card])
                self.next_turn()

    # -----------------------------------   Game functions   --------------------------------------------------

    def is_ace(self, card):
        if card == SPADES_ACE or card == HEARTS_ACE or card == DIAMONDS_ACE or card == CLUBS_ACE:
            return True
        return False

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

    def is_same_value(self, card):  # Same number but not same suit
        for i in range(4):
            if self.card_on_table.id + i*13 == card or self.card_on_table.id - i*13 == card:
                return True
        return False

    def is_compatible(self, card):
        card_suit = Card(card).suit

        if self.current_suit == card_suit:
            return True
        elif self.is_bulge_card(self.card_on_table.id) and self.is_bulge_card(card):
            return True
        elif self.is_wait_turn_card(self.card_on_table.id) and self.is_wait_turn_card(card):
            return True
        elif self.is_same_value(card):
            return True
        elif self.is_ace(card):
            return True
        elif self.current_suit == 'ace':  # Current suit will never be ace unless it's first card.
            return True
        elif card == JOKER_RED or card == JOKER_BLACK:
            return True
        elif self.current_suit == 'joker':
            return True
        return False

    # ---------------------------------------------------------------------------------------------------------

