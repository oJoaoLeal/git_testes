class JurosSimples:
    def __init__(self, capital_invest, taxa_juros, tempo):
        self.__capital_inves = capital_invest
        self.__taxa_juros = taxa_juros
        self.__tempo = tempo

    def __del__(self):
        pass

    def calcJuros(self):
        return self.__capital_inves * self.__taxa_juros * self.__tempo


x = JurosSimples(1000, 1.1, 10)
print(x.calcJuros())

# Comentario teste git
