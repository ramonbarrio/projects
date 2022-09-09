from tkinter import *
import numpy as np
import time
import math

FIELD_OF_VIEW = 90*math.pi/180
F = 1/math.tan(FIELD_OF_VIEW/2)
LENGTH = 700

theta_x = 0
theta_z = 0
omega_x = 3
omega_z = 1.2

projection_matrix = np.array([
    [F, 0, 0],
    [0, F, 0],
    [0, 0, 1]
])

x_rot_matrix = np.array([
    [1, 0, 0],
    [0, math.cos(theta_x), math.sin(theta_x)],
    [0, -math.sin(theta_x), math.cos(theta_x)]
])

z_rot_matrix = np.array([
    [math.cos(theta_z), math.sin(theta_z), 0],
    [-math.sin(theta_z), math.cos(theta_z), 0],
    [0, 0, 1]
])


def project_point(coord):
    temp = np.matmul(coord, projection_matrix)
    if (abs(temp[2]) < 0.0001):
        return temp
    temp[0] /= temp[2]
    temp[1] /= temp[2]
    return temp


def project_trig(trig):
    res = []
    for point in trig.points:
        temp = project_point(point.coord)
        x, y = temp[0], temp[1]
        res = np.append(res, np.array([x, y]))
    return res


def cross(v1, v2):
    # cross_product
    return np.array(
        [v1[1]*v2[2] - v1[2]*v2[1],
         v1[2]*v2[0] - v1[0]*v2[2],
         v1[0]*v2[1] - v1[1]*v2[0]]
    )


def norm(v):
    # vector_norm
    return pow(pow(v[0], 2)+pow(v[1], 2)+pow(v[2], 2), 0.5)


def dir(v):
    # vector_director
    return np.array(v)/norm(v)


def norm_cross(v1, v2):
    # cross_product normalized
    temp = cross(v1, v2)
    return np.array(dir(temp))


def get_trigs_to_render(trigs_list):
    trigs_to_render = [0]*len(trigs_list)

    for id, trig in enumerate(trigs_list):
        trigs_to_render[id] = project_trig(trig)

    return trigs_to_render[:id+1]


def rescale_projection_to_screen(trigs_to_scale):
    trigs_res = [0]*len(trigs_to_scale)
    for id, trig in enumerate(trigs_to_scale):
        trigs_res[id] = (np.array(trig)+1)*LENGTH/2
    return trigs_res


def rotate_mesh(mesh):
    rot_trigs = [0]*len(mesh.trigs)
    rot_mat = np.matmul(x_rot_matrix, z_rot_matrix)
    for id, trig in enumerate(mesh.trigs):
        rot_points = [0]*len(trig.points)
        for id2, point in enumerate(trig.points):
            rot_point = np.matmul(rot_mat, point.coord)
            rot_points[id2] = Point(*rot_point)
        rot_trigs[id] = Triangle(*rot_points)
    return Mesh(rot_trigs)


def translate(mesh, dir):
    for trig in mesh.trigs:
        for point in trig.points:
            point.coord[0] += dir[0]
            point.coord[1] += dir[1]
            point.coord[2] += dir[2]
            temp = False

    return mesh


root = Tk()
root.title('MyRenderer')
root.geometry('320x320')
root.config(bg='#345')

c = Canvas(
    root,
    height=LENGTH,
    width=LENGTH,
    bg="black"
)

c.place(relx=0.5, rely=0.5, anchor=CENTER)


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


# UNITY CUBE
p1 = Point(0.0, 0.0, 0.0)
p2 = Point(1.0, 0.0, 0.0)
p3 = Point(1.0, 0.0, 1.0)
p4 = Point(0.0, 0.0, 1.0)
p5 = Point(0.0, 1.0, 0.0)
p6 = Point(1.0, 1.0, 0.0)
p7 = Point(1.0, 1.0, 1.0)
p8 = Point(0.0, 1.0, 1.0)

t1 = Triangle(p1.copy(), p2.copy(), p3.copy())
t2 = Triangle(p1.copy(), p3.copy(), p4.copy())
t3 = Triangle(p1.copy(), p6.copy(), p2.copy())
t4 = Triangle(p1.copy(), p5.copy(), p6.copy())
t5 = Triangle(p3.copy(), p2.copy(), p6.copy())
t6 = Triangle(p3.copy(), p6.copy(), p7.copy())
t7 = Triangle(p1.copy(), p4.copy(), p5.copy())
t8 = Triangle(p4.copy(), p8.copy(), p5.copy())
t9 = Triangle(p4.copy(), p3.copy(), p7.copy())
t10 = Triangle(p4.copy(), p7.copy(), p8.copy())
t11 = Triangle(p5.copy(), p8.copy(), p7.copy())
t12 = Triangle(p5.copy(), p7.copy(), p6.copy())

trigs = [
    t1, t2, t3, t4, t5, t6,
    t7, t8, t9, t10, t11, t12
]

# PYRAMID
L = 1

p1 = Point(0.0, 0.0, 0.0)
p2 = Point(L/2, 0.0, L/2*3**0.5)
p3 = Point(L, 0.0, 0.0)
p4 = Point(L/2, L, L/6*3**0.5)

t1 = Triangle(p1, p2, p3)
t2 = Triangle(p1, p4, p2)
t3 = Triangle(p1, p3, p4)
t4 = Triangle(p2, p4, p3)

trigs = [t1, t2, t3, t4]

# SPHERE

R = 1


theta_min = 0
theta_max = 2*math.pi

phi_min = 0.1
phi_max = math.pi - 0.1

N = 10
theta_list = np.linspace(theta_min, theta_max, 2*N, endpoint=False)
phi_list = np.linspace(phi_min, phi_max, N, endpoint=True)

coords_spheric = [[(theta, phi) for phi in phi_list] for theta in theta_list]
coords_cart = [[(R*math.cos(entry[0])*math.sin(entry[1]), R*math.sin(entry[0]) *
                 math.sin(entry[1]), R*math.cos(entry[1])) for entry in row] for row in coords_spheric]

points_list = [[Point(*entry)for entry in row] for row in coords_cart]

trigs_list = []
for row in range(len(points_list) - 1):
    for col in range(len(points_list[0]) - 1):
        temp1 = Triangle(
            points_list[row][col], points_list[row + 1][col], points_list[row][col + 1])
        temp2 = Triangle(
            points_list[row + 1][col], points_list[row][col + 1], points_list[row + 1][col + 1])
        trigs_list.extend((temp1, temp2))

for col in range(len(points_list[-1]) - 1):
    temp1 = Triangle(
        points_list[-1][col], points_list[0][col], points_list[-1][col + 1])
    temp2 = Triangle(
        points_list[0][col], points_list[-1][col + 1], points_list[0][col + 1])
    trigs_list.extend((temp1, temp2))

p_top = Point(R*math.cos(0)*math.sin(0), R *
              math.sin(0)*math.sin(0), R*math.cos(0))
for row in range(len(points_list) - 1):
    trigs_list.append(
        Triangle(p_top, points_list[row][0], points_list[row + 1][0]))

p_bottom = Point(R*math.cos(0)*math.sin(math.pi), R *
                 math.sin(0)*math.sin(math.pi), R*math.cos(math.pi))
for row in range(len(points_list) - 1):
    trigs_list.append(
        Triangle(points_list[row][-1], p_bottom, points_list[row+1][-1]))


# SOIL

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


trigs = trigs_list.copy()
del_t = 0.001
while True:
    theta_x += del_t*omega_x
    theta_z += del_t*omega_z

    x_rot_matrix = np.array([
        [1, 0, 0],
        [0, math.cos(theta_x), -math.sin(theta_x)],
        [0, math.sin(theta_x), math.cos(theta_x)]
    ])

    z_rot_matrix = np.array([
        [math.cos(theta_z), -math.sin(theta_z), 0],
        [math.sin(theta_z), math.cos(theta_z), 0],
        [0, 0, 1]
    ])

    mesh = Mesh(trigs)
    rotated_mesh = rotate_mesh(mesh)
    translated_mesh = translate(rotated_mesh, [-1.1, +1, 1.5])
    trigs_to_scale = get_trigs_to_render(translated_mesh.trigs)
    trigs_to_render = rescale_projection_to_screen(trigs_to_scale)
    time.sleep(0.01)
    c.delete('all')
    for trig in trigs_to_render:
        c.create_polygon(list(trig), fill='', outline='white')
    root.update()

root.mainloop()
