#!/usr/bin/python3
"""
Calculates the fewest number of operations needed to result in exactly n H characters.
Only two operations are allowed: Copy All and Paste.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations to get n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations, or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    current_h = 1
    clipboard = 0

    while current_h < n:
        if clipboard == 0:
            # If clipboard is empty, we must copy
            clipboard = current_h
            operations += 1
        elif current_h < n // 2 + 1 and n % current_h == 0:
            # If we can reach n faster by multiplying the current count
            clipboard = current_h
            operations += 1
        elif clipboard > 0:
            # Paste
            current_h += clipboard
            operations += 1
        elif current_h == 1:
            # Should not reach here if n > 1
            return 0

    return operations


if __name__ == "__main__":
    n = 1
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 2
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 3
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 5
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 6
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 8
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 9
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 16
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
