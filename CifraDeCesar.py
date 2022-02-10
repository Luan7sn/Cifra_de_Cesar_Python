import random
import os

class CifraDeCesar:
    #Construtor
    def __init__(self, caracteresPossiveis):
        self.caracteresPossiveis = caracteresPossiveis

    #Método para criptografar uma string com um único caractere / str, int -> str
    def criptografar(self, caractereDeEntrada, chave):
        if len(caractereDeEntrada) != 1:
            return print("String de entrada incompatível")
        else:
            if caractereDeEntrada in self.caracteresPossiveis:
                #Filtrando a chave
                if chave > 70:
                    filtro = int(chave / 70)
                    chave = chave - 70 * filtro
                posicao = self.caracteresPossiveis.find(caractereDeEntrada)
                #Verificando a string de forma circular
                if chave > (len(self.caracteresPossiveis) - (posicao + 1)):
                    caractereDeSaida = self.caracteresPossiveis[chave - (len(self.caracteresPossiveis) - posicao)]
                else:
                    caractereDeSaida = self.caracteresPossiveis[posicao + chave]
            else:
                caractereDeSaida = caractereDeEntrada
        #Retornando o caractere criptografado
        print("Caractere criptografado: " + caractereDeSaida)
        return caractereDeSaida
    
    #Método para descriptografar uma string com um único caractere / str, int -> str
    def descriptografar(self, caractereDeEntrada, chave):
        if len(caractereDeEntrada) != 1:
            return print("String de entrada incompatível")
        else:
            if caractereDeEntrada in self.caracteresPossiveis:
                #Filtrando a chave
                if chave > 70:
                    filtro = int(chave / 70)
                    chave = chave - 70 * filtro
                posicao = self.caracteresPossiveis.find(caractereDeEntrada)
                #Verificando a string de forma circular
                if chave > (posicao + 1):
                    caractereDeSaida = self.caracteresPossiveis[(len(self.caracteresPossiveis) - chave + posicao)]
                else:
                    caractereDeSaida = self.caracteresPossiveis[posicao - chave]
            else:
                caractereDeSaida = caractereDeEntrada
        #Retornando o caractere descriptografado
        print("Caractere descriptografado: " + caractereDeSaida)
        return caractereDeSaida

    #Método para criptografar um arquivo / str, int -> sem retorno
    def criptografarArquivo(self, nomeDoArquivo, chave):
        #Verificando se chave está dentro dos limites estabelecidos e randomizando se não estiver
        if chave < -70 or chave > 70:
            chave = random.randint(-70, 70)
            while chave == 0:
                chave = random.randint(-70, 70)
        #Tratamento de exceção
        try:
            arquivoDeEntrada = open(nomeDoArquivo, "r")
        except FileNotFoundError:
            print("O arquivo não foi encontrado!")
            print("Digite 1 para finalizar o programa: ")
            finalizar = input()
            if finalizar == 1:
                return 0
        finally:
            arquivoDeEntrada.close()
        #Abrindo arquivo
        arquivoDeEntrada = open(nomeDoArquivo, "r")
        #Separando o nome da extensão para utilizar no novo arquivo
        nomes = nomeDoArquivo.split(".")
        nome = nomes[0]
        arquivoDeSaida = open(nome + "Cripto.txt", "w")
        #Lendo um caractere
        caractereDeEntrada = arquivoDeEntrada.read(1)
        InstanciaCifra = CifraDeCesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ#$&*@().:,!?[]=+-%" + "abcdefghijklmnopqrstuvwxyz")
        #Lendo o arquivo inteiro e criptografando
        while caractereDeEntrada != "":
            arquivoDeSaida.write(InstanciaCifra.criptografar(caractereDeEntrada, chave))
            caractereDeEntrada = arquivoDeEntrada.read(1)
        #Fechando os arquivos
        arquivoDeEntrada.close()
        arquivoDeSaida.close()
        print("Chave utilizada: " + str(chave))
        print("Digite 1 para finalizar o programa: ")
        finalizar = input()
        if finalizar == 1:
            return 0

    #Método para descriptografar um arquivo / str, int -> sem retorno
    def descriptografarArquivo(self, nomeDoArquivo, chave):
        #Verificando se chave está dentro dos limites estabelecidos e randomizando se não estiver
        if chave < -70 or chave > 70:
            chave = random.randint(-70, 70)
            while chave == 0:
                chave = random.randint(-70, 70)
        #Tratamento de exceção
        try:
            arquivoDeEntrada = open(nomeDoArquivo, "r")
        except FileNotFoundError:
            print("O arquivo não foi encontrado!")
            print("Digite 1 para finalizar o programa: ")
            finalizar = input()
            if finalizar == 1:
                return 0
        finally:
            arquivoDeEntrada.close()
        #Abrindo arquivo
        arquivoDeEntrada = open(nomeDoArquivo, "r")
        #Separando o nome da extensão para utilizar no novo arquivo
        nomes = nomeDoArquivo.split(".")
        nome = nomes[0]
        arquivoDeSaida = open(nome + "Cripto.txt", "w")
        #Lendo um caractere
        caractereDeEntrada = arquivoDeEntrada.read(1)
        InstanciaCifra = CifraDeCesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ#$&*@().:,!?[]=+-%" + "abcdefghijklmnopqrstuvwxyz")
        #Lendo o arquivo inteiro e criptografando
        while caractereDeEntrada != "":
            arquivoDeSaida.write(InstanciaCifra.descriptografar(caractereDeEntrada, chave))
            caractereDeEntrada = arquivoDeEntrada.read(1)
        #Fechando os arquivos
        arquivoDeEntrada.close()
        arquivoDeSaida.close()
        print("Chave utilizada: " + str(chave))
        print("Digite 1 para finalizar o programa: ")
        finalizar = input()
        if finalizar == 1:
            return 0
    
    #Método para criptografar um arquivo e escrever no mesmo arquivo / str, int -> sem retorno
    def criptografarMesmoArquivo(self, nomeDoArquivo, chave):
        #Verificando se chave está dentro dos limites estabelecidos e finalizando o programa se não estiver
        if chave < -70 or chave > 70:
            print("A chave é inválida")
            print("Digite 1 para finalizar o programa: ")
            finalizar = input()
            if finalizar == 1:
                return 0
        #Tratamento de exceção
        try:
            arquivoDeEntrada = open(nomeDoArquivo, "r")
        except FileNotFoundError:
            print("O arquivo não foi encontrado!")
            print("Digite 1 para finalizar o programa: ")
            finalizar = input()
            if finalizar == 1:
                return 0
        finally:
            arquivoDeEntrada.close()
        #Abrindo arquivo
        arquivoDeEntrada = open(nomeDoArquivo, "r")
        #Criando um nome arquivo de nome temporário
        arquivoDeSaida = open("Temporario", "w")
        #Criando uma list e lendo uma linha do arquivo
        linhaDeEntrada = []
        linhaDeEntrada = arquivoDeEntrada.readline()
        InstanciaCifra = CifraDeCesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ#$&*@().:,!?[]=+-%" + "abcdefghijklmnopqrstuvwxyz")
        #Lendo o arquivo inteiro linha por linha e criptografando
        while linhaDeEntrada != "":
            #Lendo a linha caractere por caractere e criptografando
            for i in range(len(linhaDeEntrada)):
                arquivoDeSaida.write(InstanciaCifra.criptografar(linhaDeEntrada[i], chave))
            linhaDeEntrada = arquivoDeEntrada.readline()
        #Fechando os arquivos
        arquivoDeEntrada.close()
        arquivoDeSaida.close()
        #Excluindo o arquivo de entrada
        os.remove(nomeDoArquivo)
        #Renomeando o arquivo de saida com o nome do arquivo de entrada
        os.rename("Temporario", nomeDoArquivo)
        print("Chave utilizada: " + str(chave))
        print("Digite 1 para finalizar o programa: ")
        finalizar = input()
        if finalizar == 1:
            return 0

    #NÚMERO DE TESTES UTILIZADOS: 11
    #TESTE  --> caractereDeEntrada -->      < 1
    #                                       = 1
    #                                       > 1
    #TESTE  --> chave -->                   < -70
    #                                       = -70
    #                                       = 0
    #                                       = 70
    #                                       > 70
    #TESTE  --> nomeDoArquivo -->           verdadeiro
    #                                       falso
    #                                       em branco    

def main():
    print("Escolha uma das opções abaixo e digite seu número:\n")
    print("1 - Criptografar caractere")
    print("2 - Descriptografar caractere")
    print("3 - Criptografar arquivo")
    print("4 - Descriptografar arquivo")
    print("5 - Criptografar e sobrescrever no mesmo arquivo")
    escolha = input()
    escolha = int(escolha)
    print(escolha)
    if escolha == 1:
        caractereDeEntrada = input("Digite o caractere a ser criptografado: ")
        chave = int(input("Digite a chave a ser utilizada: "))
        InstanciaCifra = CifraDeCesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ#$&*@().:,!?[]=+-%" + "abcdefghijklmnopqrstuvwxyz")
        InstanciaCifra.criptografar(caractereDeEntrada, chave)
    elif escolha == 2:
        caractereDeEntrada = input("Digite o caractere a ser criptografado: ")
        chave = int(input("Digite a chave a ser utilizada: "))
        InstanciaCifra = CifraDeCesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ#$&*@().:,!?[]=+-%" + "abcdefghijklmnopqrstuvwxyz")
        InstanciaCifra.descriptografar(caractereDeEntrada, chave)
    elif escolha == 3:
        nomeDoArquivo = input("Digite o nome do arquivo: ")
        chave = int(input("Digite a chave a ser utilizada: "))
        InstanciaCifra = CifraDeCesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ#$&*@().:,!?[]=+-%" + "abcdefghijklmnopqrstuvwxyz")
        InstanciaCifra.criptografarArquivo(nomeDoArquivo, chave)
    elif escolha == 4:
        nomeDoArquivo = input("Digite o nome do arquivo: ")
        chave = int(input("Digite a chave a ser utilizada: "))
        InstanciaCifra = CifraDeCesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ#$&*@().:,!?[]=+-%" + "abcdefghijklmnopqrstuvwxyz")
        InstanciaCifra.descriptografarArquivo(nomeDoArquivo, chave)
    elif escolha == 5:
        nomeDoArquivo = input("Digite o nome do arquivo: ")
        chave = int(input("Digite a chave a ser utilizada: "))
        InstanciaCifra = CifraDeCesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ#$&*@().:,!?[]=+-%" + "abcdefghijklmnopqrstuvwxyz")
        InstanciaCifra.criptografarMesmoArquivo(nomeDoArquivo, chave)
    else:
        print("Digite 1 para finalizar o programa: ")
        finalizar = input()
        if finalizar == 1:
            return 0
if __name__ == '__main__':
    main()
