#Código exercício 1 
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            posicoes.append([linha + i, coluna])

        if orientacao == 'horizontal':
            posicoes.append([linha, coluna + i])

    return posicoes

# Código exercício 2 

def preenche_frota(frota, navio, linha, coluna, orientacao, tamanho):
    frota1 = frota
    if navio not in frota1:

        frota1[navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    else:
         frota1[navio] += [define_posicoes(linha, coluna, orientacao, tamanho)]

         
    return frota1

#Código exercício 3 

def faz_jogada(tabuleiro, linha , coluna):
    if tabuleiro[linha][coluna] == 1: 
                tabuleiro[linha][coluna] = "X"
    else: 
        tabuleiro[linha][coluna] = "-"
    return tabuleiro

# Código exercício 4

def posiciona_frota(frota):

    tabuleiro = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
    ]

    for tipo_navio in frota.values():
        for navio in tipo_navio:
            for posicoes in navio:

                tabuleiro[posicoes[0]][posicoes[1]] = 1


    return tabuleiro

#Código exercício 5 

def afundados(frota, tabuleiro):
    afundados = 0  
    for valores in frota.values(): 
        for navios in valores:
            posição_navio = 0 
            for coordenadas in navios: 
                x = coordenadas[0]
                y = coordenadas[1]
                if tabuleiro[x][y] == 'X' or tabuleiro[x][y] == '-':
                    posição_navio += 1 
                if posição_navio == len(navios):
                    afundados += 1 
    return afundados


#Código exercício 6
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    tabuleiro2 = posiciona_frota(frota)
    posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    locais_com_barco = []
    vertical = 0 
    validade = True 

    for i in tabuleiro2:
        horizontal= 0
        for o in i:
            if o == 1:
                locais_com_barco.append([vertical,horizontal])
            horizontal += 1

        vertical += 1

    for j in locais_com_barco:
        for k in posicao:
            if k[0] == j[0] and k[1] == j[1]:
                validade = False
            if k[0] > 9 or k[1] > 9 or k[0] < 0 or k[1] < 0:
                validade = False

    for w in posicao:
            if w[0] > 9 or w[1] > 9 or w[0] < 0 or w[1] < 0:
                validade = False

            

    return validade