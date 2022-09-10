from entities import Point, Triangle
import math
import numpy as np


def generate():
    R = 1

    theta_min = 0
    theta_max = 2*math.pi

    phi_min = 0.1
    phi_max = math.pi - 0.1

    N = 20
    theta_list = np.linspace(theta_min, theta_max, 2*N, endpoint=False)
    phi_list = np.linspace(phi_min, phi_max, N, endpoint=True)

    coords_spheric = [[(theta, phi) for phi in phi_list]
                      for theta in theta_list]
    coords_cart = [[(R*math.cos(entry[0])*math.sin(entry[1]), R*math.sin(entry[0]) *
                    math.sin(entry[1]), R*math.cos(entry[1])) for entry in row] for row in coords_spheric]

    points_list = [[Point(*entry)for entry in row] for row in coords_cart]

    trigs_list = []
    for row in range(len(points_list) - 1):
        for col in range(len(points_list[0]) - 1):
            temp1 = Triangle(
                points_list[row][col], points_list[row][col+1], points_list[row+1][col])
            temp2 = Triangle(
                points_list[row + 1][col], points_list[row][col + 1], points_list[row + 1][col + 1])
            trigs_list.extend((temp1, temp2))

    for col in range(len(points_list[-1]) - 1):
        temp1 = Triangle(
            points_list[-1][col], points_list[-1][col + 1], points_list[0][col])
        temp2 = Triangle(
            points_list[0][col], points_list[-1][col + 1], points_list[0][col + 1])
        trigs_list.extend((temp1, temp2))

    p_top = Point(R*math.cos(0)*math.sin(0), R *
                  math.sin(0)*math.sin(0), R*math.cos(0))
    for row in range(len(points_list) - 1):
        trigs_list.append(
            Triangle(p_top, points_list[row][0], points_list[row + 1][0]))
    trigs_list.append(Triangle(p_top, points_list[-1][0], points_list[0][0]))

    p_bottom = Point(R*math.cos(0)*math.sin(math.pi), R *
                     math.sin(0)*math.sin(math.pi), R*math.cos(math.pi))
    for row in range(len(points_list) - 1):
        trigs_list.append(
            Triangle(points_list[row][-1], p_bottom, points_list[row+1][-1]))
    trigs_list.append(
        Triangle(points_list[-1][-1], p_bottom, points_list[0][-1]))
    return trigs_list
