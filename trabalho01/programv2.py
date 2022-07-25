#!/usr/bin/env python3

#Aqui vou fazer os testes do programa

#imports
from plotlib_programv2 import plotRealEnv, plotRobEnv, plotPlanningMap

#Criação da Class Ambiente.
class envClass:

    def __init__(self):

        #abrindo o arquivo que foi passado com as informações do ambiente
        self.arquivo = open('entradas.txt', 'r')

        #Criando lista que receberá as informações do arquivo
        informacoes_do_ambiente = []

        for linha in self.arquivo:

            #limpando a linha, retirando caracteres que não vamo usar e garantido que seja um numero inteiro
            linha = int(linha.strip())

            #adicionando ao final da minha lista os dados do arquvio
            informacoes_do_ambiente.append(linha)

        #fechando o arquivo
        self.arquivo.close()

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

        self.map = envMaptoPlot

    def imprime(self):
        #Teste para imprimir os dados do arquivo prinade representando o ambiente conhecido pelo robô.
        print('O numero de colunas é {} e o tipo do dado é {}'.format(self.nbCol,type(self.nbCol)))
        print('O numero de linhas é {} e o tipo do dado é {}'.format(self.nbRow,type(self.nbRow)))
        print('Esse é o mapa atual do meu ambiente {}'.format(self.map))

    def mapa_ambiente(self):
        
        return self.map

    def addObstacle(self, linha, coluna):
        #Metodo do objeto para adicionar os obstáculos

        #Checando se o valor esta detro da área do mapa
        if (0 <= linha < self.nbRow and 0 <= coluna < self.nbCol):
            self.map[linha][coluna] = -1

        #Saidas caso esteja fora do range do mapa
        if (linha >= self.nbRow or linha < 0):
            print('Você digitou um valor de linha fora do range. Precisa ser um valor entre 0 e {}'.format(self.nbRow))
        if (coluna >= self.nbRow or coluna < 0):
            print('Você digitou um valor de coluna fora do range. Precisa ser um valor entre 0 e {}'.format(self.nbCol))

    def subObstacle(self, linha, coluna):
        #Metodo do objeto para remover os obstáculos

        #Checando se o valor esta detro da área do mapa
        if (0 <= linha < self.nbRow and 0 <= coluna < self.nbCol):
            self.map[linha][coluna] = 0

        #Saidas caso esteja fora do range do mapa
        if (linha >= self.nbRow or linha < 0):
            print('Você digitou um valor de linha fora do range. Precisa ser um valor entre 0 e {}'.format(self.nbRow))
        if (coluna >= self.nbRow or coluna < 0):
            print('Você digitou um valor de coluna fora do range. Precisa ser um valor entre 0 e {}'.format(self.nbCol))

class robot:

    def __init__(self):

        #abrindo o arquivo que foi passado com as informações do ambiente
        self.arquivo = open('robot.txt', 'r')

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

        self.nbRow = informacoes_do_robo[0]
        self.nbCol = informacoes_do_robo[1]
        self.posicao_atual_do_robo_linha = informacoes_do_robo[2]
        self.posicao_atual_do_robo_coluna = informacoes_do_robo[3]
        self.destino_linha = 0
        self.destino_coluna = 0
        self.sensorRange = informacoes_do_robo[4]
        self.mapa_do_robo = []
        self.plan = []

        #Gera o mapa inicial do Robo com zeros
        envMaptoPlot = []
        line = []
        for i in range(self.nbRow):
            line = []
            for j in range(self.nbCol):
                line.append(0)
            envMaptoPlot.append(line)

        self.mapa_do_robo = envMaptoPlot

    def imprime(self):
        #Teste para imprimir os dados do arquivo prinade representando o ambiente conhecido pelo robô.
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
            print('Nova posicao: Linha {} e coluna {}'.format(self.destino_linha,self.destino_coluna))

        #Saidas caso esteja fora do range do mapa
        if (fimx >= self.nbRow or fimx < 0):
            print('Você digitou um valor de linha fora do range. Precisa ser um valor entre 0 e {}'.format(self.nbRow))
        if (fimy >= self.nbRow or fimy < 0):
            print('Você digitou um valor de coluna fora do range. Precisa ser um valor entre 0 e {}'.format(self.nbCol))

    def varredura(self, mapa):
        #Sente a presenca ou não de um obstaculo e atualiza o mapa do robô. A entrada mapa representa uma lista com o mapa atual do robô

        range_de_varredura_linha = list(range(self.posicao_atual_do_robo_linha - self.sensorRange, self.posicao_atual_do_robo_linha + self.sensorRange +1))
        print(range_de_varredura_linha)

        #Interseção linha

        lista_auxiliar_linha = []
        for i in range(self.nbRow):
            if i in range_de_varredura_linha:
                lista_auxiliar_linha.append(i)
        range_de_varredura_linha_filtrada = lista_auxiliar_linha.copy()
        print(range_de_varredura_linha_filtrada)

        range_de_varredura_coluna = list(range(self.posicao_atual_do_robo_coluna - self.sensorRange, self.posicao_atual_do_robo_coluna + self.sensorRange +1))
        print(range_de_varredura_coluna)

        #interseção coluna

        lista_auxiliar_coluna = []
        for i in range(self.nbRow):
            if i in range_de_varredura_coluna:
                lista_auxiliar_coluna.append(i)
        range_de_varredura_coluna_filtrada = lista_auxiliar_coluna.copy()
        print(range_de_varredura_coluna_filtrada)

        for i in range_de_varredura_linha_filtrada:
            for j in range_de_varredura_coluna_filtrada:
                if self.mapa_do_robo[i][j] != 1:
                    self.mapa_do_robo[i][j] = mapa[i][j]
        print(self.mapa_do_robo)

    def caminho(self):
        pass


####### Inicio das Chamadas ######

#Criando o objeto ambiente
ambiente1 = envClass()
#Imprime o ambiente
ambiente1.imprime()
#adicionando obstáculos
ambiente1.addObstacle(1,1)
ambiente1.addObstacle(0,1)
ambiente1.addObstacle(5,5)
ambiente1.addObstacle(4,5)
#variável qie recebe o mapa horiginal do ambiente
mapa_ambiente1 = ambiente1.mapa_ambiente()

#criando o objeto robo
robo = robot()
#imprime as informações do objeto robô
robo.imprime()
#adiciona a posição desejada
robo.posicao_desejada(3,3)
#atualiza o mapa do robô
robo.varredura(mapa_ambiente1)

#plotando o ambiente real
plotRealEnv(ambiente1,robo)

##plotando o ambiente conhecido do robô
plotRobEnv(robo)