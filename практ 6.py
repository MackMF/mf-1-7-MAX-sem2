m = 6 
A = [1, 2, 3, 4, 5, 6][:m]  
B = [10, 20, 30, 40, 50, 60][:m]  

C = []
for i in range(m):
    C.extend([A[i], B[i]])

print("Массив A:", A)
print("Массив B:", B)
print("Сформированный массив C:", C)