#!/usr/bin/env python

"""
A zero-indexed array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is also moved to the first place.

For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]. The goal is to rotate array A K times; that is, each element of A will be shifted to the right by K indexes.

Write a function:

class Solution { public int[] solution(int[] A, int K); }

that, given a zero-indexed array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given array A = [3, 8, 9, 7, 6] and K = 3, the function should return [9, 7, 6, 3, 8].

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""


def rotate(arr, k):
    # note the len(arr) = 0 case
    if len(arr) == 0:
        return arr
    newarr = [0] * len(arr)
    for i in range(len(arr)):
        newarr[(i - 1 + k) % len(arr)] = arr[i-1]
    return newarr


def rotate2(arr, k):
    # write your code in Python 2.7
    if len(arr) == 0:
        return arr

    k %= len(arr)

    # -k will access the value at len(arr) - 1 - k
    return arr[-k:] + arr[:-k]
