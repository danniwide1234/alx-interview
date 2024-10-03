#!/usr/bin/python3
"""
Prime Game
"""


def primeNumbers(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    primeNos = []
    sieve = [True] * (n + 1)  # Renamed 'filtered' to 'sieve'
    for prime in range(2, n + 1):
        if sieve[prime]:
            primeNos.append(prime)
            for i in range(prime, n + 1, prime):
                sieve[i] = False
    return primeNos


def isWinner(rounds, limits):
    """
    Determines winner of Prime Game
    Args:
        rounds (int): no. of rounds of game (renamed 'x' to 'rounds')
        limits (list): upper limit of range for each round (renamed 'nums' to 'limits')
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if rounds is None or limits is None or rounds == 0 or limits == []:
        return None
    Maria = Ben = 0
    for i in range(rounds):
        primeNos = primeNumbers(limits[i])
        if len(primeNos) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
