import tkinter as tk
import datetime as dt
from decimal import Decimal
#import numpy as np
#import matplotlib.pyplot as plt

def add_entry_command(date, price, liters, km):
    
    # DEALING WITH DATE
    possible_char = '/ _-.'
    print('this is date', date)
    for char in possible_char:
        if char in date:
            print(date.split(char))
            day, month, year = date.split(char)
            break    
        
    day = int(day)
    month = int(month)
    year = int(year)    
    new_date = dt.date(year, month, day)
    
    #DEALING WITH PRICE
    new_price = float(Decimal(float(price)).quantize(Decimal('1.00')))
    
    #DEALING WITH LITERS
    new_liters = float(liters)
    
    #DEALING WITH km
    new_km = float(km)
    
    new_entry = (new_date, new_price, new_liters, new_km)
    insert_entry_to_history(new_entry)
    
def insert_entry_to_history(new_entry):
    global history
    aux_string = ' '.join([str(_) for _ in new_entry]) + '\n'
    with open('gas_history.txt', 'a') as history:
        history.write(aux_string)
        
def clear_history_command():
    with open('gas_history.txt', 'w') as history:
        history.write('   DATE     PRICE   LITERS   km \n')
    
def new_entry_command():
    new_entry_window = tk.Tk()
    new_entry_window.geometry('250x150')
    
    my_frame = tk.Frame(new_entry_window)
    
    date_entry_text = tk.StringVar(new_entry_window, '')
    date_label = tk.Label(my_frame, text = 'Date')
    date_entry = tk.Entry(my_frame, textvariable = date_entry_text)
    date_label.grid(row = 0, column = 0) 
    date_entry.grid(row = 0, column = 1)
    
    price_entry_text = tk.StringVar(new_entry_window,  '')
    price_label = tk.Label(my_frame, text = 'Price')
    price_entry = tk.Entry(my_frame, textvariable = price_entry_text)
    price_label.grid(row = 1, column = 0) 
    price_entry.grid(row = 1, column = 1)

    liters_entry_text = tk.StringVar(new_entry_window,  '')    
    liters_label = tk.Label(my_frame, text = 'Liters')
    liters_entry = tk.Entry(my_frame, textvariable = liters_entry_text)
    liters_label.grid(row = 2, column = 0) 
    liters_entry.grid(row = 2, column = 1)

    km_entry_text = tk.StringVar(new_entry_window,  '')
    km_label = tk.Label(my_frame, text = 'km read')
    km_entry = tk.Entry(my_frame, textvariable = km_entry_text)
    km_label.grid(row = 3, column = 0) 
    km_entry.grid(row = 3, column = 1)
    
    
    my_frame.place(relx=.5, rely=.4, anchor='c')
    
    add_entry_button = tk.Button(new_entry_window, text = 'Add', command = lambda:add_entry_command(date_entry_text.get(),price_entry_text.get(),liters_entry_text.get(),km_entry_text.get()))
    add_entry_button.place(relx =.5, rely = .8, anchor = 'c')
    
    new_entry_window.mainloop()

root = tk.Tk()

my_label = tk.Label(root, text = 'my_label')
my_label.pack()

new_entry_button = tk.Button(root, text = 'Add Entry', command = new_entry_command)
new_entry_button.pack()

clear_history_button = tk.Button(root, text = 'Clear History', command = clear_history_command)
clear_history_button.pack()

root.mainloop()
