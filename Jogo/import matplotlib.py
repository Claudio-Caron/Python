import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
plt.title("Histograma de Probabilidade")
plt.xlabel("Valores")
plt.ylabel("Densidade")
plt.show()
