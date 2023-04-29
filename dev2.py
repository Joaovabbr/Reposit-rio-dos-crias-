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
def afundados(frota, tabuleiro):
    afundados = 0 
    #Estou fazendo valores ser a lista dentro do valor do dicionário 
    for valores in frota.values():
        #estou fazendo navios ser a grande lista dentro da lista maior 
        for navios in valores:
            #estou resetando a posição navio para 0 para cada vez que ele mudar na lista intermediária 
            posição_navio = 0 
            for coordenadas in navios: 
                x = coordenadas[0]
                y = coordenadas[1]
                if tabuleiro[x][y] == 'X' or tabuleiro[x][y] == '-':
                    posição_navio += 1 
                if posição_navio == len(navios):
                    afundados += 1 
    return afundados  

#Código exercício 7 

    
          
          
