#!/usr/bin/python3
"""A function to determine the fewest number of coins needed
   to meet a given amount total
"""

def makeChange(coins, total):
    """This function will take a list of coins and use
       that to calculate how much change the total will require
    """
    if total <= 0:
        return 0

    else:
        sorted_coins = sorted(coins)
        sorted_coins.reverse()
        coin_count = 0
        for coin in sorted_coins:
            while(total >= coin):
                coin_count += 1
                total -= coin
        if total == 0:
            return coin_count
        return -1
