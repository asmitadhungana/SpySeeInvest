"""
Author: Saahil Mahato
Date: July 7, 2019 
"""

from math import exp
from pandas import DataFrame
from pandas import set_option

def f(x):
    return exp(x) - 4*x

def df(x):
    return x*exp(x) - 4

xList = list()
fxList = list()

def table(x, fx):
    xList.append(x)
    fxList.append(fx)

def newton_raphson(x):
    while True:
        table(x, f(x))
        if f(x) == 0.0:
            break 
        x = x - f(x)/df(x)
    print("The value of the root is:", x)

if __name__ == "__main__":
    x = 1.0
    newton_raphson(x)
    set_option("display.precision", 16)
    df = DataFrame()
    df['x']=xList
    df['f(x)']=fxList
    print(df)
