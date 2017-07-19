# -*- coding: cp1252 -*-

'''
Created on 31/05/2012

@author: lab03aluno02

'''

import ProjetoDama
import os


#-------------------------------CHAMADA DA FUNÇÃO ------------------------------------------
tabuleiro = ProjetoDama.criaTabuleiro()
tabuleiro = ProjetoDama.inicializaTabuleiro(tabuleiro)

ProjetoDama.imprimeTabuleiro(tabuleiro) 

#(p1,p2) = 0,0
#(p3,p4) = 0,0
#pecaMovida, m, o = 0,0,0
#pecaCapturada, n, p = 0,0,0

while True:
    
    
    print "MENU DE JOGO"
    print "1 - JOGAR\n","2 - SAIR"
    op = raw_input()
        
    if op == "1":
        (p1,p2) = input("MOVE PECA: ")
        (p3,p4) = input("PARA: ")
        pecaMovida, m, o = ProjetoDama.retornaPeca(tabuleiro, (p1,p2))
        pecaCapturada, n, p = ProjetoDama.retornaPeca(tabuleiro, (p3,p4))
        
        ProjetoDama.movePeca(tabuleiro, (p1,p2), (p3,p4))        

    elif op == "2":
        break
    
    os.system("cls")
        
    ProjetoDama.imprimeTabuleiro(tabuleiro)