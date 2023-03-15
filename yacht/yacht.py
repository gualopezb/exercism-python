from collections import Counter


def four_or_a_kind(dice):
    data = next((key for key, value in dict(Counter(dice)).items() if value >= 4), None)

    return 0 if not data else data * 4


def full_house(dice):
    counts = dict(Counter(dice))
    return (
        sum(dice)
        if len(counts) == 2 and all(number in counts.values() for number in [3, 2])
        else 0
    )


YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = lambda dice: len([one for one in dice if one == 1])
TWOS = lambda dice: 2 * len([two for two in dice if two == 2])
THREES = lambda dice: 3 * len([three for three in dice if three == 3])
FOURS = lambda dice: 4 * len([four for four in dice if four == 4])
FIVES = lambda dice: 5 * len([five for five in dice if five == 5])
SIXES = lambda dice: 6 * len([six for six in dice if six == 6])
FULL_HOUSE = lambda dice: full_house(dice)
FOUR_OF_A_KIND = lambda dice: four_or_a_kind(dice)
LITTLE_STRAIGHT = lambda dice: 30 if len(set(dice)) == 5 and 6 not in dice else 0
BIG_STRAIGHT = lambda dice: 30 if len(set(dice)) == 5 and 1 not in dice else 0
CHOICE = lambda dice: sum(dice)


def score(dice, category):
    return category(dice)
