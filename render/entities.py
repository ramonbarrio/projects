
import numpy as np


class Point():
    def __init__(self, x, y, z, one=1):
        self.coord = np.array([x, y, z, one])

    def copy(self):
        return Point(self.coord[0], self.coord[1], self.coord[2])


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.points = np.array([p1, p2, p3])

    def normal(self):
        return norm_cross(self.p2.coord-self.p1.coord, self.p3.coord-self.p1.coord)

    def center(self):
        return (self.p1.coord[:3] + self.p2.coord[:3] + self.p3.coord[:3])/3


class Mesh:
    def __init__(self, trigs_list):
        self.trigs = trigs_list


def norm_cross(v1, v2):
    # cross_product normalized
    temp = cross(v1, v2)
    return np.array(direction(temp))


def cross(v1, v2):
    # cross_product
    return np.array(
        [v1[1]*v2[2] - v1[2]*v2[1],
         v1[2]*v2[0] - v1[0]*v2[2],
         v1[0]*v2[1] - v1[1]*v2[0]]
    )


def direction(v):
    # vector_director
    return np.array(v)/norm(v)


def norm(v):

    # vector_norm
    return pow(pow(v[0], 2)+pow(v[1], 2)+pow(v[2], 2), 0.5)
