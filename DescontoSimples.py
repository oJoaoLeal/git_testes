class DescontoSimples:
    def __init__(self, capital, taxa, tempo):
        self.__capital = capital
        self.__taxa = taxa
        self.__tempo = tempo

    def __del__(self):
        pass

    def calcJuros(self):
        return self.__capital * self.__taxa * self.__tempo
