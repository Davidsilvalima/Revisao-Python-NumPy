import numpy as np
vetor = np.array([10, 15 , 20, 30], dtype = float) #mudou de int32 para float64
print(vetor.shape)
print(len(vetor))
print(vetor.ndim)
print(vetor.size)
print(vetor.dtype)
vetor = vetor.astype(int)
print(vetor.dtype)
