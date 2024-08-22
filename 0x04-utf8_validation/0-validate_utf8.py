#!/usr/bin/env python3
"""
This module provides a function to validate whether a data set represents
a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Parameters:
    data (list): A list of integers representing bytes of data.
    Returns:
    bool: True if the data is a valid UTF-8 encoding, otherwise False.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        # Get the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Count the number of leading 1's
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # 1 byte character
            if num_bytes == 0:
                continue

            # For 2, 3, or 4 byte character
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
