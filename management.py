"""
Faça um algoritmo que utilize o menu abaixo:

MENU
======
1- Ler arquivo de jogadores
2- Escalar time
3- Realizar Substiuição
4- Expulsão
5- Imprimir escalação
Escolha:


Opção 1: Ler de um arquivo texto todos os jogadores
        escalados para a copa e armazenar em uma
        lista (lst_jogadores)
        Cada Elemento da lista será uma instância
            da classe Jogador.

Opção 2: Você deverá escalar 11 dos jogadores para
        iniciar a partida.
        Os Jogadores escalados para a partida ficam
            em uma lista (lst_escalados)
            Alterar o atributo 'participou_partida'
                para True
        Os jogadores que não forem escalados para
            iniciar a partida ficam em uma outra
            lista (lst_reserva)
Opção 3: Você poderá realizar a substituição de um
        jogador por outro.
        Quando isso acontecer o jogador vai para
            a lista de Reserva e o outro para a
            lista Escalados.

Opção 4: Caso haja alguma expulsão, o jogador sai
        da lista de Escalados e vai para a lista
        Reserva.

Opção 5: Mostrar a escalação de todos jogadores que
        participaram do jogo, inclusive as substituições
        e expulsões.
        Salve esses dados em um arquivo (todosjogadores.txt)


class Jogador:
    def __init__(self, nome, numero, posicao):
        self.__numero = numero
        self.__nome_jogador = nome
        self.__posicao = posicao # GOLEIRO ou DEFESA ou MEIO-CAMPO ou ATECANTE
        self.__situacao = "NORMAL"  # ou "EXPULSO"
        self.__participou_partida = False # ou True


arquivo texto para leitura (convocados.txt):
1:Alisson:GOLEIRO
2:Danilo:DEFESA
3:Thiago Silva:DEFESA
4:Marquinhos:DEFESA
5:Casemiro:MEIO-CAMPO
6:Alex Sandro:DEFESA
7:Lucas Paquetá:MEIO-CAMPO
8:Fred:MEIO-CAMPO
9:Richarlison:ATACANTE
10:Neymar:ATACANTE
11:Raphinha:ATACANTE
12:Weverton:GOLEIRO
13:Dani Alves:DEFESA
14:Éder Millitão:DEFESA
15:Fabinho:MEIO-CAMPO
16:Alex Telle:DEFESA
17:Bruno Guimarães:MEIO-CAMPO
18:Gabriel Jesus:ATACANTE
19:Antony:ATACANTE
20:Vinicius Junior:ATACANTE
21:Rodrygo:ATACANTE
22:Éverton Ribeiro:MEIO-CAMPO
23:Ederson:GOLEIRO
24:Bremer:DEFESA
25:Pedro:ATACANTE
26:Gabriel Martinelli:ATACANTE
"""

class Jogador:
    def __init__(self, nome, numero, posicao):
        self.__numero = numero
        self.__nome_jogador = nome
        self.__posicao = posicao  # GOLEIRO ou DEFESA ou MEIO-CAMPO ou ATECANTE
        self.__situacao = "NORMAL"  # ou "EXPULSO"
        self.__participou_partida = False  # ou True
        
                
    def escalar_time(self):
        contador = 1
        while contador < 12:
                ind_jogador = (int(input(f"({contador}/11 jogadores)Digite o número do jogador para escalá-lo: ")) - 1)   
                if lst_jogadores[ind_jogador] in lst_escalados:
                        print('Este jogador ja está escalado, escolha outro.')
                
                else:
                        print(f'Você escalou {lst_jogadores[ind_jogador]}')             
                        lst_escalados.append(lst_jogadores[ind_jogador])
                        lst_jogadores[ind_jogador]
                        contador += 1
                    
        for a in lst_jogadores:
                if not a in lst_escalados: 
                    lst_reservas.append(a)
                    
        for a in lst_jogadores:
            if a in lst_escalados:
                a.__participou_partida=True 
                
        
    def realizar_substiuição(self): 
        for ind, escalado in enumerate(lst_escalados):
            print(f"{ind} - {escalado}")
        sai = int(input('Digite o ÍNDICE de quem você deseja substituir: '))
        lst_reservas.append(lst_escalados[sai])
        lst_escalados.pop(sai)
        
        
        for ind, reserva in enumerate(lst_reservas):
            print(f"{ind} - {reserva}")
        entra = int(input("Digite o índice de quem irá entrar: "))
        lst_escalados.append(lst_reservas[entra]) 
        lst_reservas.pop(entra)

        for a in lst_jogadores:
            if a in lst_escalados:
                a.__participou_partida=True 
        
             
    def expulsao(self):
        verifica = False
        expulso=input('Digite o número do jogador expulso: ')
        for a in lst_escalados:
            if expulso == a.__numero :
                lst_reservas.append(a)
                print(f"{a.__nome_jogador} foi expulso.")
                print(' ')
                a.__situacao="EXPULSO"
                verifica = True
            
        if verifica == False:
            print(' !! O jogador não está na partida !! ')
                
    def imprimir_escalacao(self):
        arquivo = open("todosjogadores.txt", "w")
        for a in lst_jogadores:
            if a.__participou_partida == True:
                print(f"""-------------------------------------------------------
{a} - Situação: {a.__situacao} - Participou da partida: {a.__participou_partida}""")
                arquivo.write(f"{a} - Situação: {a.__situacao} - Participou da partida: {a.__participou_partida} \n \n")                    
        
    
    def __str__(self):
        return f"Nome: {self.__nome_jogador} - Número: {self.__numero} - Posição: {self.__posicao}  "



def mostrar_jogadores():
        arquivo = open("convocados.txt", "r")
        convocados = arquivo.read()
        print(convocados)


def ler_arquivo_de_jogadores():
        
        arquivo = open("convocados.txt", "w")
        arquivo.write("""1:Alisson:GOLEIRO
2:Danilo:DEFESA
3:Thiago Silva:DEFESA
4:Marquinhos:DEFESA
5:Casemiro:MEIO-CAMPO
6:Alex Sandro:DEFESA
7:Lucas Paquetá:MEIO-CAMPO
8:Fred:MEIO-CAMPO
9:Richarlison:ATACANTE
10:Neymar:ATACANTE
11:Raphinha:ATACANTE
12:Weverton:GOLEIRO
13:Dani Alves:DEFESA
14:Éder Millitão:DEFESA
15:Fabinho:MEIO-CAMPO
16:Alex Telle:DEFESA
17:Bruno Guimarães:MEIO-CAMPO
18:Gabriel Jesus:ATACANTE
19:Antony:ATACANTE
20:Vinicius Junior:ATACANTE
21:Rodrygo:ATACANTE
22:Éverton Ribeiro:MEIO-CAMPO
23:Ederson:GOLEIRO
24:Bremer:DEFESA
25:Pedro:ATACANTE
26:Gabriel Martinelli:ATACANTE""")
        
        arquivo=open("convocados.txt", "r")

        for linha in arquivo:
               numero, nome, posicao = linha.split(":")
               lista_numero.append(numero)
               lista_nome.append(nome)
               lista_posicao.append(posicao)
        
        arquivo.close()

        contador = 0
        for x in lista_numero:
                lst_jogadores.append(Jogador(lista_nome[contador], lista_numero[contador], lista_posicao[contador]))
                contador = contador + 1

        mostrar_jogadores()
        print(' ')
        print(' # Arquivo lido com sucesso # ')
        print(' ')




lista_numero = []
lista_nome = []
lista_posicao = []
lst_jogadores = []
lst_escalados = []
lst_reservas = []
j=Jogador('a',1,'a')

while True:
        escolha = input("""
MENU
======
1- Ler arquivo de jogadores
2- Escalar time
3- Realizar Substiuição
4- Expulsão
5- Imprimir escalação
Escolha: """)

        if escolha == "1": ler_arquivo_de_jogadores()
        if escolha == "2": j.escalar_time()
        if escolha == "3": j.realizar_substiuição()
        if escolha == "4": j.expulsao()
        if escolha == "5": j.imprimir_escalacao()
        

