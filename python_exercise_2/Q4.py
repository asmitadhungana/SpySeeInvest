from math import exp, sqrt, pi
import numpy as np

n_divisions = 50

intervals = np.linspace(-4, 4, 51)
h = intervals[1] - intervals[0]

y = list()
for i in intervals:
    y.append(sqrt(1/(2*pi)) * exp(i**2/2))

odd_sum = np.sum(y[1:-1:2])
even_sum = np.sum(y[2:-1:2])
I = (h/3)*(y[0]+y[-1]+4*odd_sum+2*even_sum)

print(I)
