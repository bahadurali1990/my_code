""""# Numpy Broadcasting Exercise in Python
import numpy as np

A = np.array([1,
              2,
              3]
             )
B = np.array([2,3,4])

A_shape = A.shape
B_Shape = B.shape

print(A_shape)
print(B_Shape)

C=A+B
print(C)
"""
import numpy as np

#-------------------------------------------------------Polynomial-------------------------------------------
"""
import numpy as np

from numpy.polynomial import Polynomial

p = Polynomial([1,2,3,4,5,6])

print(p(2))
"""

# ------------------------------------------Numpy Copyto functions -----------------------------------------

"""import numpy as np

A = np.array([1,2,3,4,5,6])
B = np.zeros(6)
np.copyto(B,A,casting='unsafe')

print(A)
"""

#-------------------------------------- Find the shape and dimentions of Numpy array ----------------------

"""import numpy  as np

A = np.array([[1,2,3,4,5,6],[6,8,9,6,8,9]])
print(A.ndim)
print(A.shape)
"""

# ---------------------------------------------- Size of Numpy Array ----------------------------------------


B = np.array([
              [4,5],
              [6,7],
              [7,7]
              ]
             )

print(B.size)

Size_1 = np.size(B,axis=0)

print(Size_1)


