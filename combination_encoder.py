# combination_encoder.py
#
# Author: Chris LaSota
# Date: July 25, 2021

from combination_table import CombinationTable


class CombinationEncoder():
    """Given a set of N unique items, we can select k of them in C(N,k) ways
       when we don't care about order. If we assign integer IDs from 0 to N-1
       to each of the unique items, then we can represent a particular
       combination of k items using an ordered list of k integer ID values,
       where the ID values are strictly increasing.  In this way, we can
       perform a total ordering on the set of all possible combinations.
       
       It can be useful to map this ordered set of combinations onto the
       sequence of integers from 0 to C(N,k)-1.  

       This class provides a member method which can map every one of the
       unique ordered combinations to this set of integers.
    """

    def __init__(self, items: int, choices: int) -> None:
        self._items = items
        self._choices = choices
        self._combo_table = CombinationTable(items)

    def encode(self, combo_to_encode: list) -> int:
        """ The algorithm employed here REQUIRES that the combination to be
            encoded is passed in as a list of unique integers.  Each
            integer must range from 0 to the value of (self._items - 1)
        """
        # combo_to_encode.sort()    # just in case you didn't do this already
        code = 0
        for item_position in range(self._choices):
            this_item_value = combo_to_encode[item_position]
            if item_position == 0:
                number_of_terms_to_sum = this_item_value
            else:
                number_of_terms_to_sum = (this_item_value - previous_item_value) - 1
            for term_count in range(number_of_terms_to_sum):
                code += self._combo_table.combination(self._items - this_item_value + term_count, self._choices - 1 - item_position) 
            previous_item_value = this_item_value
        return code

