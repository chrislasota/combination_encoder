# test_encoder.py
#
# Author: Chris LaSota
# Date: July 25, 2021

from itertools import combinations
from combination_encoder import CombinationEncoder

NUMBER_OF_ITEMS = 6
NUMBER_OF_CHOICES = 3

def main():
    # Generate all possible combinations using itertools library function.
    items = [x for x in range(NUMBER_OF_ITEMS)]
    all_possible_combinations = list(combinations(items, NUMBER_OF_CHOICES))

    # Create encoder object
    encoder = CombinationEncoder(NUMBER_OF_ITEMS, NUMBER_OF_CHOICES)

    # Show that it works as expected
    print(f"Number of items to choose from : {NUMBER_OF_ITEMS}" 
          + "  {" + f"0...{NUMBER_OF_ITEMS - 1}" + '}')
    print(f"Number of items in each combination : {NUMBER_OF_CHOICES}")
    print("COMBINATION : CODE")

    for combination in all_possible_combinations:
        code = encoder.encode(combination)

        print(combination, " : ", code)
        
    print(f"Total combinations = {code + 1}")


if __name__ == '__main__':
    main()

