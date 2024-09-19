#!/usr/bin/python3
""" A function that determines the fewest number of coins
needed to meet a given amount total
"""

def fewestCoins(denominations, amount):
    """Determines the fewest number of coins to make the total amount
    Args:
        denominations (list[int]) : list of different coin values
        amount (int): The target amount

    Return:
        coin_count (int): the fewest number of coins
    """

    if amount < 1:
        return 0

    coin_count = -1

    if len(denominations):
        denominations = sorted(denominations, reverse=True)
        num_of_denominations = len(denominations)
        coin_count = 0

        for i in range(num_of_denominations):
            while amount:
                # if total >= 1:
                if amount - denominations[i] >= 0:
                    coin_count += 1
                    amount -= denominations[i]
                else:
                    break

        if amount != 0:
            coin_count = -1

    return coin_count
