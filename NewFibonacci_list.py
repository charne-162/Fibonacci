# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 10:29:39 2022

@author: charn
"""

#define function for fibonaci series
def fib():
    #Request user input
    n = int(input("How many terms of the Fibonacci series would you like to see? \n"))
    # initialize list with oth and 1st indices (taking 0 and 1 as the first 2 terms)
    f_list = [0,1]
    if n < 1:
        #If user enters 0 or negative value - it is invalid.
        #Use recursion to call function again until user enters positive integer
        print("Invalid input.Cannot have zero or negative number of numbers.Please enter a positive integer.\n ")
        fib()
    #Else If user inputs 1 then print the first number only which is a = 0
    elif n == 1:
        print(f_list[0])
    else:
        for i in range (2, n+1):
            f_list.append(f_list[i-1] + f_list[i-2])
        return f_list

    
series = fib()
print("Fibonacci Series:")
print(series)
         
        