#Find the set difference between 2 arrays

import numpy as np

a1 = [0, 10, 20, 40, 60, 80]
a2 = [10, 30, 40, 50, 70, 90]
print(np.setdiff1d(a1,a2))