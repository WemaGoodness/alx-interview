#!/usr/bin/python3
"""
This module defines the prime game between two players, Maria and Ben.
The game is played with consecutive integers where primes and their
multiples are removed.
The winner is determined after multiple rounds, based on optimal strategy.
"""


def sieve_of_eratosthenes(n):
    """
    Generates a list of prime numbers up to a given number n using the Sieve
    of Eratosthenes algorithm.
    Args:
        n (int): The upper limit to generate prime numbers.
    Returns:
        list: A list of prime numbers up to n.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i, is_prime in enumerate(primes) if is_prime]


def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds, where both players
    play optimally.
    Args:
        x (int): The number of rounds to be played.
        nums (list of int): List containing the upper limit of numbers in each
        round.
    Returns:
        str: The name of the player who won the most rounds ("Maria" or "Ben").
             If there is no clear winner, returns None.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # dp stores the number of primes up to a certain number n
    dp = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        dp[i] = dp[i - 1] + (1 if i in primes else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if dp[n] % 2 == 1:  # Maria wins if there is an odd number of primes
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
