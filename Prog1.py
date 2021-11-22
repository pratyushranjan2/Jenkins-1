#!/usr/bin/python3
# Source code for summation of two numbers

def summation(data):
    return sum(data)

def factorial(n):
    if n < 0:
        return null
    f = 1
    for i in range(1,n+1):
        f *= i
    return f
