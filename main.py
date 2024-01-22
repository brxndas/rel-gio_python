# importacoes da libs

import tkinter as tk
from tkinter import * 
import os
from time import strftime

root = tk.Tk()
root.title('Seu relógio')
root.geometry('600x320')
root.maxsize(600,320)
root.minsize(600,320)
root.configure(background='#979aaa')

def get_name():
    name_usuario= os.getlogin()
    name.config(text=f'Olá, {name_usuario}')

def get_data():
    data_atual = strftime('%a, %d/%m/%Y')
    data.config(text=data_atual)

def get_hora():
    hora_atual = strftime('%H:%M:%S')
    hora.config(text=hora_atual)
    hora.after(1000, get_hora)

margin = tk.Canvas(root,width=600, height=60, bg='#979aaa', bd=0, highlightthickness=0, relief='ridge')
margin.pack()

name = Label(root,bg='#979aaa', fg='#f2d7e3', font=('Montserrat',16))
name.pack()

data = Label(root,bg='#979aaa', fg='#f2d7e3', font=('Montserrat',14))
data.pack(pady=2)

hora = Label(root,bg='#979aaa', fg='#f2d7e3', font=('Montserrat',64, 'bold'))
hora.pack(pady=2)

get_name()
get_data()
get_hora()
root.mainloop()

