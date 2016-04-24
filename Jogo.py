# -*- coding: utf-8 -*-

import numpy as np

class Jogo:
    
    def __init__(self):
        self.matriz = np.zeros([3, 3])
        self.contador = 0
        #self.jogador


    def troca_jogador (self):
        if self.verifica_ganhador() == -1:
            if self.contador %2 == 0:
                print ("contador =", self.contador)
                print (" ")
                return "Vez do jogador X"
            else:
                print ("contador =", self.contador)
                print (" ")
                return "Vez do jogador O"
        elif self.verifica_ganhador() == 1:
            return "Jogador X ganhou!"
        elif self.verifica_ganhador() == 2:
            return "Jogador 0 ganhou!"
        elif self.verifica_ganhador() == 0:
            return "O jogo deu velha!"
        
        

                
                
    def limpa_jogadas (self):
        self.matriz = np.zeros([3,3])
        print (self.matriz)
                    
                
    def verifica_ganhador(self):
        
        if self.matriz[0][0] == self.matriz[0][1] == self.matriz[0][2] == 1\
            or self.matriz[1][0] == self.matriz[1][1] == self.matriz[1][2] == 1\
            or self.matriz[2][0] == self.matriz[2][1] == self.matriz[2][2] == 1\
            or self.matriz[0][0] == self.matriz[1][0] == self.matriz[2][0] == 1\
            or self.matriz[0][1] == self.matriz[1][1] == self.matriz[2][1] == 1\
            or self.matriz[0][2] == self.matriz[1][2] == self.matriz[2][2] == 1\
            or self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] == 1\
            or self.matriz[2][2] == self.matriz[1][1] == self.matriz[2][0] == 1:
                return 1
                
        elif self.matriz[0][0] == self.matriz[0][1] == self.matriz[0][2] == 2\
            or self.matriz[1][0] == self.matriz[1][1] == self.matriz[1][2] == 2\
            or self.matriz[2][0] == self.matriz[2][1] == self.matriz[2][2] == 2\
            or self.matriz[0][0] == self.matriz[1][0] == self.matriz[2][0] == 2\
            or self.matriz[0][1] == self.matriz[1][1] == self.matriz[2][1] == 2\
            or self.matriz[0][2] == self.matriz[1][2] == self.matriz[2][2] == 2\
            or self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] == 2\
            or self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] == 2:
                return 2
                
        elif self.matriz[0][0] == 0\
            or self.matriz[0][1] == 0\
            or self.matriz[0][2] == 0\
            or self.matriz[1][0] == 0\
            or self.matriz[1][1] == 0\
            or self.matriz[1][2] == 0\
            or self.matriz[2][0] == 0\
            or self.matriz[2][1] == 0\
            or self.matriz[2][2] == 0:
                return -1
        else:
            return 0
                 
        
    def recebe_jogada (self, i, j):
        if self.verifica_ganhador() == 1\
            or self.verifica_ganhador == 2:
                pass
                ### O que devo fazer aqui? ###
                ### Aqui deve-se colocar o que acontece quando alguém já ganhou ###
            
        elif self.verifica_ganhador() == -1:
            
            if self.contador % 2 == 0:
                self.contador += 1
                self.matriz[i][j] = 1
                self.troca_jogador ()
                print (self.matriz)
                return "X"
                
            else:
                self.contador += 1
                self.matriz[i][j] = 2
                self.troca_jogador ()
                print (self.matriz)
                return "O"
                
        elif self.verifica_ganhador() == 0:
            pass
            ###O que devo fazer aqui???###
            ### Aqui deve-se colocar o que acontece quando o jogo empatou ###