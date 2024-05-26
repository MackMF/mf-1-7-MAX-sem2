x = [7, 12, 2, 1, 8, 15, 12, 12, 7, 5, 9, 6]
y = [7, 11, 1, 1, 7, 15, 13, 12, 6.5, 5, 8, 6]
avg_x = sum(x) / len(x)
avg_y = sum(y) / len(y)
numerator = sum([(xi - avg_x) * (yi - avg_y) for xi, yi in zip(x, y)])
denominator = sum([(xi - avg_x) ** 2 for xi in x])

a = numerator / denominator
b = avg_y - a * avg_x
print(f"Коэффициент a: {a}")
print(f"Коэффициент b: {b}")
