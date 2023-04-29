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
tipos = ['porta-aviões', 'navio-tanque', 'contratorpedeiro', 'submarino']
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

i = 0
while i < len(tipos):
    if i == 0:

        Q_navio = 0

        while Q_navio < 1:

            print('Insira as informações referentes ao navio porta-aviões que possui tamanho 4')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            orientacao = int(input('[1] vertical [2] horizontal >'))
            if orientacao == 2:
                orientacao = 'horizontal'
            else:
                orientacao = 'vertical'

            if posicao_valida(frota, linha, coluna,orientacao, 4) == True:
                frota[tipos[i]] = [(define_posicoes(linha, coluna, orientacao, 4))]
                Q_navio += 1

            else: 
                print('Esta posição não está válida!')
            

    if i == 1:

        Q_navio = 0

        while Q_navio < 2:
            print('Insira as informações referentes ao navio navio-tanque que possui tamanho 3')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            orientacao = int(input('[1] vertical [2] horizontal >'))
            if orientacao == 2:
                orientacao = 'horizontal'
            else:
                orientacao = 'vertical'

            if posicao_valida(frota, linha, coluna,orientacao, 3) == True:
                if tipos[i] not in frota:
                    frota[tipos[i]] = [(define_posicoes(linha, coluna, orientacao, 3))]
                    Q_navio += 1
                if tipos[i] in frota:
                    frota[tipos[i]] += [(define_posicoes(linha,coluna,orientacao, 3))]
                    Q_navio += 1

            else: 
                print('Esta posição não está válida!')

    if i == 2:
        Q_navio = 0
        while Q_navio < 3:
            print('Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            orientacao = int(input('[1] vertical [2] horizontal >'))
            if orientacao == 2:
                orientacao = 'horizontal'
            else:
                orientacao = 'vertical'

            if posicao_valida(frota, linha, coluna,orientacao, 2) == True:
                if tipos[i] not in frota:
                    frota[tipos[i]] = [(define_posicoes(linha, coluna, orientacao, 2))]
                    Q_navio += 1
                if tipos[i] in frota:
                    frota[tipos[i]] += [(define_posicoes(linha,coluna,orientacao, 2))]
                    Q_navio += 1
            else: 
                print('Esta posição não está válida!')

    
    if i == 3:
        Q_navio = 0
        while Q_navio < 4:
            print('Insira as informações referentes ao navio submarino que possui tamanho 1')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            orientacao = 'vertical'

            if posicao_valida(frota, linha, coluna,orientacao, 1) == True:
                if tipos[i] not in frota:
                    frota[tipos[i]] = [(define_posicoes(linha, coluna, orientacao, 1))]
                    Q_navio += 1
                if tipos[i] in frota:
                    frota[tipos[i]] += [(define_posicoes(linha,coluna,orientacao, 1))]
                    Q_navio += 1
            else: 
                print('Esta posição não está válida!')

            



    i += 1
print(frota)
    
    
          
          
