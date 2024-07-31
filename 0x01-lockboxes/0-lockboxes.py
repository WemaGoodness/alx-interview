#!/usr/bin/python3
"""
This module contains the function `can_unlock_all` which determines
if all boxes can be unlocked given a list of lists where each list
represents a box and contains keys to other boxes.
"""

def can_unlock_all(boxes):
    """
    Determines if all the boxes can be opened.

    Parameters:
    boxes (list of lists): A list of lists where each sublist represents
                           a box and contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, otherwise False.
    """
    if not boxes:
        return False

    n = len(boxes)
    opened_boxes = set()
    keys = set([0])

    while keys:
        current_key = keys.pop()
        if current_key not in opened_boxes:
            opened_boxes.add(current_key)
            for key in boxes[current_key]:
                if key < n:
                    keys.add(key)

    return len(opened_boxes) == n
