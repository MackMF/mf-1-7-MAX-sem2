
def f(x):
    return 2*x**4 - 8*x**3 - 9*x**2 + 14*x - 1
z = float(1000)
v = float(1000)
for x in range(-5, 6):
    y = f(x)
    if y > z:
        z = y
    if y < v:
        v = y
print(f"Наибольшее значение функции f(x) на отрезке [-5, 5]: {z}")
print(f"Наименьшее значение функции f(x) на отрезке [-5, 5]: {v}")