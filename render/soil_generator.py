import numpy as np
from game import Point, Triangle, Mesh

L = 10.
N = 10.
x_list = np.linspace(0, L, N)
z_list = np.linspace(0, L, N)
points_list = [[0]*N]*N

for i in range(len(points_list)):
    for j in range(len(points_list[0])):
        points_list[i][j] = Point(x_list[i], np.random.randint(4), z_list[j])

trigs_list = []
for i in range(len(points_list) - 1):
    for j in range(len(points_list[0]) - 1):
        temp1 = Triangle(
            points_list[i][j], points_list[i + 1][j], points_list[i][j + 1])
        temp2 = Triangle(
            points_list[i + 1][j], points_list[i][j + 1], points_list[i + 1][j + 1])
        trigs_list.extend((temp1, temp2))
