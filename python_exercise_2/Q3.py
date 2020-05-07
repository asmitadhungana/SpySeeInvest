from math import sin, pi, exp
from numpy import linspace, array

n = 20
x = linspace(0, pi, n+1)
h = (pi-0)/n
y = list()
for i in x:
    y.append(sin(i)/exp(i))
y_temp = y[1:-1]
y, y_temp = array(y), array(y_temp)
sum = 0
for i in y_temp:
    sum+= 2*i
I = h/2 * (y[0] + sum + y[-1])
print(I)
