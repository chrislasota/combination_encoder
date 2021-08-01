from itertools import combinations
from combination_encoder import CombinationEncoder

# Construct a standard deck of 52 cards and then create all C(52,5) possible
# 5-card hands as lists of 5 unique integers, sorted low to high.  Use this
# collection of hands to test the combination encoder algorithm

DECK_SIZE = 52
HAND_SIZE = 5

def main():
    # create labels for cards for display purposes
    labels = []
    face_values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['c', 'h', 's', 'd']
    for suit in suits:
        for face in face_values:
            labels.append(face + suit)

    # Generate all possible hands using itertools library function.
    cards = [x for x in range(DECK_SIZE)]
    all_possible_hands = list(combinations(cards, HAND_SIZE))
    
    # Create encoder object
    encoder = CombinationEncoder(DECK_SIZE, HAND_SIZE)
   
    # Output results to show that the encode() method yields successive
    # integer-valued codes when we loop through the totally ordered list
    # of possible hands
    for hand in all_possible_hands:
        code = encoder.encode(hand)

        # Display the hand using face and suit 
        for card in hand:
            print(labels[card], end=' ')
        print(':', end=' ')

        # Display corresponding integer values for the cards
        for card in hand:
            print(card, end=' ')
        print(':', end=' ')

        # Display the encoded value for the hand
        print(code)


if __name__ == '__main__':
    main()


