#!/usr/bin/python3
"""0-minoperations module
"""
def minOperations(n):
    """Calculate the fewest number of operations needed to result in exactly n H characters in the file.
    Args:
        n (int): Number of H characters
    Returns:
        int: Minimum number of operations needed
    """
    if n <= 1:
        # It's impossible to have fewer than 2 H characters
        return 0
    # Initialize the number of operations and the number of H characters in the file
    min_ops = 0
    i = 2

    while i <= n:
        if n % i == 0:
            # If n is a multiple of the current number of H characters, we can copy and paste
            min_ops += i
            n = n / i
        else:
            # Otherwise, we need to add one more H character to the file
            i += 1
    return min_ops
