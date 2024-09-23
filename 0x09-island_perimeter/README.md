# Island Perimeter

This project involves calculating the perimeter of an island in a grid. The grid is represented by a 2D array of integers where `0` represents water and `1` represents land. The goal is to determine the perimeter of the island.

## Requirements

- Python 3.4.3
- PEP 8 style (version 1.7)
- No external modules allowed

## Usage

To use the `island_perimeter` function, import it and pass a grid as an argument:

```python
from 0-island_perimeter import island_perimeter

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(island_perimeter(grid))
```
```
# Output: 12
```
