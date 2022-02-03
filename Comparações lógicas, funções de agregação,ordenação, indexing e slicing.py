import numpy as np

a = np.array([10, 15, 20])
b = np.array([10, 18, 21])
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

c = np.array([1,1,1])
d = np.array([1,1,1])
print(np.array_equal(c,d))

# Funçao de agregação

vetor = np.arange(1, 21)
print(vetor)
print(vetor.sum())
print(sum(vetor))
print(vetor.min())
print(vetor.max())
print(vetor.mean())
print(np.median(vetor))
print(np.std(vetor))
print(np.var(vetor))

matrix = np.array([[2, 11, 15], [20, 21, 17], [90, 15, 13]])
print(matrix)

print(np.corrcoef(matrix))

#   Ordenando arrays
vetor = np.array([18, 15, 1, -3, 4])
print(vetor)
vetor.sort()
print(vetor)

# Subsetting, Slicing, Indexing

vetor = np.array([1, 2, 3])
print(vetor[2])
print(vetor[0])

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
print(matrix[0])
print(matrix[1])
print(matrix[1, 2])
print(matrix[1, 1])
print(vetor)
print(vetor[0:1])
print(vetor[0:2])

print(matrix)
print(matrix[0:2,1])
print(matrix[:2,1])
print(matrix[:, 1])

print(vetor[::-1])
print(vetor[-1])
print(vetor[-3])

print(vetor[vetor<2])
print(vetor[vetor>=2])
print(vetor[vetor>=2])

vetor1 = np.arange(1, 101)
print(vetor1)
print(vetor1[vetor1>50])

vetor2 = np.random.randint(1, 50, 50)
print(vetor2)
print(vetor2[vetor2>=30])