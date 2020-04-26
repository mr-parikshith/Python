"""
Coding Exam Question 11
Write a Python program to print the first 12 "even" Fibonacci numbers.

Assume Fibonacci numbers start from 1 and 1
"""

def EvenFibonacci(Number = 12):
    Fibonacci0 = 1
    Fibonacci1 = 1
    #Number = 12
    Fibonacci2 = Fibonacci1
    Fibonacci3 = Fibonacci0 + Fibonacci1
    while Fibonacci2 <= Number:
        Fibonacci3 = Fibonacci0 + Fibonacci1
        Fibonacci2 = Fibonacci1
        Fibonacci0 = Fibonacci1
        if Fibonacci2 % 2 == 0:
            print(Fibonacci2)
        Fibonacci1 = Fibonacci3

#Main starts here
EvenFibonacci()
