import tkinter as tk

#caracter_string = ',.<>#;:~^}]ºªç´`¹²³£¢¬\=+-§"!@#$%&*_+/?°®ŧ←↓→øæßðđħ̉«»©“”nµŋħ̉'
caracter_string = 'abcdefghijklmnopqrstuvwxyz'
#caracter_string = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
#caracter_string = '1234567890'

N = 6
nlin = N
ncol = N
char_dict = {}
index = 0

for i in range(nlin):
    for j in range(ncol):
        if index <= len(caracter_string) - 1:
            char_dict[(i,j)] = caracter_string[index]     
            index += 1

square_size = 15
root = tk.Tk()
for place in char_dict:
    char = char_dict[place]
    x, y = place
    line = square_size*char+'\n'
    text_to_label = ''.join(square_size*line)
    my_label = tk.Label(text=text_to_label, font = ('Lucida Console', 5))
    my_label.grid(row = x, column = y)
    
root.mainloop()