#!/usr/bin/env python3

#Aqui vou fazer os testes do programa

#imports

#Ambiente.
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

        self.nbRow = informacoes_do_ambiente[0]
        self.nbCol = informacoes_do_ambiente[1]

        #Mapa inicial
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
        print(self.map)

    def mapa_ambiente(self):
        return self.map

    def addObstacle(self, linha, coluna):
        #Metodo do objeto para adicionar os obstáculos
        if (0 <= linha <= self.nbRow and 0 <= coluna <= self.nbCol):
            self.map[linha][coluna] = -1

        if (linha > self.nbRow or linha < 0):
            print('Você digitou um valor de linha fora do range. Precisa ser um valor entre 0 e {}'.format(self.nbRow))
        if (coluna > self.nbRow or coluna < 0):
            print('Você digitou um valor de coluna fora do range. Precisa ser um valor entre 0 e {}'.format(self.nbCol))

    def subObstacle(self, linha, coluna):
        #Metodo do objeto para remover os obstáculos
        if (0 <= linha <= self.nbRow and 0 <= coluna <= self.nbCol):
            self.map[linha][coluna] = 0

        if (linha > self.nbRow or linha < 0):
            print('Você digitou um valor de linha fora do range. Precisa ser um valor entre 0 e {}'.format(self.nbRow))
        if (coluna > self.nbRow or coluna < 0):
            print('Você digitou um valor de coluna fora do range. Precisa ser um valor entre 0 e {}'.format(self.nbCol))

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

        self.nbRow = informacoes_do_robo[0]
        self.nbCol = informacoes_do_robo[1]
        self.position_row = informacoes_do_robo[2]
        self.position_col = informacoes_do_robo[3]
        self.end_row = 0
        self.end_col = 0
        self.sensorRange = informacoes_do_robo[4]
        self.map_robot = []
        self.plan = []

        #Mapa inicial
        envMaptoPlot = []
        line = []
        for i in range(self.nbRow):
            line = []
            for j in range(self.nbCol):
                line.append(0)
            envMaptoPlot.append(line)

        self.map_robot = envMaptoPlot

    def imprime(self):
        #Teste para imprimir os dados do arquivo prinade representando o ambiente conhecido pelo robô.
        print('O numero de colunas é {} e o tipo do dado é {}'.format(self.nbCol,type(self.nbCol)))
        print('O numero de linhas é {} e o tipo do dado é {}'.format(self.nbRow,type(self.nbRow)))
        print('A posicao inicial: linha {} e coluna {}'.format(self.position_row,self.position_col))
        print('O valor de leitura do sensor é {} casas'.format(self.sensorRange))
        print(self.map_robot)


    def posicao_desejada(self, fimx, fimy):
        #Definir a posicao que se deseja chegar
        self.end_row = fimx
        self.end_col = fimy
        print('Nova posicao: Linha {} e coluna {}'.format(self.end_row,self.end_row))

    def varredura(self, Mapa):
        #Sente a presenca ou nao de um obstaculo
        for i in range(self.position_row - self.sensorRange, self.position_row + self.sensorRange +1):
            line = []
            for j in range(self.position_col - self.sensorRange, self.position_col + self.sensorRange +1):
                line.append(Mapa[i][j])
            self.map_robot.append(line)
        print(self.map_robot)

    def caminho(self):
        pass


## FUNCAO PRINCIPAL DE CHAMADA

#Criando o objeto ambient
ambiente1 = envClass()
ambiente1.imprime()
ambiente1.addObstacle(7,2)
ambiente1.addObstacle(8,3)
mapa_aux = ambiente1.mapa_ambiente()

robo = robot()
robo.imprime()
robo.posicao_desejada(8,8)
robo.varredura(mapa_aux)
