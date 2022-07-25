#!/usr/bin/env python3


#Aqui vou fazer os testes do programa

#imports

#import numpy as np

#Ambiente. 
class envClass:

    def __init__(self):

        #abrindo o arquivo que foi passado com as informações do ambiente
        self.arquivo = open('entradas', 'r')
        
        #Criando lista que receberá as informações do arquivo
        informacoes_do_ambiente = []

        for linha in self.arquivo:

            #limpando a linha, retirando caracteres que não vamos usar e garantido que seja um numero inteiro
            linha = int(linha.strip())

            #adicionando ao final da minha lista os dados do arquvio
            informacoes_do_ambiente.append(linha)
        
        #fechando o arquivo
        self.arquivo.close()
        
        self.nbRow = informacoes_do_ambiente[0]
        self.nbCol = informacoes_do_ambiente[1]

	#Preenchendo o mapa com zeros
        mapa = []
        linha2 = []
        for i in range(self.nbRow):
	    linha2 = []
	    for j in range(self.nbCol):
	        linha2.append(0)
	        mapa.append(linha2)
	self.map = mapa

    def imprime(self):
        #Teste para imprimir os dados do arquivo
        print('O numero de colunas é {} e o tipo do dado é {}'.format(self.nbCol,type(self.nbCol)))
        print('O numero de linhas é {} e o tipo do dado é {}'.format(self.nbRow,type(self.nbRow)))

    def addObstacle(self, linha, coluna):
        #Metodo do objeto para adicionar os obstáculos
        self.map[linha][coluna] = -1

    def subObstacle(self, linha, coluna):
        #Metodo do objeto para remover os obstáculos
        self.map[linha][coluna] = 0

