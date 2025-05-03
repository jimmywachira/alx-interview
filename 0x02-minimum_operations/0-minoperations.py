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
        int: The minimum number of operations, or 0 if n is impossible
             to achieve (n <= 1).
    """
    if n <= 1:
        return 0

    operations = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            operations += i
            n //= i
        i += 1

    if n > 1:
        operations += n

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

    n = 21
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 19170307
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 972
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 2147483640
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
