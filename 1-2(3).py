import math

def f(x, t):
    z = math.sqrt((math.cos(x)**2 + math.sin(x)**2) / (35 * x * t))
    return z

t = 3
x = 1
z = f(x, t)
print(z)
