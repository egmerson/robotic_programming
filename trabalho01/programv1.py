#Aqui vou fazer os testes do programa

#imports

#Ambiente. 
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
        #Teste para imprimir os dados do arquivo
        print('O numero de colunas é {} e o tipo do dado é {}'.format(self.nbCol,type(self.nbCol)))
        print('O numero de linhas é {} e o tipo do dado é {}'.format(self.nbRow,type(self.nbRow)))
        print(self.map)

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
            self.map[linha][coluna] = -1

        if (linha > self.nbRow or linha < 0):
            print('Você digitou um valor de linha fora do range. Precisa ser um valor entre 0 e {}'.format(self.nbRow))
        if (coluna > self.nbRow or coluna < 0):
            print('Você digitou um valor de coluna fora do range. Precisa ser um valor entre 0 e {}'.format(self.nbCol))