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

#Exercício 5 

def afundados(embarcaçoes , tabuleiro):
    afundados = 0 
    for chaves in embarcaçoes.values():
        for i in range(len(chaves)):
            for contador in range(len(chaves[i])):
                if tabuleiro[chaves[i][contador]] == 'X':
                    afundados += 1 
    return afundados