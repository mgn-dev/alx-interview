#!/usr/bin/env python3
"""
Prime Game Module

This module defines the `isWinner` function to determine the winner of
a prime-based game between Maria and Ben. In this game, players alternately
pick prime numbers from a set of consecutive integers, removing the chosen
prime and its multiples until no moves are possible.

Maria always goes first, and both players play optimally. The function
evaluates multiple rounds and returns the name of the player who wins the
most rounds. If neither player wins the majority, it returns None.

Example:
    x = 3
    nums = [4, 5, 1]
    result = isWinner(x, nums)  # Output: 'Maria'
"""


def isWinner(x, nums):
    """
    Determine the winner of multiple rounds of the prime game.

    Args:
        x (int): The number of rounds to play.
        nums (list): A list of integers, where each integer `n` represents
                     the size of the set of consecutive integers for a round.

    Returns:
        str: The name of the player who won the most rounds:
             - 'Maria' if Maria wins the majority.
             - 'Ben' if Ben wins the majority.
             - None if neither player wins the majority.
    """
    # Edge case: No rounds to play
    if x == 0 or not nums:
        return None

    def sieve(n):
        """
        Generate a list indicating prime numbers up to `n`.

        Args:
            n (int): The upper limit for prime number calculation.

        Returns:
            list: A boolean list where `True` indicates a prime number.
        """
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
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
        if n < 1:
            # Ben wins by default since Maria cannot start
            ben_wins += 1
            continue

        # Maria wins if the count of primes is odd; otherwise, Ben wins
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
