#!/usr/bin/python3
"""
This module contains the implementation of the function minOperations()
which calculates the minimum number of operations needed to produce
exactly n H characters in a text file using only the
operations Copy All and Paste.
"""


def minOperations(n: int) -> int:
    """
    Calculates the minimum number of operations needed to produce
    exactly n 'H' characters in a text file using only the
    operations 'Copy All' and 'Paste'.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required to obtain
             exactly n 'H' characters, or 0 if it is impossible.
    """
    if n < 2:
        return 0

    operations = 0
    current = 1

    # Iterate over possible factors from 2 to the square root of n.
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:  # While i is a factor of n
            operations += i
            n //= i  # Reduce n by the factor

    # If n is still greater than 1, then it is a prime number
    if n > 1:
        operations += n  # Add the prime factor itself

    return operations
