#!/usr/bin/python3
"""
This module contains the implementation of the function minOperations()
which calculates the minimum number of operations needed to produce
exactly n H characters in a text file using only the
operations Copy All and Paste.
"""

"""
To solve the problem of determining the minimum number of operations
needed to produce exactly n H characters using only the operations
"Copy All" and "Paste", we can use a mathematical approach based
on the factors of n. The key here is to realize that every time you use
"Copy All", you effectively double your current characters
(depending on how many times you "Paste" after that).

Explanation:
Understanding Operations:

The first action must always be a "Copy All" after you have at
least one character, which can only be done once at the start.
Each "Paste" operation adds the current number of characters to
the total character count.
Our goal is to determine the minimal sequence of these operations
that leads us to exactly n H characters.
Using Factors:

If n is divisible by k, where k is the number of Hs currently in
the file, that means you can perform "Copy All" when you
have k Hs, and then perform "Paste" (n/k - 1) times to reach n.
The optimal way to reach n is by breaking it down into smaller
factors, which can lead to fewer operations.
Implementation:
The basic idea is to find the factors of n and use them
recursively to count the operations required.
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
