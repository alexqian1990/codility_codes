#!/usr/bin/env python

"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.

Assume that:

N is an integer within the range [1..2,147,483,647].
Complexity:

expected worst-case time complexity is O(log(N));
expected worst-case space complexity is O(1).

"""


def compute_simpler(n):
    max_zero_count = 0
    current_zero_count = 0
    while n % 2 == 0 and n > 0:
        n //= 2
    while n > 0:
        res = n % 2
        n //= 2
        if res == 0:
            current_zero_count += 1
        else:
            max_zero_count = current_zero_count if current_zero_count > max_zero_count \
                else max_zero_count
            current_zero_count = 0
    return max_zero_count


def compute(n):
    residual = 0
    quotien = n
    max_zero_count = 0
    current_zero_count = 0
    while residual == 0 and quotien > 0:
        residual = quotien % 2
        # use
        quotien = quotien // 2
        # instead of (old version of code, not good)
        # quotien = (quotien - residual) / 2
    while quotien > 0:
        residual = quotien % 2
        quotien = quotien // 2
        # quotien = (quotien - residual) / 2

        if residual == 0:
            current_zero_count += 1
        else:
            if current_zero_count > max_zero_count:
                max_zero_count = current_zero_count
            current_zero_count = 0
    return max_zero_count
