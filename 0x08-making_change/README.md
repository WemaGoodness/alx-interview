# Coin Change Problem - Dynamic Programming Approach 🪙

## Introduction 📋
This project tackles the classic **Coin Change Problem** using dynamic programming. The goal is to find the minimum number of coins required to make up a given total amount using a set of coin denominations. The problem tests algorithmic skills, particularly the use of dynamic programming to optimize solutions.

## Concepts Covered 🌐
- **Greedy Algorithms:** Understanding their limitations for this problem.
- **Dynamic Programming:** Breaking down problems into manageable sub-problems to achieve an optimal solution.
- **Algorithmic Complexity:** Evaluating time and space complexity to ensure efficiency.
- **Python Programming:** Leveraging type annotations, list comprehensions, and conditional statements.


## Requirements 🛠️
- All files are interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.4.3**.
- Code follows the `pycodestyle` style guide (version 2.5.*).
- Each module and function is documented appropriately, explaining its purpose and usage.
- All functions are type-annotated.
- Files are executable and comply with PEP 8 standards.

## Usage 🚀
### makeChange Function
- **Prototype:** `def makeChange(coins: List[int], total: int) -> int`
- **Parameters:**
  - `coins` (List[int]): List of available coin denominations (positive integers).
  - `total` (int): The target amount to form using the fewest number of coins.
- **Returns:**
  - The fewest number of coins needed to meet the total.
  - `0` if the total is `0` or less.
  - `-1` if the total cannot be met with the given coin denominations.

### Example
To run the function with sample inputs:

```py
#!/usr/bin/python3
from 0-making_change import makeChange

if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```
