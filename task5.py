import numpy as np

n1 = np.random.randint(0, 100, size=[5, 3])
print(n1)
n2 = np.random.randint(0, 100, size=[3, 2])
print(n2)

print(np.matmul(n1, n2))
