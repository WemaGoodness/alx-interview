# 0x01. Lockboxes

This project contains a solution to the "Lockboxes" problem. The goal of the problem is to determine if all the boxes can be opened given a set of keys in each box. This solution uses graph traversal techniques to check if all boxes can be unlocked starting from the first box.

## Problem Description

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to other boxes. The first box `boxes[0]` is always unlocked.

### Prototype

```python
def canUnlockAll(boxes)
