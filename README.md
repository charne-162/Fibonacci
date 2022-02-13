# Fibonacci
## Various methods to display terms from the Fibonacci Sequence of numbers

The Fibonacci sequence is a sequence of numbers beginning with 0 and 1, in which every number is the sum of the two numbers preceeding it i.e 0,1,1,2,3,5,8,13,21,34 etc.

*Fibonacci_while_loop*

* A function is defined as: fib().
* User input is requested to indicate how many terms (including the first two terms, 0 and 1) of the Fibonacci Series they would like to see.
* Variables n1 and n2 are initialized to the first two numbers of the series: n1=0 and n2=1.
* The counter for the while loop is initialized: i = 0.
* Conditional statements are used to ensure that the user only enters positive integers:
If the user enters 0 or a number less than zero (recursive case), they are prompted to re-enter a number that is a positive integer.
The function fib() is called recursively until the user enters a positive integer.
When the user enters a positive integer, recursion will stop (base case).
* If the user enters 1, it means they want to see 1 term only which will be the first term, 0. The program will print 0.
* If the user enters a number greater than 1 (i.e 2 or higher), the while loop takes effect.
* While i is less than n (user input), the next term or new term will become the sum of n1 and n2.
* n1 which was previously 0, becomes the value of n2.
* n2 becomes the value of the next or new term.
* This happens until the while loop counter reaches the value of n and the n number of terms will be displayed.

*Fibonacci_for_loop*
* A function is defined as def fib().
* User input is requested to indicate how many terms (including the first two terms, 0 and 1) of the Fibonacci Series they would like to see.
* Variables a and b are initialized to the first two numbers of the series 0 and 1.
* Conditional statements are used to ensure that the user only enters positive integers. This is implemented with recursion in the same way as in the *Fibonacci_while_loop.*
* If the user enters 1, it means they want to see 1 term only, the first term, which is 0. The program will print 0.
* If the user enters a number greater than 1 (i.e 2 or higher), the for loop takes effect.
* For i in the range from 2 up to n: The sum of a and b is taken and stored into variable c. For every following iteration, the values are updated: a becomes b, b becomes c, c becomes the sum of new and b.

*Fibonacci _list*
* This follows the same procedure as the for loop and incorporates lists.
* The first two terms are added into a list.
* If the user enters a value greater than 1 (i.e 2 or greater) it will append all the following terms to the list containing the first two terms o and 1.

