# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import Jogo

class Board:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x320+100+100")
        self.window.title("Jogo da Velha!")
        
        self.window.rowconfigure(0, minsize = 100)
        self.window.rowconfigure(1, minsize = 100)
        self.window.rowconfigure(2, minsize = 100)
        self.window.rowconfigure(3, minsize = 10)
        self.window.columnconfigure(0, minsize = 100)
        self.window.columnconfigure(1, minsize = 100)
        self.window.columnconfigure(2, minsize = 100)
        
        self.button1 = tk.Button(self.window, text = " ", height = 5, width = 10)
        self.button1.grid(row = 0, column = 0, sticky = "nsew")
        self.button1.configure(command=self.button1_clicado)
        
        self.button2 = tk.Button(self.window, text = " ", height = 5, width = 10)
        self.button2.grid(row = 0, column = 1, sticky = "nsew")
        self.button2.configure(command=self.button2_clicado)
        
        self.button3 = tk.Button(self.window, text = " ", height = 5, width = 10)
        self.button3.grid(row = 0, column = 2, sticky = "nsew")
        self.button3.configure(command=self.button3_clicado)
        
        self.button4 = tk.Button(self.window, text = " ", height = 5, width = 10)
        self.button4.grid(row = 1, column = 0, sticky = "nsew")
        self.button4.configure(command=self.button4_clicado)
        
        self.button5 = tk.Button(self.window, text = " ", height = 5, width = 10)
        self.button5.grid(row = 1, column = 1, sticky = "nsew")
        self.button5.configure(command=self.button5_clicado)
        
        self.button6 = tk.Button(self.window, text = " ", height = 5, width = 10)
        self.button6.grid(row = 1, column = 2, sticky = "nsew")
        self.button6.configure(command=self.button6_clicado)
        
        self.button7 = tk.Button(self.window, text = " ", height = 5, width = 10)
        self.button7.grid(row = 2, column = 0, sticky = "nsew")
        self.button7.configure(command=self.button7_clicado)
        
        self.button8 = tk.Button(self.window, text = " ", height = 5, width = 10)
        self.button8.grid(row = 2, column = 1, sticky = "nsew")
        self.button8.configure(command=self.button8_clicado)
        
        self.button9 = tk.Button(self.window, text = " ", height = 5, width = 10)
        self.button9.grid(row = 2, column = 2, sticky = "nsew")
        self.button9.configure(command=self.button9_clicado)
        
        self.label_status = tk.Label()
        self.label_status.configure(text = "Próxima Jogada: X")
        self.label_status.grid(row = 3, column = 0)
        
        menu = Menu(self.window)
        self.window.config(menu=menu)
        
        file = Menu(menu)
        file.add_command(label = "Exit", command = self. client_exit)
        menu.add_cascade(label="File", menu = file)
        

    def iniciar(self):
        self.window.mainloop()
        
    def client_exit(self):
        exit()
        
        
jdv = Board()
jdv.iniciar()
