
import numpy as np


class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.coord = np.array([x, y, z])

    def copy(self):
        return Point(self.x, self.y, self.z)


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.points = np.array([p1, p2, p3])
        self.n = norm_cross(p2.coord-p1.coord, p3.coord-p1.coord)


class Mesh:
    def __init__(self, trigs_list):
        self.trigs = trigs_list


def norm_cross(v1, v2):
    # cross_product normalized
    temp = cross(v1, v2)
    return np.array(dir(temp))


def cross(v1, v2):
    # cross_product
    return np.array(
        [v1[1]*v2[2] - v1[2]*v2[1],
         v1[2]*v2[0] - v1[0]*v2[2],
         v1[0]*v2[1] - v1[1]*v2[0]]
    )
