#!/usr/bin/python3
def minOperations(n):
    if n <= 1:
        # It's impossible to have fewer than 2 H characters
        return 0

    # Start with a single H character in the file
    file_contents = 'H'

    # Initialize the number of operations and the number of H characters in the file
    num_ops = 0
    num_h = 1

    while num_h < n:
        if n % num_h == 0:
            # If n is a multiple of the current number of H characters, we can copy and paste
            file_contents += file_contents
            num_ops += 1
            num_h *= 2
        else:
            # Otherwise, we need to add one more H character to the file
            file_contents += 'H'
            num_ops += 1
            num_h += 1

        if num_ops > n:
            # If the number of operations exceeds n, it's impossible to reach n H characters
            return 0

    return num_ops
