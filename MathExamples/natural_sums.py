
"""
this is a simple module that provides three methods to calculate the natural summations about
the natural number from 1 to n (Gauss Sum)
odds number from 1 to n (odds_numbers ** 2)
even number from 1 to n (even_numbers * (even_numbers + 1))
These method helps to reduce the complexity because they avoid using the loops
"""


def sum_of_numbers(n):
    return n * (n + 1) // 2


def sum_of_odds_number(n_odds):
    return n_odds ** 2


def sum_of_even_numbers(n_even):
    return n_even * (n_even + 1)


def check_of_n(n):
    if n % 2 == 0:
        return True
    return False


def main():
    n = 10000001

    if (not check_of_n(n)):
        n_odds = (n // 2) + 1
    else:
        n_odds = n // 2
    n_even = n // 2

    print("Gauss Sum = {}".format(\
        sum_of_numbers(n)
    ))
    
    print("odds numbers summation = {}".format(\
        sum_of_odds_number(n_odds),
    ))

    print("even numbers summation = {}".format(\
        sum_of_even_numbers(n_even)
    ))


if __name__ == '__main__':
    main()
