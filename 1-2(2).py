import math

def f(x, y):
    z = (x + 4) ** (1/3) - math.atan(x*y / 3*y+1)**2
    return z

y = 2
x = 2
z = f(x, y)
print(z)
