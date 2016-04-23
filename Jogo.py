# -*- coding: utf-8 -*-

import numpy as np

class Jogo:
    
    def __init__(self):
        self.matriz = np.zeros([3, 3])
        self.contador = 0              
        
        
    def muda_button (self, i, j):
        if self.contador % 2 == 0:
            self.contador += 1
            self.matriz[i][j] = 1
            print (self.matriz)
            return "X"
        else:
            self.contador += 1
            self.matriz[i][j] = 2
            print (self.matriz)
            return "O"
    
    def recebe_jogada (self, i, j):
        
        ganhador = self.verifica_ganhador()
        
        if ganhador == -1:
            if self.contador %2 == 0:
                self.matriz[i][j] = 1
                ganhador = self.verifica_ganhador()
                print (self.matriz)
            else:
                self.matriz[i][j] = 2
                ganhador = self.verifica_ganhador()
                print (self.matriz)
            
            
                
                
    def verifica_ganhador(self):
        # retorna -1 se ninguem ganhou ainda
        # retorna 0 se empatou
        # retorna 1 se X ganhou
        # retorna 2 se O ganhou
        pass  
