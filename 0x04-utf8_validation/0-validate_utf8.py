#!/usr/bin/python3
"""
Module to check if a given data set represents a valid UTF-8 encoding.

This module contains a function, validUTF8, that verifies if a list of integers
represents bytes that form a valid UTF-8 encoded character.

Each integer in the list represents one byte (the least significant 8 bits).
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Parameters:
    data (list of int): List of integers representing bytes of data.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for byte in data:
        # Get the last 8 bits of the integer
        byte &= 0xFF

        # Check how many leading 1's are there
        if num_bytes == 0:
            if (byte >> 5) == 0b110:      # 2 bytes
                num_bytes = 1
            elif (byte >> 4) == 0b1110:   # 3 bytes
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4 bytes
                num_bytes = 3
            elif (byte >> 7) == 0:        # 1 byte
                continue
            else:                         # Invalid byte
                return False
        else:
            # This should be a continuation byte
            if (byte >> 6) != 0b10:       # Check if it starts with '10'
                return False
            num_bytes -= 1

    return num_bytes == 0  # Check if any bytes are left unprocessed
