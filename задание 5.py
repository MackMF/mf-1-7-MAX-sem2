def uk(x, k):
    return (-1)**(k) * (x**k / (2*k+1)**2)

def calculate_sum(x, n):
    total_sum = 0
    for k in range(1, n+1):
        total_sum += uk(x, k)
    return total_sum

x_values = [0.1, 0.3, 0.4, 0.7, 1.0]
n = 10

print("|   x   |    S    |")
print("-------------------")
for x in x_values:
    result = calculate_sum(x, n)
    print(f"| {x}  |  {result:.6f} |")
print("-------------------")