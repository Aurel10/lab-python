from timeit import *


"""
In this module are presents a different version of Fibonacci series calculations
There are many implementations from multiple recursion to use the dynamic programming approach
"""


def wrost_fib(n):
    if n <= 1:
        return 1

    return wrost_fib(n-1) + wrost_fib(n-2)


def tuple_fib(n):
    if n <= 1:
        return (0, n)

    b, a = tuple_fib(n-1)

    return (a, a+b)


def iterative_fib(n):
    if n <= 1:
        return 1

    a, b = 0, 1

    while n > 0:
        a, b = b, a+b
        n -= 1

    return b


def mem_fib(n):
    if n <= 1:
        return 1

    n += 2
    fib = [0] * n
    fib[0], fib[1] = 0, 1

    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]

    return fib[n-1]


def dynamic_fib(n):
    if n <= 1:
        return 1

    fib = [0] * 2
    fib[0], fib[1] = 0, 1

    for i in range(0, n):
        fib[0], fib[1] = fib[1], fib[1]+fib[0]

    return fib[1]


def main():
    N = 10

    print("wrost_fib ", wrost_fib(N))
    print("tuple_fib ", tuple_fib(N))
    print("iterative fib ", iterative_fib(N))
    print("mem fib ", mem_fib(N))
    print("dynamic_fib ", dynamic_fib(N))

    print("wrost_fib of timer = ", timeit(
        lambda: wrost_fib(N), number=100))
    print("tuple_fib of timer = ", timeit(
        lambda: tuple_fib(N), number=100))
    print("iterative_fib of timer = ", timeit(
        lambda: iterative_fib(N), number=100))
    print("mem_fib of timer = ", timeit(
        lambda: mem_fib(N), number=100))
    print("dynamic_fib of timer = ", timeit(
        lambda: dynamic_fib(N), number=100))


if __name__ == '__main__':
    main()
