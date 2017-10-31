from model.core.Entity import Entity

class Produto(Entity):

    def __init__(self, id, descricao, maquina, dataFabricacao, horaFabricacao):
        Entity.__init__(self)
        self.setId(id)
        self.setDescricao(descricao)
        self._maquina = maquina
        self._dataFabricacao = dataFabricacao
        self._horaFabricacao = horaFabricacao
        self._inicializarObjetos()

    def getSerialCode(self):
        return self._serialCode

    def getDataFabricacao(self):
        return self._dataFabricacao

    def getHoraFabricacao(self):
        return self._horaFabricacao

    def getMaquina(self):
        return self._maquina

    def _inicializarObjetos(self):
        self._serialCode = "%i%i" %(self.getId(),self.getMaquina().getId())



