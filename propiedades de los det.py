import numpy as np

A = np.array([[1,2,3],[0,1,4],[5,6,0]])
B = np.array([[2,0,0],[0,2,0],[0,0,2]])
print(np.linalg.det(A.T), np.linalg.det(A))
print(np.linalg.det(np.dot(A,B)), np.linalg.det(A)*np.linalg.det(B))
C = np.array([[1,2,3],[2,4,6],[3,6,9]])
print(np.linalg.det(C))
D = A.copy()
D[0] = 3*D[0]
print(np.linalg.det(D))
E = A.copy()
E[[0,1]] = E[[1,0]]
print(np.linalg.det(E))
T = np.array([[2,0,0],[0,3,0],[0,0,4]])
print(np.linalg.det(T), 2*3*4)
I = np.eye(3)
print(np.linalg.det(I))
print(np.linalg.det(np.linalg.inv(A)), 1/np.linalg.det(A))
F = np.array([[1,2,3],[1+2,2+4,3+6],[3,6,9]])
print(np.linalg.det(F))
