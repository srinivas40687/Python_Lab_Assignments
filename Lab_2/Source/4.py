import numpy as np
r = np.random.randint(low=0,high=20,size=15)
print("The random vector is",r)
c = np.bincount(r)
print("Most frequent item in the list is",np.argmax(c))
