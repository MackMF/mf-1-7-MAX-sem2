def v(x, y):
    u = min(x+y, x-3*y) / max(x+6*y, x-y)
    print('нльзя')
    return u
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
z = min(x+y, x-3*y)
o = max(x+6*y, x-y)
result = v(x, y)
print(f"min(x+y, x-3y) = {z}")
print(f"max(x+6y, x-y) = {o}")
print(f"u = min(x+y, x-3y) / max(x+6y, x-y) = {result}")
