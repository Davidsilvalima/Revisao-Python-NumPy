import numpy as np
matrix = np.array([[1, 2, 4], [26, 27, 29],[11, 17, 18]])
print(matrix)
print(matrix.T)
print(matrix.shape)

matrix1 = np.array([[1, 1], [2, 0], [1, 5]])
print(matrix1)
print(matrix1.shape)
print(matrix1.T)
print(matrix1.T.shape)

vetor = matrix1.ravel()
print(vetor)
print(vetor.shape)
vetor.shape = (6, 1)
print(vetor)

vetor = np.array([[1], [1], [2], [0], [1], [5]])
print(vetor)
vetor = np.array([1, 1, 2, 0, 1, 5])
print(vetor)

vetor = vetor.reshape((6, 1))
print(vetor)

vetor = np.arange(1, 51).reshape((50, 1))
print(vetor)

vetor = np.arange(1, 11).reshape(-1,1)
print(vetor)

vetor2 = np.arange(11, 21).reshape(-1, 1)
print(vetor2)
v = np.append(vetor, vetor2).reshape(-1, 1)
v = np.insert(v, 0, 0).reshape(-1,1)
print(v)