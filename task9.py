import numpy as np

s = input('შეიყვანეთ ფესები: ')
nums = s.split(',')
print(np.roots(nums))
