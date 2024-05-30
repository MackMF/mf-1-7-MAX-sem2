import numpy as np 
B = np.array([[4, 1, 2], [0, 4, 3], [1, 1, 1]])
r = np.array([[-0.7], [1.3], [0.2]])
q = np.array([[-1.6], [0.8], [1.1]])
p = np.array([[0.1], [1.7], [-1.5]])

naillox = sum((B[i] * (r[i] - q[i]) * p[i] for i in range(3)))

print("Скалярное произведение векторов:", naillox)

###
import numpy as np

A = np.array([[1, 2, 3], [1, 2, 1], [3, 2, 0]])

B = np.array([[4, 2, 1], [0, 4, 3], [1, 1, 1]])

p = np.array([1.7, 0.8, 1.3])

q = np.array([0.1, -1.6, -0.7])

r = np.array([-1.5, 1.1, 0.2])

s = np.dot(np.dot(B, r - q), p)

print(s)
###
A=input(‘Введите матрицу A=’);
b=input(‘Введите вектор b=’);
n=length(b);
disp(‘Матрицакоэффициентов СЛАУ (Матрица A)›);
for i=1:n
fprintf(‘%6.2f’,A(i,:));
fprintf(‘\n’);
end
disp(‘Вектор правых частей СЛАУ (Вектор b)’);
fprintf(‘%12.4f \n’,b)
d=det(A);
disp(‘Oпределитель матрицы A’);
fprintf(‘%12.4f \n’,d);
Ainv=inv(A);
disp(‘Обратная матрица’);
for i=1:n(1)
fprintf(‘%12.4g’,Ainv(i,:));
fprintf(‘\n’);
end
x=A\b;
disp(‘Решение СЛАУ (Вектор x)’);
fprintf(‘%12.4f \n’,x)
