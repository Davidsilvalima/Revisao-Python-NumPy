import numpy as np
vetor1 = np.array([2, 4, 1])
vetor2 = np.array([1, 3, 2])
soma = vetor1+vetor2
print(soma)
soma = np.add(vetor1, vetor2)
print(soma)

sub = vetor1-vetor2
print(sub)
print(np.subtract(vetor1, vetor2))

print(vetor1/vetor2)
print(np.divide(vetor1, vetor2))

mult = vetor1*vetor2
print(mult)
print(np.multiply(vetor1, vetor2))

print(vetor1+1)
print(vetor1-1)
print(vetor1**2)
v = vetor1**2
print(v)
print(np.sqrt(v))

print(np.sin(vetor1))
print(np.log2(v))

matrix1 = np.array([[1, 2],[3, 4]])
matrix2 = np.array([[1, 1], [2, 2]])
print(matrix1)
print(matrix2)
print(matrix1.shape)
print(matrix1.ndim)
print(matrix1+matrix2)
print((4)*matrix1)

print(np.dot(matrix1, matrix2))
print(matrix2)
print(matrix1 @ matrix2)