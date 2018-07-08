import numpy as np

a = np.array([[0,1], [2,1]])
b = np.array([[1,1], [0, 2]])

c = np.array([[6,3,2], [2,3,1]])
d = np.array([[2,2], [2,1], [1,1]])

result = a.dot(b)
print(result)

result_2 = c.dot(d)
print(result_2)


