#Define posições
def define_posicoes(linha , coluna , orientaçao , tamanho): 
    posição = []
    for numero in range(tamanho): 
        if orientaçao == 'horizontal': 
            posição.append([linha , coluna+numero])
        if orientaçao == 'vertical': 
            posição.append([linha+numero , coluna])   
    return posição

#Preenche frota 

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    frota_posicionada = frota 
    if nome_navio not in frota_posicionada: 
        frota_posicionada[nome_navio] = [define_posicoes(linha,coluna,orientacao,tamanho)]
    else: 
        frota_posicionada[nome_navio].append((define_posicoes(linha,coluna,orientacao,tamanho)))
    return frota_posicionada

#Faz jogada
def faz_jogada(tabuleiro, linha , coluna):
    if tabuleiro[linha][coluna] == 1: 
                tabuleiro[linha][coluna] = "X"
    else: 
        tabuleiro[linha][coluna] = "-"
    return tabuleiro

#Posiciona Frota 
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


#Embarcações afundadas 
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
                if tabuleiro[x][y] == 'X':
                    posição_navio += 1 
                if posição_navio == len(navios):
                    afundados += 1 
    return afundados  


#Posição Válida
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

#Posicionando Frota
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
    
#Jogadas do jogador e jogadas do inimigo
import random

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto
frota_inimiga = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
tabuleiro_inimigo = posiciona_frota(frota_inimiga)

tabuleiro_jogador = posiciona_frota(frota)

jogando = True 
ataques = []
ataques_inimgo = []
while jogando: 
    jogada_ataque = True
    tabuleiro = monta_tabuleiros(tabuleiro_jogador , tabuleiro_inimigo)
    print(tabuleiro)
    while jogada_ataque:
        jogador_linha = int(input("Digite uma linha de 0 a 9: "))
        while jogador_linha > 9 or jogador_linha < 0:
            print("'Linha inválida!'")
            jogador_linha = int(input("Digite uma linha de 0 a 9: ")) 
        
        jogador_coluna = int(input("Digite uma coluna de 0 a 9: "))
        while jogador_coluna > 9 or jogador_coluna < 0: 
            print('Coluna inválida!')
            jogador_coluna = int(input("Digite uma coluna de 0 a 9: "))
        
        if [jogador_linha , jogador_coluna] not in ataques:
            ataques.append([jogador_linha, jogador_coluna])
            jogada_ataque = False
        
        else:
            print('A posição da {0} e coluna {1} já foi informada anteriormente'.format(jogador_linha , jogador_coluna))
    
    tabuleiro_inimigo = faz_jogada(tabuleiro_inimigo , jogador_linha , jogador_coluna)
    número_afundados = afundados(frota_inimiga,tabuleiro_inimigo)
    
    if número_afundados == 10: 
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False  
    
    elif número_afundados < 10:
        inimigo = True
        while inimigo: 
            inimigo_linha = random.randint(0,9)
            inimigo_coluna = random.randint(0,9)
            ataque_i = [inimigo_linha , inimigo_coluna]
            if ataque_i not in ataques_inimgo:
                ataques_inimgo.append(ataque_i)
                inimigo = False
                print('Seu oponente está atacando na linha {0} e coluna {1}'.format(inimigo_linha , inimigo_coluna))
        tabuleiro_jogador = faz_jogada(tabuleiro_jogador , inimigo_linha , inimigo_coluna)
        afundados_inimigo = afundados(frota , tabuleiro_jogador)

        if afundados_inimigo == 10: 
            jogando = False
            print('Xi! O oponente derrubou toda a sua frota =(')

        

      
          
