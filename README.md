# combination_encoder

Python implementation of an algorithm to uniquely map every element of a set of "N-choose-k" combinations to consecutive integers from 0 to C(N,k)-1, preserving the ordering of each combination from low values to high values.

Run the test code in a terminal:
>$ python3 test_encoder.py
>Number of items to choose from : 6  {0...5}
>Number of items in each combination : 3
>COMBINATION : CODE
>(0, 1, 2)  :  0
>(0, 1, 3)  :  1
>(0, 1, 4)  :  2
>(0, 1, 5)  :  3
>(0, 2, 3)  :  4
>(0, 2, 4)  :  5
>(0, 2, 5)  :  6
>(0, 3, 4)  :  7
>(0, 3, 5)  :  8
>(0, 4, 5)  :  9
>(1, 2, 3)  :  10
>(1, 2, 4)  :  11
>(1, 2, 5)  :  12
>(1, 3, 4)  :  13
>(1, 3, 5)  :  14
>(1, 4, 5)  :  15
>(2, 3, 4)  :  16
>(2, 3, 5)  :  17
>(2, 4, 5)  :  18
>(3, 4, 5)  :  19
>Total combinations = 20

For a more extensive test using 5-card hands from a 52-card deck, run this test code:
>$ python3 test_poker_hand_encoding.py > output.txt

This test may take a minute or two since all C(52,5) = 2,598,960 combinations are being encoded and output

Then look at the output file to verify that each ordered hand of 5 cards has a matching code that increments by 1
>$ less output.txt

Check the line count of the output file:
>$ wc -l output.txt


