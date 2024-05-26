def F(x):
    return 5.525+5.29*x-2.9*x**2+

a = float(input("дай a: "))
b = float(input("дай b: "))
eps = float(input("дай Eps: "))

while abs(b - a) > eps:
    x = (a + b) / 2
    if (F(x) == 0): break
    if (F(a) * F(x) > 0):
        a = x
    else:
        b = x

print('X = ', x)
print('F(X) = ', F(x))
