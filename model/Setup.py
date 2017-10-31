class Setup:
    def __init__(self, produto, qtdePecas, qtdeMaquinas):
        self._produto = produto
        self._qtdePecas = qtdePecas
        self._qtdemaquinas = qtdeMaquinas

    def getProduto(self):
        return self._produto

    def getQtdePecas(self):
        return self._qtdePecas

    def getQtdeMaquinas(self):
        return self._qtdemaquinas