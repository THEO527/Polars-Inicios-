import numpy as np

print("Determinantes por funcion")
M1 = np.array([[2,1,3],[1,0,2],[4,1,8]])
print(np.linalg.det(M1))
M2 = np.array([[1,2,3],[0,1,4],[5,6,0]])
print(np.linalg.det(M2))
M3 = np.array([[4,1,2],[1,3,0],[2,0,5]])
eigvals, eigvecs = np.linalg.eig(M3)
print(np.prod(eigvals))
