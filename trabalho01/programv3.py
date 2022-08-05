#!/usr/bin/env python3

#imports
from random import randint
from plotlib_programv3 import plotRealEnv, plotRobEnv, plotPlanningMap

#Criação da Class Ambiente.
class envClass:

    def __init__(self):

        #abrindo o arquivo que foi passado com as informações do ambiente
        self.arquivo = open('entradas', 'r')

        #Criando lista que receberá as informações do arquivo
        informacoes_do_ambiente = []

        for linha in self.arquivo:

            #limpando a linha, retirando caracteres que não vamo usar e garantido que seja um numero inteiro
            linha = int(linha.strip())

            #adicionando ao final da minha lista os dados do arquvio
            informacoes_do_ambiente.append(linha)

        #fechando o arquivo
        self.arquivo.close()

        #Passando as informações para as variáveis

        self.nbRow = informacoes_do_ambiente[0]
        self.nbCol = informacoes_do_ambiente[1]

        #Gerando o mapa inicial preenchido com zeros
        envMaptoPlot = []
        line = []
        for i in range(self.nbRow):
            line = []
            for j in range(self.nbCol):
                line.append(0)
            envMaptoPlot.append(line)

        #Atributo Self.map recebe o mapa do ambiente vazio

        self.map = envMaptoPlot

    def imprime(self):
        #Teste para imprimir os dados do arquivo representando o ambiente conhecido pelo robô.
        print('O numero de colunas é {} e o tipo do dado é {}'.format(self.nbCol,type(self.nbCol)))
        print('O numero de linhas é {} e o tipo do dado é {}'.format(self.nbRow,type(self.nbRow)))
        print(self.map)
        print('Esse é o mapa atual do meu ambiente {}'.format(self.map))

    def mapa_ambiente(self):
        #função que retona o mapa do ambiente
        return self.map

    def addObstacle(self, linha, coluna):
        #Metodo do objeto ambiente para adicionar os obstáculos

        #Checando se o valor esta detro da área do mapa
        if (0 <= linha < self.nbRow and 0 <= coluna < self.nbCol):
            self.map[linha][coluna] = -1

        #Saídas caso esteja fora do range do mapa
        if (linha >= self.nbRow or linha < 0):
            print('Você digitou um valor de linha fora do range. Precisa ser um valor entre 0 e {}'.format(self.nbRow))
        if (coluna >= self.nbRow or coluna < 0):
            print('Você digitou um valor de coluna fora do range. Precisa ser um valor entre 0 e {}'.format(self.nbCol))

    def subObstacle(self, linha, coluna):
        #Metodo do objeto ambiente para remover os obstáculos

        #Checando se o valor esta detro da área do mapa
        if (0 <= linha < self.nbRow and 0 <= coluna < self.nbCol):
            self.map[linha][coluna] = 0

        #Saidas caso esteja fora do range do mapa
        if (linha >= self.nbRow or linha < 0):
            print('Você digitou um valor de linha fora do range. Precisa ser um valor entre 0 e {}'.format(self.nbRow))
        if (coluna >= self.nbRow or coluna < 0):
            print('Você digitou um valor de coluna fora do range. Precisa ser um valor entre 0 e {}'.format(self.nbCol))


#Criação da classe robô
class robot:
    
    def __init__(self):

        #abrindo o arquivo que foi passado com as informações do ambiente
        self.arquivo = open('robot', 'r')

        #Criando lista que receberá as informações do arquivo
        informacoes_do_robo = []

        for linha in self.arquivo:
            # print(linha,linha.strip())
            #limpando a linha, retirando caracteres que não vamo usar e garantido que seja um numero inteiro
            linha = int(linha.strip())

            #adicionando ao final da minha lista os dados do arquvio
            informacoes_do_robo.append(linha)

        #fechando o arquivo
        self.arquivo.close()

        #iniciando os atributos da classe

        self.nbRow = informacoes_do_robo[0]
        self.nbCol = informacoes_do_robo[1]
        self.posicao_atual_do_robo_linha = informacoes_do_robo[2]
        self.posicao_atual_do_robo_coluna = informacoes_do_robo[3]
        self.destino_linha = randint(0,self.nbRow -1)
        self.destino_coluna = randint(0,self.nbCol -1)
        self.sensorRange = informacoes_do_robo[4]
        self.mapa_do_robo = []
        self.mapa_de_potenciais = []
        self.movimentacao = 1
        self.path = []

        #Gera o mapa inicial do Robo com zeros
        envMaptoPlot = []
        line = []
        for i in range(self.nbRow):
            line = []
            for j in range(self.nbCol):
                line.append(0)
            envMaptoPlot.append(line)

        #Preenchendo o mapa do robo  com zeros
        self.mapa_do_robo = envMaptoPlot[:]

        #Gera o mapa inicial do potências com zeros
        envMaptoPlot = []
        line = []
        for i in range(self.nbRow):
            line = []
            for j in range(self.nbCol):
                line.append(0)
            envMaptoPlot.append(line)

        #Preenchendo o mapa de potênciais com zeros
        self.mapa_de_potenciais = envMaptoPlot[:]

    def imprime(self):
        #Teste para imprimir os dados do arquivo representando o ambiente conhecido pelo robô.
        print('O numero de colunas é {} e o tipo do dado é {}'.format(self.nbCol,type(self.nbCol)))
        print('O numero de linhas é {} e o tipo do dado é {}'.format(self.nbRow,type(self.nbRow)))
        print('A posicao atual: linha {} e coluna {}'.format(self.posicao_atual_do_robo_linha,self.posicao_atual_do_robo_coluna))
        print('O valor de leitura do sensor é {} casas'.format(self.sensorRange))
        print(self.mapa_do_robo)


    def posicao_desejada(self, fimx, fimy):
        #Definir a posicao que se deseja chegar

        #Checando se o valor esta dentro da area do mapa
        if (0 <= fimx < self.nbRow and 0 <= fimy < self.nbCol):
            self.mapa_do_robo[fimx][fimy] = 1
            self.destino_linha = fimx
            self.destino_coluna = fimy
            #print('Nova posicao: Linha {} e coluna {}'.format(self.destino_linha,self.destino_coluna))

        #Saidas caso esteja fora do range do mapa
        if (fimx >= self.nbRow or fimx < 0):
            print('Você digitou um valor de linha fora do range. Precisa ser um valor entre 0 e {}'.format(self.nbRow))
        if (fimy >= self.nbRow or fimy < 0):
            print('Você digitou um valor de coluna fora do range. Precisa ser um valor entre 0 e {}'.format(self.nbCol))

    def varredura(self, mapa):
        #Sente a presenca ou não de um obstaculo e atualiza o mapa do robô. A entrada mapa representa uma lista com o mapa atual do robô

        #Range_de_varredura_linha recebe uma lista que representa o range de visão horizontal do robô

        range_de_varredura_linha = list(range(self.posicao_atual_do_robo_linha - self.sensorRange, self.posicao_atual_do_robo_linha + self.sensorRange +1))

        #Interseção linha. Aqui garantimso que o robôs so consiga ver dentro do ambiente. Ele não pode ver além do tamanho do ambiente.
        #Fazemos uma interseção do quanto ele pode ver e o tamanho do ambiente

        lista_auxiliar_linha = []
        for i in range(self.nbRow):
            if i in range_de_varredura_linha:
                lista_auxiliar_linha.append(i)
        range_de_varredura_linha_filtrada = lista_auxiliar_linha.copy()

        #Range_de_varredura_coluna recebe uma lista que representa o range de visão vertical do robô

        range_de_varredura_coluna = list(range(self.posicao_atual_do_robo_coluna - self.sensorRange, self.posicao_atual_do_robo_coluna + self.sensorRange +1))

        #interseção coluna. Aqui garantimso que o robôs so consiga ver dentro do ambiente. Ele não pode ver além do tamanho do ambiente.
        #Fazemos uma interseção do quanto ele pode ver e o tamanho do ambiente

        lista_auxiliar_coluna = []
        for i in range(self.nbRow):
            if i in range_de_varredura_coluna:
                lista_auxiliar_coluna.append(i)
        range_de_varredura_coluna_filtrada = lista_auxiliar_coluna.copy()

        #Atualizar o mapa conhecido pelo robô com as informações que ele varreu do ambiente

        for i in range_de_varredura_linha_filtrada:
            for j in range_de_varredura_coluna_filtrada:
                if self.mapa_do_robo[i][j] != 1:
                    self.mapa_do_robo[i][j] = mapa[i][j]

    def caminho(self):

        #montar matriz de mapa_de_potenciais inicial
        self.mapa_de_potenciais[self.destino_linha][self.destino_coluna] = 1

        for i in range(self.nbRow):

            for j in range(self.nbCol):
                self.mapa_de_potenciais[i][j] = abs((self.destino_linha - i)) + abs((self.destino_coluna -j)) +1

        #atualizando o mapa de potênciais com os valores conhecidos pelo robô
        for i in range(self.nbRow):
            for j in range(self.nbCol):
                if self.mapa_do_robo[i][j] == -1:
                    self.mapa_de_potenciais[i][j] = -1
        

        #planejando o caminho

        #Aqui o passamos os valores do mapa de potênciais nas posições que o robô pode se mover para uma lista

        possiveis_movimentacao_campo = [self.mapa_de_potenciais[self.posicao_atual_do_robo_linha -self.movimentacao][self.posicao_atual_do_robo_coluna],
        self.mapa_de_potenciais[self.posicao_atual_do_robo_linha +self.movimentacao][self.posicao_atual_do_robo_coluna],
        self.mapa_de_potenciais[self.posicao_atual_do_robo_linha][self.posicao_atual_do_robo_coluna -self.movimentacao],
        self.mapa_de_potenciais[self.posicao_atual_do_robo_linha][self.posicao_atual_do_robo_coluna +self.movimentacao]]

         #Aqui o passamos para uma lista as possiveis coordenadas das movimentações do robô de a cordo com a posição atual dele

        possiveis_movimentacao = [[self.posicao_atual_do_robo_linha -self.movimentacao ,self.posicao_atual_do_robo_coluna],
        [self.posicao_atual_do_robo_linha +self.movimentacao,self.posicao_atual_do_robo_coluna],
        [self.posicao_atual_do_robo_linha,self.posicao_atual_do_robo_coluna -self.movimentacao],
        [self.posicao_atual_do_robo_linha,self.posicao_atual_do_robo_coluna +self.movimentacao]]

        #print(possiveis_movimentacao)

        for i in range(0,4):
            if self.mapa_de_potenciais[self.posicao_atual_do_robo_linha][self.posicao_atual_do_robo_coluna] > possiveis_movimentacao_campo[i] and possiveis_movimentacao_campo[i] != -1:
                self.path.append(possiveis_movimentacao[possiveis_movimentacao_campo.index(possiveis_movimentacao_campo[i])])
                nova_posicao_robo = possiveis_movimentacao[possiveis_movimentacao_campo.index(possiveis_movimentacao_campo[i])]
                break

        return nova_posicao_robo

    def move(self,nova_posicao):
        
        #metodo para mover o robô

        self.posicao_atual_do_robo_linha = nova_posicao[0]
        self.posicao_atual_do_robo_coluna = nova_posicao[1]



####### MAIN ######

#Criando o objeto ambiente
ambiente1 = envClass()

#Adicionando obstáculos aleatórios ao ambiente
for i in range(0,30):
    ambiente1.addObstacle(randint(0,ambiente1.nbRow -1),randint(0,ambiente1.nbCol -1))

#Variável que recebe o mapa do ambiente
mapa_ambiente1 = ambiente1.mapa_ambiente()

#criando o objeto robo
robo = robot()

#plotando o ambiente real
plotRealEnv(ambiente1,robo)

#inicio da movimentação do robô

while ((robo.destino_linha != robo.posicao_atual_do_robo_linha) or (robo.destino_coluna != robo.posicao_atual_do_robo_coluna)):
    #atualiza o mapa do robô

    robo.varredura(mapa_ambiente1)
    proximo_passo = robo.caminho()
    robo.move(proximo_passo)

    ##plotando o ambiente conhecido do robô
    plotRobEnv(robo)

