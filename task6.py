import numpy as np

n1 = np.random.randint(0, 100, size=6)
n2 = np.random.randint(0, 100, size=9)
n3 = np.random.randint(0, 100, size=12)

print(np.concatenate((n1, n2, n3), axis=None))
