from entities import Point, Triangle
import numpy as np
import math


def generate():
    L = 3.
    N = 20
    x_list = np.linspace(0, L, N)
    z_list = np.linspace(0, L, N)
    points_list = [[0]*N for i in range(N)]

    phase_x = np.random.random()*2*np.pi
    phase_z = np.random.random()*2*np.pi

    for i in range(len(points_list)):
        for j in range(len(points_list[0])):
            points_list[i][j] = Point(x_list[i], math.sin(x_list[i]*2*np.pi/L + phase_x)*math.cos(
                z_list[j]*2*np.pi/L+phase_z)*0.3 + np.random.random()*0.1, z_list[j])

    trigs_list = []
    for i in range(len(points_list) - 1):
        for j in range(len(points_list[0]) - 1):
            temp1 = Triangle(
                points_list[i][j], points_list[i + 1][j], points_list[i][j + 1])
            temp2 = Triangle(
                points_list[i + 1][j], points_list[i][j + 1], points_list[i + 1][j + 1])
            trigs_list.extend((temp1, temp2))
    return trigs_list
