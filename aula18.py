# class ContaInvestimento:
#     def __init__(self,cpf:str,saldo:float):
#         self.cpf = cpf
#         self.saldo=saldo

#     def simular_rendimento(self,taxa:float,tempo:int):
#         return self.saldo*(1+taxa/100)**tempo

# def test_simular_rendimento_cenario_1():
#     conta = ContaInvestimento('123.456.789-10',1000.00)
#     assert conta.simular_rendimento(10,3)==1331.00

# def test_simular_rendimento_cenario_2():
#     conta = ContaInvestimento('123.456.789-10',25000.00)
#     assert conta.simular_rendimento(15,1)==28750.00

# def test_simular_rendimento_cenario_3():
#     conta = ContaInvestimento('123.456.789-10',50000.00)
#     assert conta.simular_rendimento(17,40)== 26693435.64



class Livro:
    def __init__(self, titulo: str, autor:list, disponivel: bool):
        self.titulo = titulo
        self.autor = []
        self.__disponivel = disponivel
        
    def get_disponivel():
        pass

    def set_disponivel():
        pass


class Usuario:
    def __init__(self,nome:str,livros:list):
        self.nome = nome
        self.livros = []
    
    def emprestar(livro:Livro):
        pass

    def devolver(livro:Livro):
        pass


def test_1_get_disponivel():
    livro = Livro("10 Mandamentos", 'Michael Ramos', True)
    assert livro.get_disponivel() == True

def test_2_set_disponivel():
    livro = Livro("10 Mandamentos", 'Michael',True)
    livro.set_disponivel(False)
    assert livro.get_disponivel() == False

def test_3_emprestar():
    livro = Livro("10 Mandamentos", 'Michael', True)
    usuario = Usuario('Michael')
    usuario.emprestar(livro)
    assert livro.get_disponivel() == False and livro in usuario.livros 

def test_4_devolver():
    livro = Livro("10 Mandamentos", 'Michael')
    livro.emprestar()
    assert True(livro.set_disponivel())