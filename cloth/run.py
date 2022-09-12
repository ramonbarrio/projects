
from sqlite3 import connect
from tkinter import *
import time
from entites import Bridge, Cloth, Knot

HEIGHT = 700
WIDTH = 500
FRACTION = 0.8
RATIO = WIDTH/HEIGHT
OFFSET = (HEIGHT*1-FRACTION)/2

root = Tk()
root.title('2D Cloth Simulator')
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


def build_cloth(width=2, height=1, mass=1, elasticity=1, del_l=0.1):
    nx = int(width/del_l) + 1
    ny = int(height/del_l) + 1
    knot_mass = mass/nx*ny
    knot_id = 0
    knots_list = [0]*(nx*ny)
    knots_matrix = [[0 for i in range(ny)] for j in range(nx)]

    for i in range(nx):
        for j in range(ny):
            is_fixed = False
            if j == 0:
                is_fixed = True
            temp_knot = Knot(knot_id, knot_mass, [i, j], [
                             i*del_l, j*del_l], fixed=is_fixed)
            print(temp_knot)
            knots_matrix[i][j] = temp_knot
            knots_list[knot_id] = temp_knot
            knot_id += 1
    print('finished building knots list')

    bridges_list = [0]*(2*nx*ny - nx - ny)
    bridge_elasticity = elasticity/del_l
    bridge_id = 0

    for knot_x in range(len(knots_matrix)):
        for knot_y in range(len(knots_matrix[0])):
            knot_id = knots_matrix[knot_x][knot_y].id
            connect_right = knot_x < nx - 1
            connect_down = knot_y < ny - 1

            if connect_down:
                temp_bridge = Bridge(
                    bridge_id, bridge_elasticity, del_l, knot_id, knot_id + 1)
                print(temp_bridge)
                bridges_list[bridge_id] = temp_bridge
                bridge_id += 1

            if connect_right:
                temp_bridge = Bridge(
                    bridge_id, bridge_elasticity, del_l, knot_id, knot_id + ny)
                print(temp_bridge)
                bridges_list[bridge_id] = temp_bridge
                bridge_id += 1

    return Cloth(knots_list, bridges_list)


def reescale_to_screen(lines_list):
    reescaled_lines = [0]*len(lines_list)
    for id, line in enumerate(lines_list):
        reescaled_lines[id] = [(line[0]*WIDTH),
                               (line[1]*RATIO*HEIGHT), (line[2]*WIDTH), (line[3]*RATIO*HEIGHT)]

    return reescaled_lines


cloth = build_cloth()
lines_to_render = reescale_to_screen(cloth.get_lines_to_render())

while True:
    time.sleep(0.0)
    c.delete('all')
    for line in lines_to_render:
        c.create_polygon(line, fill='', outline='white')
    root.update()

root.mainloop()
