"""
Probability of rolling a 1 out of n dice: 1 - (5/6)**n
Expected value: (10 / 3) * n

Safest # to roll normally: 3

When opponent is far ahead, roll safer.
When opponent is far behind, roll risky.

    Dice rolled:  1
    Change of scoring 1: 16.67%
    Chance of scoring more than 1: 83.33%
    Expected gain if no 1s: 3.33

    Dice rolled:  2
    Change of scoring 1: 30.56%
    Chance of scoring more than 1: 69.44%
    Expected gain if no 1s: 6.67

    Dice rolled:  3
    Change of scoring 1: 42.13%
    Chance of scoring more than 1: 57.87%
    Expected gain if no 1s: 10.00

    Dice rolled:  4
    Change of scoring 1: 51.77%
    Chance of scoring more than 1: 48.23%
    Expected gain if no 1s: 13.33

    Dice rolled:  5
    Change of scoring 1: 59.81%
    Chance of scoring more than 1: 40.19%
    Expected gain if no 1s: 16.67

    Dice rolled:  6
    Change of scoring 1: 66.51%
    Chance of scoring more than 1: 33.49%
    Expected gain if no 1s: 20.00

    Dice rolled:  7
    Change of scoring 1: 72.09%
    Chance of scoring more than 1: 27.91%
    Expected gain if no 1s: 23.33

    Dice rolled:  8
    Change of scoring 1: 76.74%
    Chance of scoring more than 1: 23.26%
    Expected gain if no 1s: 26.67

    Dice rolled:  9
    Change of scoring 1: 80.62%
    Chance of scoring more than 1: 19.38%
    Expected gain if no 1s: 30.00

    Dice rolled:  10
    Change of scoring 1: 83.85%
    Chance of scoring more than 1: 16.15%
    Expected gain if no 1s: 33.33

Log opponent's scores. If they play more risky, uhhhh...

Choose to swap when... opponent[0] < opponent[1] and expected_value =< swap_value

Roll zero dice when the benefit of that is equal to or greater than the expected outcome of a roll otherwise
"""

def p_roll_1():
    for x in range(1, 11):
        chance_of_score_1 = (1 - (5/6) ** x) * 100
        print("Dice rolled: ", x)
        print(f"Change of scoring 1: {chance_of_score_1:.2f}%")
        print(f"Chance of scoring more than 1: {(100 - chance_of_score_1):.2f}%")
        print(f"Expected gain if no 1s: {((10 / 3) * x):.2f}")
        print()

p_roll_1()