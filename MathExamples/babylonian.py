from timeit import *
from math import *


"""
This is a module that implements an approximation about square root functions. 
There are three versions about the square root calculation, Babylonian method, 
math library of python and simple python calculation using operator **
"""


def babylonian_sqrt(value):
	prev_1 = prev_2 = 0.0
	approx = 1.0

	while (approx != prev_1 and approx != prev_2):
		prev_1 = prev_2
		prev_2 = approx
		approx += (value / approx)
		approx /= 2
	
	return approx


def main():
	N = 1100000000044141051194814197418974197419714
	
	print("radix of {0} is = {1} ".format(N, babylonian_sqrt(N)))
	print("radix of {0} is = {1} ".format(N, sqrt(N)))	
	print("radix of {0} is = {1} ".format(N, N ** 0.5))

	print("time execution of Babylonian method is = {}".format(
		timeit(lambda : babylonian_sqrt(N), number=100)))
	print("time execution square root math library function is = {}".format(
		timeit(lambda : sqrt(N), number=100)))
	print("time execution square root python operation ** is = {} ".format(
		timeit(lambda : N ** 0.5, number=100)))

if __name__ == '__main__':
	main()
