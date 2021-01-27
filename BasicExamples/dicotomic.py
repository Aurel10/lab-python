from timeit import *


"""
this is a simple module that implements the dicotomic research
in two ways, recurive mode and iterative mode
keep attetion between python3 and python2 about integer division
"""


def binary_dic(value, start, end, A):
    if value > A[end] or value < A[start]:
        return -1
    if start > end:
        return -1

    med = (end + start) // 2

    if A[med] == value:
        return med
    elif A[med] < value:
        return binary_dic(value, med+1, end, A)
    elif A[med] > value:
        return binary_dic(value, start, med-1, A)
    return -1


def binary_dic_iter(A, value):
    if A[len(A)-1] < value or A[0] > value:
        return -1
    start, end = 0, len(A) - 1

    while start <= end:
        med = (end + start) // 2
        if A[med] == value:
            return med
        elif A[med] < value:
            start = med + 1
        elif A[med] > value:
            end = med - 1
    return -1


def main():
    A = [3, 4, 6, 14, 41, 98]
    value = 14
    start, end = 0, len(A) - 1

    print("recursive func, index = {}".format(
        binary_dic(value, start, end, A)))
    print("iterative func, index = {}".format(binary_dic_iter(A, value)))

    print("timer of recursive func ", timeit(
        lambda: binary_dic(value, start, end, A), number=100))
    print("timer of iterative func ", timeit(
        lambda: binary_dic_iter(A, value), number=100))


if __name__ == '__main__':
    main()
