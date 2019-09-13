import CardGen as CardGen


def play():
    is_last_card = len(CardGen.list_dealt) == 51
    if is_last_card:
        print("This is the last card.")

    card, draw_speech = CardGen.draw_card()

    print(draw_speech)

    if is_last_card:
        print("Thank you for playing.")


play()
