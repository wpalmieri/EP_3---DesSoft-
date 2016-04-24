# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import Jogo

class Board:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x320+100+100")
        self.window.title("Jogo da Velha!")
        self.jogo = Jogo.Jogo()
        
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
        self.label_status.configure(text = self.jogo.troca_jogador())
        self.label_status.grid(row = 3, column = 0)
        
        menu = Menu(self.window)
        self.window.config(menu=menu)
        file = Menu(menu)
        file.add_command(label = "Exit", command = self. client_exit)
        file.add_command(label = "Reset", command = self. client_reset)
        menu.add_cascade(label="File", menu = file)
        

    def iniciar(self):
        self.window.mainloop()
        
        
    def button1_clicado(self):
        
        self.button1.config(state = "disabled")
        self.jogo.verifica_ganhador()
        self.button1["text"] = self.jogo.recebe_jogada(0, 0)
        self.label_status.configure(text = self.jogo.troca_jogador())
        
  
    def button2_clicado(self):
        
        self.button2.config(state = "disabled")
        self.jogo.verifica_ganhador()
        self.button2["text"] = self.jogo.recebe_jogada(0, 1)
        self.label_status.configure(text = self.jogo.troca_jogador())
    
    
    def button3_clicado(self):
        
        self.button3.config(state = "disabled")
        self.jogo.verifica_ganhador()
        self.button3["text"] = self.jogo.recebe_jogada(0, 2)
        self.label_status.configure(text = self.jogo.troca_jogador())


    def button4_clicado(self):
        
        self.button4.config(state = "disabled")
        self.jogo.verifica_ganhador()
        self.button4["text"] = self.jogo.recebe_jogada(1, 0)
        self.label_status.configure(text = self.jogo.troca_jogador())


    def button5_clicado(self):
        
        self.button5.config(state = "disabled")
        self.jogo.verifica_ganhador()
        self.button5["text"] = self.jogo.recebe_jogada(1, 1)
        self.label_status.configure(text = self.jogo.troca_jogador())

 
    def button6_clicado(self):
        
        self.button6.config(state = "disabled")
        self.jogo.verifica_ganhador()
        self.button6["text"] = self.jogo.recebe_jogada(1, 2)
        self.label_status.configure(text = self.jogo.troca_jogador())
    
           
    def button7_clicado(self):
        
        self.button7.config(state = "disabled")
        self.jogo.verifica_ganhador()
        self.button7["text"] = self.jogo.recebe_jogada(2, 0)
        self.label_status.configure(text = self.jogo.troca_jogador())
 
 
    def button8_clicado(self):
        
        self.button8.config(state = "disabled")
        self.jogo.verifica_ganhador()
        self.button8["text"] = self.jogo.recebe_jogada(2, 1)
        self.label_status.configure(text = self.jogo.troca_jogador())
            
    
    def button9_clicado(self):
        
        self.button9.config(state = "disabled")
        self.jogo.verifica_ganhador()
        self.button9["text"] = self.jogo.recebe_jogada(2, 2)
        self.label_status.configure(text = self.jogo.troca_jogador())


    def client_exit(self):
        
        exit()
        
        
    def client_reset(self):
        
        self.jogo.limpa_jogadas()
                
        self.button1.config(state = "active")
        self.button1["text"] = " "
        
        self.button2.config(state = "active")
        self.button2["text"] = " "

        self.button3.config(state = "active")
        self.button3["text"] = " "

        self.button4.config(state = "active")
        self.button4["text"] = " "

        self.button5.config(state = "active")
        self.button5["text"] = " "

        self.button6.config(state = "active")
        self.button6["text"] = " "

        self.button7.config(state = "active")
        self.button7["text"] = " "

        self.button8.config(state = "active")
        self.button8["text"] = " "

        self.button9.config(state = "active")
        self.button9["text"] = " "
        
        
jdv = Board()
jdv.iniciar()
