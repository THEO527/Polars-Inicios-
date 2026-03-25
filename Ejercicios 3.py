import numpy as np

print("Matrices de Rotacion")
theta = np.pi/6
R1 = np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])
print(R1)
theta = np.pi/4
R2 = np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])
print(R2)
theta = np.pi/3
R3 = np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])
print(R3)
print("Matrices Simetricas")
S1 = np.array([[1,2,3],[2,4,5],[3,5,6]])
S2 = np.array([[2,0,1],[0,3,4],[1,4,5]])
S3 = np.array([[5,1,2],[1,6,3],[2,3,7]])
print(S1)
print(S2)
print(S3)
print("Matrices Antisimetricas")
AS1 = np.array([[0,2,-3],[-2,0,4],[3,-4,0]])
AS2 = np.array([[0,1,-1],[-1,0,2],[1,-2,0]])
AS3 = np.array([[0,5,-2],[-5,0,3],[2,-3,0]])
print(AS1)
print(AS2)
print(AS3)
