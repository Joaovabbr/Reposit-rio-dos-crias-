#Código do exercício 1
def define_posicoes(linha , coluna , orientaçao , tamanho): 
    posição = []
    for numero in range(tamanho): 
        if orientaçao == 'horizontal': 
            posição.append([linha , coluna+numero])
        if orientaçao == 'vertical': 
            posição.append([linha+numero , coluna])   
    return posição

#Código exercicio 3 
def faz_jogada(tabuleiro, linha , coluna):
    if tabuleiro[linha][coluna] == 1: 
                tabuleiro[linha][coluna] = "X"
    else: 
        tabuleiro[linha][coluna] = "-"
    return tabuleiro

#Código exercicio 5 
