# -*- coding: utf-8 -*-
import numpy as np

class Jogo:
    
    def __init__(self):
        self.matriz = np.zeros([3, 3]) # Na matriz: 0 = vazio, 1 = X e 2 = O
        self.contador = 0


    def troca_jogador (self):
        
        if self.verifica_ganhador() == -1: # Caso ainda não tenha ganhador
            
            if self.contador % 2 == 0: # Quando o contador é um número par
                
                print ("contador =", self.contador)
                print (" ")
                return "Vez do jogador: X"
            
            else: # Quando o contador é impar
            
                print ("contador =", self.contador)
                print (" ")
                return "Vez do jogador: O"
                
        elif self.verifica_ganhador() == 1: # Caso X tenha ganhado
            
            return "Jogador X ganhou!"
            
        elif self.verifica_ganhador() == 2: # Caso O tenha ganhado
            
            return "Jogador O ganhou!"
            
        elif self.verifica_ganhador() == 0: # Caso tenha dado empate
    
            return "O jogo deu velha!"
   
   
    def limpa_jogadas (self):
    
        self.matriz = np.zeros([3,3]) # Cria uma nova matriz
        print (self.matriz)
  
   
    def verifica_ganhador(self):
        
        # retorna 0 em caso de empate, 1 caso X tenha ganhado, 2 caso O tenha ganhado e -1 caso contrário
        
        if self.matriz[0][0] == self.matriz[0][1] == self.matriz[0][2] == 1\
            or self.matriz[1][0] == self.matriz[1][1] == self.matriz[1][2] == 1\
            or self.matriz[2][0] == self.matriz[2][1] == self.matriz[2][2] == 1\
            or self.matriz[0][0] == self.matriz[1][0] == self.matriz[2][0] == 1\
            or self.matriz[0][1] == self.matriz[1][1] == self.matriz[2][1] == 1\
            or self.matriz[0][2] == self.matriz[1][2] == self.matriz[2][2] == 1\
            or self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] == 1\
            or self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] == 1:
            # Essas são todas as possibilidades de vitória para o X
                return 1
                
        elif self.matriz[0][0] == self.matriz[0][1] == self.matriz[0][2] == 2\
            or self.matriz[1][0] == self.matriz[1][1] == self.matriz[1][2] == 2\
            or self.matriz[2][0] == self.matriz[2][1] == self.matriz[2][2] == 2\
            or self.matriz[0][0] == self.matriz[1][0] == self.matriz[2][0] == 2\
            or self.matriz[0][1] == self.matriz[1][1] == self.matriz[2][1] == 2\
            or self.matriz[0][2] == self.matriz[1][2] == self.matriz[2][2] == 2\
            or self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] == 2\
            or self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] == 2:
            # Essas são todas as possibilidades de vitória para o O   
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
            # Checar se ainda existe alguma casa vazia para poder continuar o jogo    
                return -1
        
        else:
            # Em caso de empate
            return 0
        
    def recebe_jogada (self, i, j):
        
        if self.verifica_ganhador() == 1\
            or self.verifica_ganhador == 2:
                pass
            
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
