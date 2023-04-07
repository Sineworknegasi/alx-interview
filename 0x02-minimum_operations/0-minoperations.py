#!/usr/bin/python3
"""0-minoperations module"""


def minOperations(n):
        """
        minOperations
        Gets fewest # of operations needed to result in exactly n H characters
        """
        # all outputs should be at least 2 char: (min, Copy All => Paste)
    if n <= 1:
        return 0
    min_ops = 0
    i = 2

    while i <= n:
    #if n envenly divided by i
        if n % i == 0:
            min_ops += i
            n = n / i
        else:
            # Otherwise, we need to add one more H character to the file
            i += 1
    return min_ops
