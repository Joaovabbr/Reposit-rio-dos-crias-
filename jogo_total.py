#Código Exercício 1 
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            posicoes.append([linha + i, coluna])

        if orientacao == 'horizontal':
            posicoes.append([linha, coluna + i])

    return posicoes

# Código Exercício 2 

def preenche_frota(frota, navio, linha, coluna, orientacao, tamanho):
    frota1 = frota
    if navio not in frota1:

        frota1[navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    else:
         frota1[navio] += [define_posicoes(linha, coluna, orientacao, tamanho)]

         
    return frota1

#Código exercicio 3 

def faz_jogada(tabuleiro, linha , coluna):
    if tabuleiro[linha][coluna] == 1: 
                tabuleiro[linha][coluna] = "X"
    else: 
        tabuleiro[linha][coluna] = "-"
    return tabuleiro
