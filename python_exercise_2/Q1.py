"""
Author: Saahil Mahato
Date: July 7, 2019 
"""

from math import sin
from pandas import DataFrame
from pandas import set_option


def f(x):
    return x**2 - sin(x)


lista=[]
listb=[]
listxo=[]
listfxo=[]


def table(a,b,c,d):
    lista.append(a)
    listb.append(b)
    listxo.append(c)
    listfxo.append(d)


def bisection_method(a, b):
    if f(a)*f(b) > 0.0:
        print("Please choose alternate values for a and b.")
    else:
        while f(a)*f(b) < 0.0:
            c = (a+b)/2
            table(a,b,c,f(c))
            if f(c) == 0.0:
                break
            elif f(c)*f(a) < 0.0:
                b = c
            else:
                a = c
    print("The value of root is:", c)


if __name__ == "__main__":
    a = 0.5
    b = 1.0
    bisection_method(a,b)
    set_option("display.precision", 25)
    df = DataFrame()
    df['a'] = lista
    df['b'] = listb
    df['xo'] = listxo
    df['f(xo)'] = listfxo
    print(df)