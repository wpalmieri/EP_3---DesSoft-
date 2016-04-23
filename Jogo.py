# -*- coding: utf-8 -*-

import numpy as np

class Jogo:
    
    def __init__(self):
        self.matriz = np.zeros([3, 3])
        self.jogadores = ["O", "X"]
        self.contador = 0              
        
        
    def muda_button (self):
        if self.contador % 2 == 0:
            self.contador += 1
            return "X"
        else:
            self.contador += 1
            return "O"
    
    def recebe_jogada (self, i, j):
        
        ganhador = self.verifica_ganhador()
        
        if ganhador == -1:
            if self.contador %2 == 0:
                self.matriz[i][j] = 1
                self.jogador = "O"
                ganhador = self.verifica_ganhador()
                
            else:
                self.matriz[i][j] = 2
                self.jogador = "X"
                ganhador = self.verifica_ganhador()
            
            
                
                
    def verifica_ganhador(self):
        # retorna -1 se ninguem ganhou ainda
        # retorna 0 se empatou
        # retorna 1 se X ganhou
        # retorna 2 se O ganhou
        pass  
