#--------------------------------- Use of numpy.reshape --------------------------------
""""
import numpy as np

a = np.array([1,2,3,4,5,6,7,8])

b = np.reshape(a,(4,2))

c = np.reshape(a,(4,-1))

print(b)
print(c)

"""

# --------------------------------- Check All in the NumPy functions -------------------------------------

"""import numpy as np

a = np.array([1,2,3,4,5,6,7,8])
b = np.array([1,2,3,0])

status_a = np.all(a,axis=0)
status_b = np.all(b,axis=0)
print(status_a)
print(status_b)
"""

