# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 13:28:40 2022

@author: charn
"""
def fib():
    n = int(input("How many terms of the Fibonacci series would you like to see? \n"))
    #starting with first two numbers as 0 and 1
    n1, n2 = 0,1
    #initialise counter
    i = 0
    if n <= 0:
        print("Invalid input.Cannot have zero or negative term. Please enter a positive integer.\n")
        fib()
    elif n == 1:
        print("Here is the first term of the fibonacci series:")
        print(n1)
    else:
        print("\nFibonacci series:6")
        while i < n:
            print(n1)
            n_New = n1 + n2
            n1 = n2
            n2 = n_New
            i +=1
fib()