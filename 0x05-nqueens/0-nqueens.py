#!/usr/bin/python3
"""
nqueens.py
A script to solve the N Queens problem using backtracking.
"""

import sys
from typing import List


def print_usage_and_exit() -> None:
    """Prints usage information and exits with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def print_error_and_exit(message: str) -> None:
    """Prints an error message and exits with status 1."""
    print(message)
    sys.exit(1)


def is_safe(board: List[int], row: int, col: int) -> bool:
    """
    Check if it's safe to place a queen at board[row][col].
    A position is safe if no other queen can attack from the left,
    top left diagonal, or bottom left diagonal.
    """
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_nqueens_util(N: int, board: List[int], col: int) -> None:
    """
    Utility function to solve the N Queens problem using backtracking.
    """
    if col >= N:
        print([[i, board[i]] for i in range(N)])
        return

    for i in range(N):
        if is_safe(board, i, col):
            board[col] = i
            solve_nqueens_util(N, board, col + 1)
            board[col] = -1  # Backtrack


def solve_nqueens(N: int) -> None:
    """
    Solves the N Queens problem and prints each solution.
    """
    board = [-1] * N
    solve_nqueens_util(N, board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error_and_exit("N must be a number")

    if N < 4:
        print_error_and_exit("N must be at least 4")

    solve_nqueens(N)
