#!/usr/bin/python3

"""
text editor that can execute only two operations 
in this file: Copy All and Paste.
"""


def minOperations(n):
    """
    returns minimum operations
    """
    result = 0
    index = 2
    if n < 2:
        return 0
    while (index < n + 1):
        while n % index == 0:
            result += index
            n /= index
        index += 1
    return result
