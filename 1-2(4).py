import math

def f(x, y):
    z = (abs(x)+1)/(3*2) + (math.e**(-3*x)-0.4) / (5+7*y)
    return z

y = 3
x = 3
z = f(x, y)
print(z)
