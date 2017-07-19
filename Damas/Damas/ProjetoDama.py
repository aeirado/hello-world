# -*- coding:cp1252 -*-

#------------------------ CRIA TABULEIRO ---------------------------
def criaTabuleiro():
    """
    cria uma matriz 8x8 e adiciona uma string vazia a cada posição
    da matriz.
    """
    cTabuleiro = []
    
    for i in range(8):
        elemento = []
        for j in range(8):
            elemento.append("")
            
        cTabuleiro.append(elemento)
    
    return cTabuleiro     

tabuleiro = criaTabuleiro()

#--------------------------------- VERIFICA TAMANHO TABULEIRO ------
def verificaTamanhoTabuleiro(tabuleiro):
    """
    recebe uma matriz (8x8) e verifica se ela tem 8 linhas e 8 colunas,
    se não retorna False se tem retorna True. 
    """
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if(len(tabuleiro) or len(tabuleiro[j]) != 8):
                return False
            
    return True

#------------------- INICIALIZA TABULEIRO -------------------------
def inicializaTabuleiro(tabuleiro):
    """
    Recebe uma matriz 8x8 que representa uma tabuleiro
    Uma peça é representada por uma tupla que contém 2 caracteres, o primeiro indica a a cor da peça.
    """
    verificaTamanhoTabuleiro(tabuleiro)
    
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if(i == 0) or (i == 1) or (i == 6) or (i == 7):
                if(i == 0) or (i == 1):
                    cor = "w"
                      
                elif(i == 6) or (i == 7):
                    cor = "b" 
                      
            if (i==1):
                if(j==1) or (j==3)or(j==5)or(j==7):
                    peca="p" 
                elif(j==0) or (j==2)or (j==4)or (j==6):
                    cor,peca=" "," "   
            if (i==6):
                if(j==0) or (j==2)or(j==4)or(j==6):
                    peca="p" 
                elif(j==1) or (j==3)or (j==5)or (j==7):
                    cor,peca=" "," "          
            
            if(i == 0):
                if(j == 0):
                    peca = "p"
                elif (j == 6):
                    peca = "p"
                elif(j == 2) :
                    peca = "p"
                elif(j == 4):
                    peca = "p"
                elif(j==1) or (j==3)or (j==5)or (j==7):
                    cor,peca=" "," "   
            if(i == 7):
                if(j == 1):
                    peca = "p"
                elif (j == 3):
                    peca = "p"
                elif(j == 5) :
                    peca = "p"
                elif(j == 7):
                    peca = "p"
                elif(j==0) or (j==2)or (j==4)or (j==6):
                    cor,peca=" "," "           
                    
            if(i == 2) or (i == 3) or (i == 4) or (i == 5):
                cor,peca = " "," "

            tabuleiro[i][j] = (cor,peca)
                 
    return tabuleiro
 
#------------------------------- RETORNAPECA() -----------------------------------------------
tabuleiro = inicializaTabuleiro(tabuleiro)

def retornaPeca(tabuleiro, posicao):
    
    """
    Recebe um tabuleiro (lista 8x8) e uma posicao (tupla com 2 números informando linha e coluna)
    como argumento e retorna qual é a peça (uma tupla) que está naquela posição.
    """
    verificaTamanhoTabuleiro(tabuleiro)
    
    i, j = posicao 
    
    if(0 <= (i or j) <= 7):
        peca = tabuleiro[i][j]
    else:
        return False
    
    return peca, i, j   

#------------------------------------ MOVEPECA() -----------------------------------------------
def movePeca(tabuleiro, posicaoIni, posicaoFim):
    
    """
    Recebe um tabuleiro, uma posicao inicial e uma posicao final.
    Move a peca da posicao inicial para a posicao final.
    Retorna True se for possível mover a peça e retorna False caso contrário.
    """
    verificaTamanhoTabuleiro(tabuleiro)
    
    
    pecaIni, i, j = retornaPeca(tabuleiro, posicaoIni)
    pecaFim, k, l = retornaPeca(tabuleiro, posicaoFim)
     
    if((pecaIni and pecaFim) != False):
        if(pecaIni != ""):
            if(l != j)and((j==l-1 or j==l+1) and (i==k+1 or i== k-1)):
                
              if(pecaIni[0] == "w") and (pecaFim[0] == "b" or pecaFim[0] == " "):
                tabuleiro[k][l], tabuleiro[i][j] = pecaIni, (" "," ")          
              elif(pecaIni[0] == "b") and (pecaFim[0] == "w" or pecaFim[0] == " "):
                tabuleiro[k][l], tabuleiro[i][j] = pecaIni, (" "," ")
              #peca Dama. 
              elif(pecaFim[0]==" " and pecaIni[0]=="w")and(k==7):
                tabuleiro[k][l], tabuleiro[i][j] = ("W","D"), (" "," ")    
              elif(pecaFim[0]=="b" and pecaIni[0]=="b")and(k==0):
                tabuleiro[k][l], tabuleiro[i][j] = ("B","D"), (" "," ")
                                  
              else:
                print "ERROR......."
            else:
                 print "ERROR......."
        else:
            return False
    else:
        return False
    
    return True


#---------------------------------- IMPRIMETABULEIRO() --------------------------------------
def imprimeTabuleiro(tabuleiro):
    
    """
    Imprime na saída padrão um tabuleiro de maneira que um jogador de xadrez possa entendê-lo.
    """
    
    print "="*51
    print "PROJETO DAMAS".center(51)
    print "="*51
    
    for k in range(len(tabuleiro)):
        print "%5i"%k,
    
    print ""    
    
    for i in range(len(tabuleiro)):
        print "-"*50
        print "%i"%i,
        for j in range(len(tabuleiro[i])):
            print "|",
            print "%2s%s"%tabuleiro[i][j],
        print "|"
    
    print "-"*51
    

#-------------------------------FUNÇÃO CRIAR ARQUIVO-----------------------------------------
#def criaArquivo(peca,posicao):
#    
#    arquivo = open('Jogadas.txt','r+')
#    
#    if arquivo.readline() != None:
#        arquivo.write("Jogada - ")
#        arquivo.writelines(str(peca))
#        arquivo.writelines(str(posicao))
#
#    arquivo.close()
