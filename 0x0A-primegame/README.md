# Prime Game

## Description

This project implements a competitive game between two players, Maria and Ben. Given a set of consecutive integers starting from 1 to `n`, the players take turns choosing a prime number and removing it and its multiples from the set. The player who cannot make a valid move loses the game.

Maria always goes first, and both players play optimally. The task is to determine who wins the most rounds out of `x` rounds of the game. If neither player wins more rounds than the other, the result is a tie.

## Requirements

- **Operating System**: Ubuntu 20.04 LTS
- **Programming Language**: Python 3.4.3+
- **Style**: PEP 8 (version 1.7.x)
- All files must be executable
- All your files should end with a new line
- Your code will be interpreted/compiled on Ubuntu 20.04 LTS using `python3`

## Prototype

The function signature is as follows:

```python
def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Parameters:
    x (int): The number of rounds.
    nums (List[int]): An array of integers where each element represents 'n' for that round.

    Returns:
    str: The name of the player who won the most rounds. If it's a tie, return None.
    """
```

## Game Rules

1. Maria and Ben take turns picking prime numbers from the set of consecutive integers from 1 to `n`.
2. The player picks a prime number and removes it along with all its multiples from the set.
3. The player who cannot make a valid move loses the round.
4. The game is repeated for `x` rounds, with different values of `n` for each round.
5. Maria always plays first.

## Example

```bash
$ cat main_0.py
#!/usr/bin/python3

isWinner = __import__('prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

$ ./main_0.py
Winner: Ben
```

### Explanation:

- Round 1 (`n = 2`): Maria wins.
- Round 2 (`n = 5`): Maria wins.
- Round 3 (`n = 1`): Ben wins.
- Round 4 (`n = 4`): Ben wins.
- Round 5 (`n = 3`): Ben wins.

The final result is `Ben` with the most wins.

## Algorithm

1. **Prime Number Calculation**: Use the Sieve of Eratosthenes to efficiently generate prime numbers up to the maximum `n` in the `nums` list.
2. **Game Simulation**: Simulate each game round by removing primes and their multiples, and track the winner of each round.
3. **Dynamic Programming**: Utilize a dynamic programming approach to optimize the prime number removal process and reduce redundant calculations.
4. **Determine Winner**: After all rounds are played, determine the overall winner based on who won the most rounds.

## Installation and Usage

1. Clone the repository:

   ```bash
   $ git clone https://github.com/WemaGoodness/alx-interview.git
   $ cd alx-interview/0x0A-primegame
   ```

2. Ensure the script is executable:

   ```bash
   chmod +x prime_game.py
   ```

3. Run the script:

   ```bash
   ./main_0.py
   ```

## Files

- `0-prime_game.py`: Contains the implementation of the `isWinner` function.
- `main_.py`: Example script to test the `isWinner` function.
- `README.md`: This file.

## Author

- [Goodness Wema](https://github.com/WemaGoodness)
