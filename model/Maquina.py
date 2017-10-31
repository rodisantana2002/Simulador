import threading
from random import randint
import time

from model.Produto import Produto
from model.core.Entity import Entity
import datetime

class Maquina(Entity, threading.Thread):

    def __init__(self, id, descricao, fabrica):
        Entity.__init__(self)
        threading.Thread.__init__(self)
        self.setId(id)
        self.setDescricao(descricao)
        self.situacao = True
        self._fabrica = fabrica
        self._produtos=[]

    def getSituacao(self):
        return self.situacao

    def getFabrica(self):
        return self._fabrica

    def getProdutos(self):
        return self._produtos

    def getDataInicioOperacao(self):
        return self._dataInicioOperacao

    def getHoraInicioOperacao(self):
        return self._horaInicioOperacao

    def getDataTerminoOperacao(self):
        return self._dataTerminoOperacacao
    def setDataTerminoOperacao(self, data):
        self._dataTerminoOperacacao = data

    def getHoraTerminoOperacao(self):
        return self._horaTerminoOperacacao
    def setHoraTerminoOperacao(self, hora):
        self._horaTerminoOperacacao = hora

    def run(self):
        dataHora = datetime.datetime.today()
        self._dataInicioOperacao = "%s/%s/%s" %(dataHora.day, dataHora.month,dataHora.year)
        self._horaInicioOperacao = "%s:%s:%s %s" %(dataHora.hour,dataHora.minute, dataHora.second, dataHora.microsecond)
        print(self.getHoraInicioOperacao())

        for i in range(1, self.getFabrica().getSetup().getQtdePecas()):
            dataHora = datetime.datetime.today()
            data = "%s/%s/%s" %(dataHora.day, dataHora.month,dataHora.year)
            hora = "%s:%s:%s %s" %(dataHora.hour,dataHora.minute, dataHora.second, dataHora.microsecond)
            produto = Produto(i, self.getFabrica().getSetup().getProduto(), self, data, hora)
            print(produto.getSerialCode(), " ", produto.getHoraFabricacao())
            self._produtos.append(produto)

        self.situacao = False
        dataHora = datetime.datetime.today()
        self._dataTerminoOperacacao = "%s/%s/%s" %(dataHora.day, dataHora.month,dataHora.year)
        self._horaTerminoOperacacao = "%s:%s:%s %s" %(dataHora.hour,dataHora.minute, dataHora.second, dataHora.microsecond)
        print(self.getHoraTerminoOperacao(), "\n")
