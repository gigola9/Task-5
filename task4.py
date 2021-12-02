import numpy as np

a = np.random.randint(0, 100, size=36)
print(a)

n = int(input('შეიყვანეთ რიცხვი: '))

all = np.array([i / n for i in a])
print(all)
print('-----------')
newa = np.array([int(i/n) for i in a if i % n == 0])
print(newa)
