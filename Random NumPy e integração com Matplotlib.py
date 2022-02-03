import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# !pip3 install numpy
# !pip3 install pandas
# !pip3 install matplotlib
np.random.seed(20)
n = 30
vetor = np.random.randint(low = 1, high = 150, size = 30).reshape(-1, 1)
print(vetor)
print(vetor.shape)
print(vetor.min())
print(vetor.max())
print(vetor.mean())
print(vetor)

n1 = 100
matrix = np.random.randint(low = 50, high= 2500, size= (n1, 5))
colunas = list('ABCDE')
df = pd.DataFrame(matrix, columns = colunas, index = range(1, n1+1))
print(df.head(10))
figure(figsize= (12, 4))
df['A'].plot(color = 'black', lw = 1.3, marker = 'o', markersize = 3) #linestyle = '--',
xlabel('Eixo X')
ylabel('Eixo Y')
title('Series', fontsize = 20, pad = 15)
grid(alpha = 0.5, linestyle ='--')
# plt.show() foi substituido pelo acima;


