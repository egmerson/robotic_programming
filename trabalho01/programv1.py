#Aqui vou fazer os testes do programa

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
        #self.map =

    def imprime(self):
        #Teste para imprimir os dados do arquivo
        print('O numero de colunas é {} e o tipo do dado é {}'.format(self.nbCol,type(self.nbCol)))
        print('O numero de linhas é {} e o tipo do dado é {}'.format(self.nbRow,type(self.nbRow)))

    def addObstacle(self):
        #Metodo do objeto para adicionar os obstáculos
        pass

    def subObstacle(self):
        #Metodo do objeto para remover os obstáculos
        pass