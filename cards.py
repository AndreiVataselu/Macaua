
# CARDS Class:


class Card:

    def __init__(self, ID):
        self.image = images[ID]
        self.id = ID


# CARDS VARIABLES:

# Clubs (0,11)
CLUBS_2 = 0
CLUBS_3 = 1
CLUBS_4 = 2
CLUBS_5 = 3
CLUBS_6 = 4
CLUBS_7 = 5
CLUBS_8 = 6
CLUBS_9 = 7
CLUBS_10 = 8
CLUBS_J = 9
CLUBS_Q = 10
CLUBS_K = 11
CLUBS_ACE = 12

# Diamonds (13,24)
DIAMONDS_2 = 13
DIAMONDS_3 = 14
DIAMONDS_4 = 15
DIAMONDS_5 = 16
DIAMONDS_6 = 17
DIAMONDS_7 = 18
DIAMONDS_8 = 19
DIAMONDS_9 = 20
DIAMONDS_10 = 21
DIAMONDS_J = 22
DIAMONDS_Q = 23
DIAMONDS_K = 24
DIAMONDS_ACE = 25

# Hearts (26, 37)
HEARTS_2 = 26
HEARTS_3 = 27
HEARTS_4 = 28
HEARTS_5 = 29
HEARTS_6 = 30
HEARTS_7 = 31
HEARTS_8 = 32
HEARTS_9 = 33
HEARTS_10 = 34
HEARTS_J = 35
HEARTS_Q = 36
HEARTS_K = 37
HEARTS_ACE = 38

# Spades (39,50)
SPADES_2 = 39
SPADES_3 = 40
SPADES_4 = 41
SPADES_5 = 42
SPADES_6 = 43
SPADES_7 = 44
SPADES_8 = 45
SPADES_9 = 46
SPADES_10 = 47
SPADES_J = 48
SPADES_Q = 49
SPADES_K = 50
SPADES_ACE = 51

# JOKERS
JOKER_BLACK = 52
JOKER_RED = 53


images = {
    CLUBS_2: '/static/cards/2_of_clubs.png',
    CLUBS_3: '/static/cards/3_of_clubs.png',
    CLUBS_4: '/static/cards/4_of_clubs.png',
    CLUBS_5: '/static/cards/5_of_clubs.png',
    CLUBS_6: '/static/cards/6_of_clubs.png',
    CLUBS_7: '/static/cards/7_of_clubs.png',
    CLUBS_8: '/static/cards/8_of_clubs.png',
    CLUBS_9: '/static/cards/9_of_clubs.png',
    CLUBS_10: '/static/cards/10_of_clubs.png',
    CLUBS_J: '/static/cards/jack_of_clubs2.png',
    CLUBS_Q: '/static/cards/queen_of_clubs2.png',
    CLUBS_K: '/static/cards/king_of_clubs2.png',
    CLUBS_ACE: '/static/cards/ace_of_clubs.png',
    DIAMONDS_2: '/static/cards/2_of_diamonds.png',
    DIAMONDS_3: '/static/cards/3_of_diamonds.png',
    DIAMONDS_4: '/static/cards/4_of_diamonds.png',
    DIAMONDS_5: '/static/cards/5_of_diamonds.png',
    DIAMONDS_6: '/static/cards/6_of_diamonds.png',
    DIAMONDS_7: '/static/cards/7_of_diamonds.png',
    DIAMONDS_8: '/static/cards/8_of_diamonds.png',
    DIAMONDS_9: '/static/cards/9_of_diamonds.png',
    DIAMONDS_10: '/static/cards/10_of_diamonds.png',
    DIAMONDS_J: '/static/cards/jack_of_diamonds2.png',
    DIAMONDS_Q: '/static/cards/queen_of_diamonds2.png',
    DIAMONDS_K: '/static/cards/king_of_diamonds2.png',
    DIAMONDS_ACE: '/static/cards/ace_of_diamonds.png',
    HEARTS_2: '/static/cards/2_of_hearts.png',
    HEARTS_3: '/static/cards/3_of_hearts.png',
    HEARTS_4: '/static/cards/4_of_hearts.png',
    HEARTS_5: '/static/cards/5_of_hearts.png',
    HEARTS_6: '/static/cards/6_of_hearts.png',
    HEARTS_7: '/static/cards/7_of_hearts.png',
    HEARTS_8: '/static/cards/8_of_hearts.png',
    HEARTS_9: '/static/cards/9_of_hearts.png',
    HEARTS_10: '/static/cards/10_of_hearts.png',
    HEARTS_J: '/static/cards/jack_of_hearts2.png',
    HEARTS_Q: '/static/cards/queen_of_hearts2.png',
    HEARTS_K: '/static/cards/king_of_hearts2.png',
    HEARTS_ACE: '/static/cards/ace_of_hearts.png',
    SPADES_2: '/static/cards/2_of_spades.png',
    SPADES_3: '/static/cards/3_of_spades.png',
    SPADES_4: '/static/cards/4_of_spades.png',
    SPADES_5: '/static/cards/5_of_spades.png',
    SPADES_6: '/static/cards/6_of_spades.png',
    SPADES_7: '/static/cards/7_of_spades.png',
    SPADES_8: '/static/cards/8_of_spades.png',
    SPADES_9: '/static/cards/9_of_spades.png',
    SPADES_10: '/static/cards/10_of_spades.png',
    SPADES_J: '/static/cards/jack_of_spades2.png',
    SPADES_Q: '/static/cards/queen_of_spades2.png',
    SPADES_K: '/static/cards/king_of_spades2.png',
    SPADES_ACE: '/static/cards/ace_of_spades2.png',
    JOKER_BLACK: '/static/cards/black_joker.png',
    JOKER_RED: '/static/cards/red_joker.png',

}