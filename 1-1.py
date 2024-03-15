import math

def f(x, y):
    z = 5**(2*x*y) - x**5*x - math.e**(-x**2)
    return z

x = 0.3
y = 1
z = f(x, y)
print(z)
