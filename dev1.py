#Código exercício 1 
import random
random.seed(2)

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
                if tabuleiro[x][y] == 'X' :
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

#Código do exercício 7 
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
            orientacao = int(input('[1] vertical [2] horizontal: '))
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
            orientacao = int(input('[1] vertical [2] horizontal: '))
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
            orientacao = int(input('[1] vertical [2] horizontal: '))
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

    #Código exercício 8

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
ataques_oponente = []
while jogando:
    tabuleiro = monta_tabuleiros(tabuleiro_jogador, tabuleiro_inimigo)
    print(tabuleiro)

    ataque = True
    while ataque:
        #Ataque do jogador 
        ataque_l = int(input('Jogador, qual linha deseja atacar? '))

        while ataque_l < 0 or ataque_l > 9:
            print('Linha inválida!')
            ataque_l = int(input('Jogador, qual linha deseja atacar? '))
        ataque_c = int(input('Jogador, qual coluna deseja atacar? '))


        while ataque_c < 0 or ataque_c > 9:
            print('Coluna inválida!')
            ataque_c = int(input('Jogador, qual coluna deseja atacar? '))

        ataque_momento = [ataque_l , ataque_c]

        if ataque_momento not in ataques:
            ataques.append(ataque_momento)
            ataque = False

        else: 
            print(f'A posição linha {ataque_l} e coluna {ataque_c} já foi informada anteriormente!')

    tabuleiro_inimigo = faz_jogada(tabuleiro_inimigo, ataque_l, ataque_c)
    afundou = afundados(frota_inimiga, tabuleiro_inimigo)
    afundou2 = afundados(frota, tabuleiro_jogador)

    if afundou2 != 10:
    
        ataque_oponente = True
        while ataque_oponente:
            #Ataque do oponete 
            ataqueoponente_l = random.randint(0,9) #define a linha de ataque do oponente
            ataqueoponente_c = random.randint(0,9) #define a coluna de ataque do oponente

            ataqueoponente_momento = [ataqueoponente_l, ataqueoponente_c] 
            
            if ataqueoponente_momento not in ataques_oponente: #verifica se a posição de ataque não é repetida
                ataques_oponente.append(ataqueoponente_momento)  #adiciona os ataques no histórico para verificação
                ataque_oponente = False
            
            else:
                while ataqueoponente_momento in ataques_oponente: 

                    ataqueoponente_l = random.randint(0,9)
                    ataqueoponente_c = random.randint(0,9)

                    ataqueoponente_momento = [ataqueoponente_l, ataqueoponente_c]

        
        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, ataqueoponente_l, ataqueoponente_c)
    

    if afundou == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False

    elif afundou2 == 10:
        print('Xi! O oponente derrubou toda a sua frota =(')
        jogando = False

    else:
        print(f'Seu oponente está atacando na linha {ataqueoponente_l} e coluna {ataqueoponente_c}')