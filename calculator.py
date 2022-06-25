from ctypes import sizeof
from glob import glob
from tkinter import *
import tkinter as tk 
from tkinter import ttk # ANOTHER BUTTON STYLE 
from webbrowser import get

from setuptools import Command

# raiz 
raiz = tk.Tk()
raiz.title('Calculadora')
raiz.geometry('185x155')
raiz.resizable(1,1)

# Display
entry = tk.Entry(justify=tk.RIGHT)
entry.place(x=5,y=8)
entry.config(width=21)

op = 0
a = 0.0
b = 0.0
c = 0.0
var = ''

def beforeTo(op):
    a = entry.get()
    print('a = ' +a)
    entry.delete(0,END)
    sw = {
        1:'+',
        2:'-',
        3:'x',
        4:'/',
    }
    var = sw.get(op,'no')
    print('op = '+ str(var))

def result():
    b = entry.get()
    print('b = ' +b)
    if op == 1:
        print('Entro al 1')
        entry.insert(0,a+b)
    elif op == 2:
        print('Entro al 2')
    elif op == 3:
        print('Entro al 3')
    elif op == 4:
        print('Entro al 4')
    else:
        print('No entro')
    entry.delete(0,END)

# Buttons
exit_button = tk.Button(raiz, text='OFF', width=4, command=lambda:raiz.quit())
exit_button.place(x=5,y=125)
one_button = tk.Button(raiz, text='1', width=4, command=lambda:entry.insert(tk.END,'1'))
one_button.place(x=5,y=95)
two_button = tk.Button(raiz, text='2', width=4, command=lambda:entry.insert(tk.END,'2'))
two_button.place(x=50,y=95)
three_button = tk.Button(raiz, text='3', width=4, command=lambda:entry.insert(tk.END,'3'))
three_button.place(x=95,y=95)
four_button = tk.Button(raiz, text='4', width=4, command=lambda:entry.insert(tk.END,'4'))
four_button.place(x=5,y=65)
five_button = tk.Button(raiz, text='5', width=4, command=lambda:entry.insert(tk.END,'5'))
five_button.place(x=50,y=65)
six_button = tk.Button(raiz, text='6', width=4, command=lambda:entry.insert(tk.END,'6'))
six_button.place(x=95,y=65)
seven_button = tk.Button(raiz, text='7', width=4, command=lambda:entry.insert(tk.END,'7'))
seven_button.place(x=5,y=35)
eight_button = tk.Button(raiz, text='8', width=4, command=lambda:entry.insert(tk.END,'8'))
eight_button.place(x=50,y=35)
nine_button = tk.Button(raiz, text='9', width=4, command=lambda:entry.insert(tk.END,'9'))
nine_button.place(x=95,y=35)
zero_button = tk.Button(raiz, text='0', width=4, command=lambda:entry.insert(tk.END,'0'))
zero_button.place(x=50,y=125)
add_button = tk.Button(raiz, text='+', width=4, command=lambda:beforeTo(1))
add_button.place(x=140,y=35)
sub_button = tk.Button(raiz, text='-', width=4, command=lambda:beforeTo(2))
sub_button.place(x=140,y=65)
times_button = tk.Button(raiz, text='x', width=4, command=lambda:beforeTo(3))
times_button.place(x=140,y=95)
div_button = tk.Button(raiz, text='/', width=4, command=lambda:beforeTo(4))
div_button.place(x=140,y=125)
result_button = tk.Button(raiz, text='=', width=4, command=lambda:result(op))
result_button.place(x=95,y=125)
del_button = tk.Button(raiz, text='Del',command=lambda:entry.delete(len(entry.get())-1,END),width=4)
del_button.place(x=140,y=4)

#END
raiz.mainloop()