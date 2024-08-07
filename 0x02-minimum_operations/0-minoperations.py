#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste.
Given a number n, write a method that calculates the fewest
number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """Calculate fewest no. of operations needed to result in n H characters"""
    f = 0
    z = 2
    while n > 1:
        while not n % z:
            f += z
            n /= z
        z += 1
    return f