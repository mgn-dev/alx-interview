#!/usr/bin/python3
"""
This module contains the implementation of the function minOperations()
which calculates the minimum number of operations needed to produce
exactly n H characters in a text file using only the
operations Copy All and Paste.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to produce
    exactly n 'H' characters in a text file using only the
    operations 'Copy All' and 'Paste'.

    The function returns the number of operations required or
    0 if it is impossible to achieve exactly n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required to obtain
             exactly n 'H' characters, or 0 if it is impossible.
    """

    # If n is less than 2, there are no operations
    # needed as we start with one 'H'
    if n < 2:
        return 0

    operations = 0
    current = 1

    # Iterate over possible factors from 2 to n.
    for i in range(2, n + 1):
        # While i is a factor of n
        while n % i == 0:
            # Add the factor itself (1 Copy + i - 1 Pastes)
            operations += i
            n //= i  # Reduce n by the factor
    # Return operations or 0 if not possible
    return operations if n == 1 else 0
