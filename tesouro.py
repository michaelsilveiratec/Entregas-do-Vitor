from abc import ABC, abstractmethod


class TesouroDireto(ABC):
    def __init__(self, investimento_inicial:float, taxa_fixa: float,tempo: int):
        self.investimento_inicial = investimento_inicial
        self.taxa_fixa = taxa_fixa
        self.tempo = tempo

    @abstractmethod
    def calcular_rendimento(self):
        pass


class TesouroIpca(TesouroDireto):
    def __init__(self, investimento_inicial:float, taxa_fixa: float,tempo: int, ipca:float):
        super().__init__(investimento_inicial, taxa_fixa, tempo)
        self.ipca = ipca
    def calcular_rendimento(self):
        vf = self.investimento_inicial*(1+self.taxa_fixa+self.ipca)**self.tempo
        return vf
    

class TesouroPrefixado(TesouroDireto):
    def  __init__(sself, investimento_inicial:float, taxa_fixa: float,tempo: int, ipca:float):
        super().__init__(investimento_inicial, taxa_fixa, tempo)
        
    def calcular_rendimentos(self):
        vf = self.investimento_inicial*(1+self.taxa_fixa)**self.tempo
        return vf


class TesouroSelic(TesouroDireto):
    def __init__(self, investimento_inicial:float, taxa_fixa: float,tempo: int, ipca:float):
        super().__init__(investimento_inicial, taxa_fixa, tempo)
        self.selic = float
    def calcular_rendimento(self):
        vf = self.investimento_inicial*(1+self.taxa_fixa+self.selic)**self.tempo
        return vf
    
vi = 10000
t = 10

TesouroPrefixado = TesouroPrefixado(vi,14.71/100,t)
TesouroSelic = TesouroSelic(vi,14,71/100,t)
TesouroIpca = TesouroIpca(vi,14,71/100,t)

print(f'O valor durante o tempo determinado é R${TesouroPrefixado}')


