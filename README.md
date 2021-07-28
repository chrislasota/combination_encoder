# combination_encoder

Python implementation of an algorithm to uniquely map every element of a set of "N-choose-k" combinations to consecutive integers from 0 to C(N,k)-1, preserving the ordering of each combination from low values to high values.
 
Run the test code in a terminal:
>$ python3 test_encoder.py


For a more extensive test using 5-card hands from a 52-card deck, run this test code:
>$ python3 test_poker_hand_encoding.py > output.txt

This test may take a minute or two since all C(52,5) = 2,598,960 combinations are being encoded and output

Then look at the output file to verify that each ordered hand of 5 cards has a matching code that increments by 1
>$ less output.txt

Check the line count of the output file:
>$ wc -l output.txt


