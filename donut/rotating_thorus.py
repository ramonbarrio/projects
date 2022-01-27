import numpy as np
from math import pi, acos, cos, sin
# import matplotlib.pyplot as plt
import tkinter as tk

def director(vector):
    return vector/norm(vector)

def norm(point):
    return dist_point2point(point)
    
def dist_point2point(p1, p2=(0,0,0)):
    x, y, z = p1
    a, b, c = p2
    return ((x - a)**2 + (y - b)**2 + (z - c)**2)**0.5

def proj(vector, plane_director):
    x, y, z = vector
    a, b, c = plane_director
    dot_prod = x*a + y*b + z*c
    #print(plane_director*dot_prod)
    return (plane_director*dot_prod)

def dot(p1, p2):
    x, y, z = p1
    a, b, c = p2
    return a*x + b*y + c*z

def vec(p1, p2):
    x, y, z = p1
    a, b, c = p2
    i = y*c - z*b
    j = - x*c + z*a
    k = x*b - y*a
    return np.array((i,j,k))
            
def find_points_on_ring(center, plane_director, rad1, rad2):
    
    a, b, c = plane_director
    dir1 = director(np.array([-(b + c)/a, 1, 1]))
    dir2 = vec(dir1, (a, b, c))
    every_theta = np.linspace(0,2*pi,n_main_theta)
    every_point = [center + rad1*(sin(theta)*dir1 + cos(theta)*dir2) for theta in every_theta]
    return every_point
    
    
    #-------------------
# =============================================================================
#     a, b, c = plane_director
#     main_rad = rad1
#     second_rad = rad2
#     theta = 0.5/(main_rad + second_rad)
#     
#     curr_dir = director(np.array([-(b + c)/a, 1, 1]))
#     points = []
#     curr_theta = 0
#     curr_point = center + main_rad*curr_dir
# 
#     while curr_theta < 2*pi:
#         points.append(curr_point)
#         #print(curr_dir, curr_point)
#         
#         direction_change = vec(curr_dir, plane_director)
#         #print(dot(direction_change, curr_dir))
#         aux_point = curr_point + direction_change*0.3
#         proj_point = aux_point - proj((aux_point-center), plane_director)
#         next_dir = director((proj_point-center))
#         next_point = center + main_rad*next_dir
#         dot_prod = dot(director(next_point-center), director(curr_point-center))
#         #print(dot_prod)
#         #if dot_prod > 1:
#             #print(plane_director)
#         #    return points
#         delta_theta = acos(dot_prod)
#         curr_theta += delta_theta
#         curr_point = next_point
#         curr_dir = next_dir
#     return points
# =============================================================================

def find_points_on_thorus(center, ring, radi, plane_director):
    every_theta = np.linspace(0, 2*pi, n_second_theta)
    points_on_thorus = {}
    for point in ring:
        radi_dir = director(point - center)
        second_ring = radi*np.array([radi_dir*cos(theta)+plane_director*sin(theta) for theta in every_theta])
        for coord in second_ring:
            aux_coord = coord + point
            x, y, z = aux_coord
            points_on_thorus[(x, y, z)] = director(coord)
    return points_on_thorus

def create_text_for_label(plane_eq, bg):
    a, b, c, d = plane_eq
    plane_director = np.array((a,b,c))/norm((a,b,c))
    plane_tolerance = 1
    
    points_on_ring = find_points_on_ring(center, plane_director, main_rad, second_rad)
    points_on_thorus = find_points_on_thorus(center, points_on_ring, second_rad, plane_director)   
           
    grid_dict = {}
    norm_dict = {}
    for point in points_on_thorus:
        x, y = int(point[0]/size_grid_div), int(point[1]/size_grid_div)
        if (x,y) in grid_dict:
            if grid_dict[(x,y)] < point[2]:
                grid_dict[(x,y)] = point[2]
                norm_dict[(x,y)] = points_on_thorus[point]
        else:
            grid_dict[(x,y)] = point[2]
            norm_dict[(x,y)] = points_on_thorus[point]
            
    soma_normais = {}        
    for point in grid_dict:
        if point in soma_normais:
            soma_normais[point] += [norm_dict[point]]
        else:
            soma_normais[point] = [norm_dict[point]]
    for point in soma_normais:
        soma_normais[point] = sum(soma_normais[point])/len(soma_normais[point])    
            
    camera_angle = (0, 0, 1)
    light_intensity = {}
    
    for point in soma_normais:
        intensity = dot(soma_normais[point], camera_angle)
        light_intensity[point] = intensity
        
# =============================================================================
#     chard_dict = {
#                     0: ' ',
#                     1: '.',
#                     2: ',',
#                     3: '¬',
#                     4: '>',
#                     5: '*',
#                     6: '¢',
#                     7: '@',
#                     8: 'æ',
#                     9: '#'    
#                     } 
#     
# =============================================================================
    chard_dict = {
                    9: '.',
                    8: ',',
                    7: '~',
                    6: '>',
                    5: '¬',
                    4: '*',
                    3: '¢',
                    2: '@',
                    1: 'æ',
                    0: '#'    
                    } 
    
    
    aux_list_to_print = np.full((size_char_print, size_char_print), bg)
    #aux_list_to_print = np.full((50, 50), ' ')
    for coord in light_intensity:
        x, y = coord
        aux_list_to_print[x,y] = chard_dict[abs(int(10*light_intensity[coord]))]
    
    aux2 = ['']*size_char_print
    index = 0
    for text in aux_list_to_print:
        #print(''.join(text))
        aux2[index] = ''.join(text)
        #print(aux2[index])
        index += 1 
    
    text_to_print = '\n'.join(aux2)
    return text_to_print

def create_directions_to_rotate(plane, omega):
    directions_to_rotate = []
    d = plane[3]
    vec_dir = plane[0:3]
    for i in range(50):
        vec_change = vec(omega, vec_dir)
        new_dir = vec_dir + 0.1*vec_change
        new_dir = director(new_dir)
        a, b, c = new_dir
        directions_to_rotate.append((a, b, c, d))
        vec_dir = new_dir
    return directions_to_rotate

def _pass():
    pass

def update():
    global dir_count
    global every_frame_text
    my_label.config(text = every_frame_text[dir_count])
    dir_count += 1
    if dir_count < len(every_frame_text): 
        my_label.after(80, update)
        
def repeat():
    global dir_count
    dir_count = 0
    update()

        
# =============================================================================
# grid_to_plot = np.full((L,L),' ')
# for point in main_sphere_intersec_plane:
#     x, y = point[0], point[1]
#     grid_to_plot[x,y] = 'X'
#     
# #print(grid_to_plot)
# 

# 
# points_on_torus = []
# =============================================================================


if __name__ == '__main__':
# =============================================================================
#     size_grid = 20
#     size_grid_div = 2
#     size_char_print = size_grid/size_grid_div
# 
#     n_main_theta = 150
#     n_second_theta = 100
#     
# =============================================================================
    size_grid = 200
    size_grid_div = 5
    size_char_print = int(size_grid/size_grid_div)

    n_main_theta = 300
    n_second_theta = 200
    
    x0, y0, z0 = 100, 100, 100
    center = (x0, y0, z0)
    main_rad = 70
    
    second_rad = 20
    
    global every_frame_text
    
    rotating_plane_director = create_directions_to_rotate(np.array((4/3, 0, -10/3, 100)), np.array((1,1,1)))
    every_frame_text = [create_text_for_label((4/3, 0, -10/3, 100), ' ')]
    for direction in rotating_plane_director:
        every_frame_text.append(create_text_for_label(direction, ' '))
    
    root = tk.Tk()
    # root.geometry('1000x1000')
    size = 5
    my_label = tk.Label(root, text = create_text_for_label((4/3, 0, -10/3, 100), ' '), font = ('Lucida Console', size))
    my_button = tk.Button(root, text = 'again', command = repeat)
    
    my_button.grid(row = 0, column = 0)
    my_label.grid(row = 0, column = 1)
    
    global dir_count 
    dir_count = 0
    
    update()
    
    root.mainloop()