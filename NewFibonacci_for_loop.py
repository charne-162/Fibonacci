# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 07:49:44 2022

@author: charn

Fibonoci series - Ask user how many terms of the Fibonaci series they would like to see
Taking frst two terms as 0 and 1
Using a for loop
"""

#define function for fibonaci series
def fib():
    #Request user input
    n = int(input("How many terms of the Fibonacci series would you like to see? \n"))
    #initialize variables to the first 2 terms of the series: o and 1
    a = 0
    b = 1
    #If user enters 0 or negative value - it is invalid.
    #Use recursion to call function again until user enters positive integer
    if n <= 0:
        print("Invalid input.Cannot have zero or negative term. Please enter a positive integer.\n")
        fib()
        #If user inputs 1 then print the first number only which is a = 0
    elif n == 1: 
        print("Here is the first term of the fibonacci series:")
        print(a)
    else:
        print("\nFibonacci series:")
        print(a)
        print(b)
        for i in range (2,n): 
            # After taking the sum of a and b;
            # store the sum of a and b in variable c;
            # for next iteration update values: a becomes b; b becomes c;
            # for next iteration c will be the sum of new a and b
            c = a + b
            a = b
            b = c
            print(c)
fib()

         
        
        