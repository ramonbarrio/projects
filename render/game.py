from tkinter import *
import numpy as np
import time
import math
from entities import Point, Triangle, Mesh
import pyramidmesh
import cubemesh
import spheremesh
import soilmesh

CAMERA = [0., 0., 0.]
LIGHT_DIR = [0., 0., -1.]
FIELD_OF_VIEW = 90.*math.pi/180
ZFAR = 1000.
ZNEAR = 0.5

HEIGHT = 700
WIDTH = 500

RATIO = HEIGHT/WIDTH
F = 1/math.tan(FIELD_OF_VIEW/2)
Q = ZFAR/(ZFAR-ZNEAR)


theta_x = 0
theta_y = 0.
theta_z = 0.

omega_x = 0.
omega_y = 7.
omega_z = 0.

projection_matrix = np.array([
    [RATIO*F, 0, 0, 0],
    [0, F, 0, 0],
    [0, 0, Q, 1],
    [0, 0, -ZNEAR*Q, 0]
])


def project_point(coord):
    temp = np.matmul(coord, projection_matrix)
    if (abs(temp[3]) < 0.0001):
        return temp
    temp[0] /= temp[3]
    temp[1] /= temp[3]
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


def direction(v):
    # vector_director
    return np.array(v)/norm(v)


def norm_cross(v1, v2):
    # cross_product normalized
    temp = cross(v1, v2)
    return np.array(direction(temp))


def find_color(trig):
    global LIGHT_DIR
    if np.dot(trig.normal(), direction(LIGHT_DIR)) < 0:
        return '#000000'
    luminosity = format(
        int(255*np.dot(trig.normal(), direction(LIGHT_DIR))), '02x')
    return '#' + '00' + luminosity + '00'


def get_trigs_to_render(trigs_list):
    trigs_to_render = [0]*len(trigs_list)
    trigs_to_render = {}
    if len(trigs_list) < 1:
        raise Exception("get_trigs_to_render > No trigs in trigs list")
    for id, trig in enumerate(trigs_list):
        trigs_to_render[id] = [project_trig(trig), find_color(trig)]

    return trigs_to_render


def rescale_projection_to_screen(trigs_to_scale):
    trigs_res = {}
    for key in trigs_to_scale:
        trigs_res[key] = [(np.array(trigs_to_scale[key][0])+1)*np.array([WIDTH,
                                                                         HEIGHT, WIDTH, HEIGHT, WIDTH, HEIGHT])/2, trigs_to_scale[key][1]]
    return trigs_res


def rotate_mesh(mesh):
    rot_trigs = [0]*len(mesh.trigs)
    rot_mat_temp = np.matmul(x_rot_matrix, z_rot_matrix)
    rot_mat = np.matmul(rot_mat_temp, y_rot_matrix)
    for id, trig in enumerate(mesh.trigs):
        rot_points = [0]*len(trig.points)
        for id2, point in enumerate(trig.points):
            rot_point = np.matmul(rot_mat, point.coord)
            rot_points[id2] = Point(*rot_point)
        rot_trigs[id] = Triangle(*rot_points)
    return Mesh(rot_trigs)


def translate_mesh(mesh, dir):
    for trig in mesh.trigs:
        for point in trig.points:
            point.coord[0] += dir[0]
            point.coord[1] += dir[1]
            point.coord[2] += dir[2]

    return mesh


def get_view_dir(trig, camera):
    return direction(camera - trig.center())


def find_visible_trigs(mesh):
    visible_trigs = []
    for trig in mesh.trigs:
        similarity = np.dot(trig.normal(), get_view_dir(trig, CAMERA))
        if similarity > 0:
            visible_trigs.append(trig)
    mesh = Mesh(visible_trigs)
    return mesh


root = Tk()
root.title('MyRenderer')
root.geometry(str(WIDTH + 40) + 'x' + str(HEIGHT + 40))
root.config(bg='#345')
root.eval('tk::PlaceWindow . center')


c = Canvas(
    root,
    height=HEIGHT,
    width=WIDTH,
    bg="black"


)

c.place(relx=0.5, rely=0.5, anchor=CENTER)

trigs = soilmesh.generate().copy()
del_t = 0.001

while True:
    theta_x += del_t*omega_x
    theta_z += del_t*omega_z
    theta_y += del_t*omega_y

    x_rot_matrix = np.array([
        [1, 0, 0, 0],
        [0, math.cos(theta_x), -math.sin(theta_x), 0],
        [0, math.sin(theta_x), math.cos(theta_x), 0],
        [0, 0, 0, 1]
    ])

    z_rot_matrix = np.array([
        [math.cos(theta_z), -math.sin(theta_z), 0, 0],
        [math.sin(theta_z), math.cos(theta_z), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    y_rot_matrix = np.array([
        [math.cos(theta_y), 0, math.sin(theta_y), 0],
        [0, 1, 0, 0],
        [-math.sin(theta_y), 0, math.cos(theta_y), 0],
        [0, 0, 0, 1]
    ])

    mesh = Mesh(trigs)
    rotated_mesh = rotate_mesh(mesh)
    translated_mesh = translate_mesh(rotated_mesh, [-2, 2, 5])
    visible_mesh = find_visible_trigs(translated_mesh)
    trigs_to_scale = get_trigs_to_render(visible_mesh.trigs)
    trigs_to_render = rescale_projection_to_screen(trigs_to_scale)
    time.sleep(0.0)
    c.delete('all')
    for key in trigs_to_render:
        c.create_polygon(
            list(trigs_to_render[key][0]), fill=trigs_to_render[key][1], outline='')
    root.update()

root.mainloop()
