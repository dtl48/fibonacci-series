#!/usr/bin/python
import sys

x = sys.argv[1]
z = int(x)


def add(a, b):  ## In this part I read that you add 2 things together.
    return a + b


def dothething(n):  ## I figured out that it was the fibonacci sequence
    ## in .L10 there was two subl on %eax
    ## It is recursive because dothething was called within itself
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 1000:
        print("input number over 1000!!!")
    else:
        return add(dothething(n - 1), dothething(n - 2))


def dothething2(n):  ## Dothething2 is my main which calls on dothething
    while n <= 199:  ## used the value 199 because n cannot go past 199
        print("Value:", dothething(n))  ## The main called on a print function
        break


y = dothething(z)
print(y)
