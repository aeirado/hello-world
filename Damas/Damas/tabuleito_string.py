# tabuleiro de xadrez
# construir um tab de xadrez com "#" e " " em
# uma string e separar cada linha com "\n"

cadeia = ""
num_linhas = 8
chave = True
pb = "# " # casa preta e casa branca
bp = " #" # inverso

for j in range(num_linhas):
    for i in range(4):
        if chave:
            cadeia += pb
        else:
            cadeia += bp
    if chave:
        chave = False
    else:
        chave = True
    if j < num_linhas - 1:
        cadeia += "\n"

print(cadeia)