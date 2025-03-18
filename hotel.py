class ItemComida:
    def __init__(self,nome:str, preco:float):
        self.__nome = nome
        self.__preco = preco

    def consultar_preco(self):
        return self.__preco
    
class Conta:
    def __init__(self):
        self.__itens_consumidos: list[ItemComida] = []
        
    def adicionar_item(self,item:ItemComida):
        self.__itens_consumidos.append(item)

    def calcular_total(self,preco:float):
        total = 0
        for iten in self.__itens_consumidos:
            total += iten.consultar_preco()
        
class Quarto:
    def __init__(self,numero:int, localizacao:int, ocupado:bool):
        self.__numero = numero
        self.__localizacao = localizacao
        self.__ocupado = ocupado

    def atribuir_hospede(self):
        if not self.__ocupado:
            self.__ocupado = True
        else:
            print("Este quarto está ocupado")


    def desocupar(self):
        if self.__ocupado:
            self.__ocupado = False
        else:
            print("Este quarto está desocupado")

class Hospede:
    def __init__(self,nome:str):
        self.__nome = nome
        self.__quarto = None
        self.__conta = None

    def fazer_check_in(self, quarto:Quarto):
        self.__quarto = quarto

    def fazer_check_out(self,quarto:Quarto):
        self.__quarto = quarto

    def pagar_conta (self,conta:Conta):
        self.__quarto = quarto

    def pedir_comida (self,chef:Chef, nome:str):
        self.__quarto = quarto
