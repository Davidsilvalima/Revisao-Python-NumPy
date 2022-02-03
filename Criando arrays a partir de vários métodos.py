import numpy as np

###   criando arrays

vetor = np.array([1, 2, 3, 4, 5, 6])
print(vetor)
print(type(vetor))

vetor2 = np.array((1,2,3,4,5))
print(vetor2)
print(type(vetor2))

matrix = np.array([[10, 15, 20], [25, 30, 35], [40, 45, 50]], dtype= float)
print(matrix)

###   range(start, stop, step)

a = range(1, 20)
print(type(a))
print(a.start)
print(a.step)
print(a.stop)
print(list(range(1,  20)))
print(list(range(1,  21)))   #list pode adicionar e remover elementos
print(tuple(range(1, 21)))   #tuple não pode

print(np.arange(1, 21, 0.2))

print(np.zeros(10))
print(np.zeros(shape=(3, 3)))

print(np.ones(10))
print(np.ones(shape=(3, 3)))
print(np.ones(shape=(10, 10)))

print(np.identity(3))
print(np.eye(3))

print(np.full(10, 5))
print(np.full(shape=(10,5), fill_value=15))

print(np.empty((3, 2)))
