#!/usr/bin/python3
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
    # Number of bytes remaining in the current UTF-8 character sequence
    num_bytes = 0

    # Masks to check the significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Extract the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Count the number of leading 1 bits in the first byte
            if (byte & mask1) == 0:
                # 1-byte character
                continue

            # Determine the number of bytes in the UTF-8 character
            while (byte & mask1):
                num_bytes += 1
                byte <<= 1

            # UTF-8 characters are only valid with 2 to 4 bytes
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the subsequent byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease the number of bytes to check
        num_bytes -= 1

    # If all characters were valid, num_bytes should be 0
    return num_bytes == 0
