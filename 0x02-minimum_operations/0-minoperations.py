#!/usr/bin/python3
"""0-minoperations module
"""
  def minOperations(n):
        """Calculate the fewest number of operations needed to result in exactly
        
        
        Args:
        n (int): Number of H characters
        
        Returns:
        int: Minimum number of operations needed
    """
    if n <= 1:
        # It's impossible to have fewer than 2 H characters
        return 0
    min_ops = 0
    i = 2

    while i <= n:
        if n % i == 0:
            min_ops += i
            n = n / i
        else:
            # Otherwise, we need to add one more H character to the file
            i += 1
    return min_ops
