# -*- coding: utf-8 -*-

import numpy as np

class Jogo:
    
    def __init__(self):
        self.matriz = np.zeros([2, 2])
        self.jogadores = ["X", "O"]
        self.jogador = self.jogadores
                      
        
    def recebe_jogada (self, i, j):
        
        ganhador = self.verifica_ganhador()
        
        if ganhador == -1:
            if self.jogador == self.jogadores[0]:
                self.matriz[i][j] = 1
                self.jogador = self.jogadores[1]
                ganhador = self.verifica_ganhador()
                
            elif self.jogador == self.jogadores[1]:
                self.matriz[i][j] = 2
                self.jogador = self.jogadores[0]
                ganhador = self.verifica_ganhador()
            
            
                
                
    def verifica_ganhador(self):
        # retorna -1 se ninguem ganhou
        # retorna 0 se empatou
        # retorna 1 se X ganhou
        # retorna 2 se O ganhou
        pass  
