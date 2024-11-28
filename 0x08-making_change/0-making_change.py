#!/usr/bin/python3
"""
Module to calculate the fewest number of coins needed to make a
specified total.

This module contains a function `makeChange` that implements a
dynamic programming approach to solve the coin change problem.
Given a list of coin denominations and a target total, it returns
the minimum number of coins required to achieve that total. If no
combination of coins can create the total, it returns -1.
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given total.

    Args:
        coins (list of int): List of coin denominations available.
        total (int): The target amount to achieve with the coins.

    Returns:
        int: The minimum number of coins needed to meet the total
             if possible, otherwise -1 if the total cannot be met
             with the given coins.
    """
    if total <= 0:
        return 0

    # Array to hold the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)

    # Base case: minimum coins needed to make the total of 0 is 0
    dp[0] = 0

    # Iterate through each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            # Check if the previous amount can be formed
            if dp[amount - coin] != float('inf'):
                # Update the minimum coins needed for the current amount
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If we still have infinity for total, it means it's not possible
    # to make that amount
    return dp[total] if dp[total] != float('inf') else -1
