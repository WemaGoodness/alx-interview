#!/usr/bin/python3
"""
Module to solve the coin change problem using dynamic programming.
"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Determine the fewest number of coins needed to make up a given total
    amount.

    Args:
        coins (List[int]): List of coin denominations available.
        total (int): The total amount to be formed using the fewest number of
        coins.

    Returns:
        int: The fewest number of coins needed to meet the total.
             Returns 0 if total is 0 or less.
             Returns -1 if the total cannot be met with the given coin
             denominations.
    """
    if total <= 0:
        return 0

    # Create a list to store the minimum coins required for each amount up to
    # 'total'
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Zero coins are needed to make the total of 0

    # Loop through each coin
    for coin in coins:
        # Update the dp array for each amount from the coin's value to the
        # total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still float('inf'), it means it's not possible to form
    # 'total' with given coins
    return dp[total] if dp[total] != float('inf') else -1
