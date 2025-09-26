#!/usr/bin/env python
def Fibonacci(n):
    a = 0 
    b = 1

    # if n < 0 error
    if n < 0:
        print ("Error")
    # if n = 0 return 0
    elif n == 0:
        return 0
    # if n = 1 return 1
    elif n == 1:
        print (b, end=" ")
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
            print (b, end=" ")
        return b

print (Fibonacci(9))