import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

array = np.random.normal(10, 0.5, size=50)
print(array)
sns.histplot(array)
print(array)