#!/usr/bin/env python3
"""
Module to calculate the minimum number of operations to get exactly `n`
H characters in a text file
"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to result in exactly `n`
    H characters.
    :param n: int, number of H characters required
    :return: int, minimum number of operations required to achieve `n`
    H characters
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations


# Testing
if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))
