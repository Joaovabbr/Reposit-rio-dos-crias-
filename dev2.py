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

#A embarcação terá o posicionamento das Grotas 
#O tabuleiro terá um número de X 
#tenho que percorrer todas as chaves do dicionário conferindo se, a posição referente a elas no tabuleiro é igual a X 
def afundados(embarcaçoes , tabuleiro):
    afundados = 0 
    for chaves in embarcaçoes.values():
        for i in range(len(chaves)):
            for contador in range(len(chaves[i])):
                if tabuleiro[chaves[i][contador]] == 'X':
                    afundados += 1 
    return afundados
    
          
          
