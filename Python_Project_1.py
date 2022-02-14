#PROJETO 1 - JOGO DA VELHA
"""""
A proposta aqui é a elaboração de uma partida de jogo da velha, a ser jogada em duplas. 

O jogo é jogado em um tabuleiro 3x3 por dois jogadores. O primeiro jogador é representado pelo símbolo **O**, enquanto o segundo jogador utiliza o símbolo **X**. 
As jogadas são alternadas, preenchendo uma posição com o seu respectivo símbolo, sempre começando pelo jogador com o símbolo **O**. 
Ganha o jogador que conseguir colocar 3 símbolos em linha no tabuleiro, seja na vertical, horizontal ou diagonal.  

O seu objetivo nesse projeto é criar um jogo da velha em Python, onde os jogadores poderão informar suas posições pelo teclado e o tabuleiro será mostrado com um print após cada jogada. 
Não serão utilizadas bibliotecas
"""""


def marca_posicao(p): #Função que marca o simbolo do jogador na posição escolhida
    if n_jog==1:
        posicao[p-1]=jogador1
    else:
        posicao[p-1]=jogador2
        return posicao
def verificador_vitoria(PJ1,PJ2): #Função que verifica se cada uma das soluções possiveis se encontra na lista de posições ocupadas por cada jogador
    if len(PJ1)>=3: #Verificar se o primeiro jogador ja fez pelo menos tres jogadas (minimo para ganhar))
        if all(x in PJ1 for x in sol1) or all(x in PJ1 for x in sol2) or all(x in PJ1 for x in sol3) or all(x in PJ1 for x in sol4) or all(x in PJ1 for x in sol5) or all(x in PJ1 for x in sol6) or all(x in PJ1 for x in sol7) or all(x in PJ1 for x in sol8): 
            print('Vitória do Jogador 1 (',jogador1,')')
        elif all(x in PJ2 for x in sol1) or all(x in PJ2 for x in sol2) or all(x in PJ2 for x in sol3) or all(x in PJ2 for x in sol4) or all(x in PJ2 for x in sol5) or all(x in PJ2 for x in sol6) or all(x in PJ2 for x in sol7) or all(x in PJ2 for x in sol8):
            print('Vitória do Jogador 2 (',jogador2,')')
        elif len(PJ1)==5: #Verifica se o jogador 1 (ultimo a jogar) ja fez todas as jogadas possiveis, caso não tenha havido vitórias
            print('Empate')
        else:
            return False
    else:
        return False
def verificador_jogada(p): #Verifica se a casa marcada está vazia
    if posicao[p-1]==' ' or posicao[p-1]=='_':
        return True
    else:
        return False
def novo_jogo(): #Função que verifica se o usuário vai querer jogar novamente
    while True:
        njogo=input('Deseja jogar novamente? (s/n) ')
        njogo=njogo.upper()
        if njogo=='S':
            break
        elif njogo=='N':
            return False
        else:
            print('Entrada inválida. Por favor selecione s (sim) ou n (não) ')
sol1=[1,2,3] #Resultados de posições possíveis para vitóra
sol2=[4,5,6]
sol3=[7,8,9]
sol4=[1,4,7]
sol5=[2,5,8]
sol6=[3,6,9]
sol7=[1,5,9]
sol8=[3,5,7]
jogador1='O'
jogador2='X'
novamente=True
while novamente==True:
    posicao=[' ',' ',' ','_','_','_','_','_','_'] #Tabuleiro vazio
    i=0
    posicoes_j1=[] #Listas que vão armazenar as posições marcadas por cada jogador
    posicoes_j2=[]
    pos = int(input("Jogador 1, digite a posição que deseja jogar (de 1 a 9, exemplo abaixo):\n_7_|_8_|_9_\n_4_|_5_|_6_\n 1 | 2 | 3  "))
    while True: #Inicia o jogo
        while verificador_jogada(pos)==False: #Verifica se a jogada é possível
            pos=int(input('Posição ja ocupada. Por favor, jogue novamente '))
        n_jog=(i%2)+1 #Determina qual o jogador da vez (resulta apenas em 1 ou 2)
        marca_posicao(pos)
        print('_',posicao[6],'_|_',posicao[7],'_|_',posicao[8],'_\n_',posicao[3],'_|_',posicao[4],'_|_',posicao[5],'_\n ',posicao[0],' | ',posicao[1],' | ',posicao[2],'  ')
        if n_jog==1: #Determina qual jogador está jogando
            posicoes_j1.append(pos) #Marca a posição escolhida  pelo jogador 1 na lista 
            if verificador_vitoria(posicoes_j1,posicoes_j2)==False: #Verifica se a condição de vitória foi atingida
                pos=int(input('Jogador 2, digite a posição que deseja jogar: ')) #inicia a próxima jogada
            else:
                if novo_jogo()==False: #Interrompe o laço caso o usuário não queira jogar novamente
                    novamente=False 
                break
        else:
            posicoes_j2.append(pos) #Marca a posição escolhida pelo jogador 2 na lista
            if verificador_vitoria(posicoes_j1,posicoes_j2)==False:
                pos=int(input('Jogador 1, digite a posição que deseja jogar: '))
            else:
                if novo_jogo()==False:
                    novamente=False
                break
        i=i+1
print('FIM DE JOGO')