#!/usr/bin/python3
"""
Prime Game Module

This module defines a function `isWinner` that determines the winner of a
prime-based game played between Maria and Ben. In this game, players
alternately pick prime numbers from a set of consecutive integers, removing
the chosen prime and its multiples until no moves are possible.

Players always play optimally, and Maria always goes first. The function
determines the winner of multiple rounds and returns the name of the
player who wins the most rounds. If neither player wins the majority, the
function returns None.

The module does not use any imported libraries and supports efficient
calculation for inputs with n and x up to 10,000.

Example:
    x = 3, nums = [4, 5, 1]
    result = isWinner(x, nums)  # Output: 'Maria'
"""


def isWinner(x, nums):
    """
    Determine the winner of multiple rounds of the prime game.

    Args:
        x (int): The number of rounds to be played.
        nums (list): A list of integers, where each integer represents the
                     size of the set of consecutive integers for a round.

    Returns:
        str: The name of the player who won the most rounds ('Maria' or 'Ben').
             If there is no clear winner, return None.
    """
    def sieve(n):
        """Helper function to generate a list indicating primes up to n."""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return is_prime

    # Determine the largest value in nums for precomputation
    max_n = max(nums)
    prime_flags = sieve(max_n)

    # Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if prime_flags[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Evaluate each round
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
