from timeit import *
from random import *


"""
this is a simple module to find commom element on two arrays
to calculate the time execution is use the timeit module and lambda function
every time are trasformed into second
"""


def find_element_one(A, B):

    for i in range(0, len(A)):
        for j in range(0, len(B)):
            if A[i] == B[j]:
                return True

    return False


def find_element_two(A, B):
    dict_first = {}

    for i in range(0, len(A)):
        dict_first[A[i]] = 1

    for i in range(0, len(B)):
        if B[i] in dict_first.keys():
            return True

    return False


def find_element_three(A, B):
    if any(value in B for value in A):
        return True
    return False


def find_element_four(A, B):
    return bool(set(A) & set(B))


def find_element_five(A, B):
    for value in A:
        if value in B:
            return True
    return False


def main():
    A = [chr(randrange(97, 123)) for x in range(0, 1000000)]
    B = [chr(randrange(97, 123)) for x in range(0, 100)]

    print("find element one", find_element_one(A, B))
    print("find element_two", find_element_two(A, B))
    print("find element_three", find_element_three(A, B))
    print("find element_four", find_element_four(A, B))
    print("find element_five", find_element_five(A, B))

    print("timer of find element one", timeit(
        lambda: find_element_one(A, B), number=100))
    print("timer of find element two", timeit(
        lambda: find_element_two(A, B), number=100))
    print("timer of find element three", timeit(
        lambda: find_element_three(A, B), number=100))
    print("timer of find element four", timeit(
        lambda: find_element_four(A, B), number=100))
    print("timer of find element five", timeit(
        lambda: find_element_five(A, B), number=100))


if __name__ == '__main__':
    main()
