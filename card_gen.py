from random import randint, choice


def draw_card():
    card, draw = draw_cards(1)  # call the function with the number of cards you want.
    draw_speech = "Your card is the {0}".format(draw)

    return card, draw_speech


class Card:
    def __init__(self, card, name, description):
        self.card = card
        self.name = name
        self.description = description
        self.suit = ''


suits = {
    0: 'Clubs',
    1: 'Diamonds',
    2: 'Hearts',
    3: 'Spades'
}

cards = [
    Card('Ace', 'Waterfall', 'Keep drinking until the person to your right stops.'),
    Card('2', 'You', 'Pick a player to take a sip.'),
    Card('3', 'Me', 'Take a lonely sip.'),
    Card('4', 'Bros', 'All dudes must drink.'),
    Card('5', 'Thumb Master', 'Last person with their thumb on the table must drink, when prompted by the Thumb Master.'),
    Card('6', 'Chicks', 'All chicks must drink.'),
    Card('7', 'Heaven', 'Last person with their finger to heaven must drink, when prompted by the Heaven Master.'),
    Card('8', 'Mate', 'Pick a mate to drink with, you are now forever linked.'),
    Card('9', 'Rhyme', 'Pick a word and the person to your left must come up with a rhyming word.'),
    Card('10', 'Categories', 'Pick a category and the person to your left must name something in that category.'),
    Card('Jack', 'Make a Rule', 'Make a rule that lasts for the rest of the game.'),
    Card('Queen', 'Question Master', 'If anybody answers your questions they must drink.'),
    Card('King', "King's Tax", 'Add a bit of your drink to the dirty pint.')
]

list_dealt = []

def draw_cards(num_of_cards):
    for z in range(num_of_cards):
        card = choice(cards)

        x = randint(0, 3)  # random integer 0 to 3 to pick suit
        card.suit = suits[x]

        if [card.card, card.suit] not in list_dealt:
            list_dealt.append([card.card, card.suit])

            card_rule = get_card_rule(card)
            my_draw = "{0} of {1}, {2}".format(card.card, card.suit, card_rule)

            return card, my_draw
        elif len(list_dealt) != 52:
            num_of_cards = num_of_cards - z
            return draw_cards(num_of_cards)
        else:
            return


def get_card_rule(card):
    if card.card == "King":
        if len(list_dealt) > 0:
            kings = list(filter(lambda x: x[0] == "King", list_dealt))

            if len(kings):
                card_rule_text = "This is the last King, drink the dirty pint!"
                return card_rule_text
    if True:
        card_rule_text = "{0}. {1}".format(card.name, card.description)
        return card_rule_text