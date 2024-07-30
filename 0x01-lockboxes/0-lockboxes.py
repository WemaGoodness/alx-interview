#!/usr/bin/python3

def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
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
