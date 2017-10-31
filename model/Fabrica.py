from model.core.Entity import Entity

class Fabrica(Entity):

    def __init__(self, id, descricao, setup):
        Entity.__init__(self)
        self.setId(id)
        self.setDescricao(descricao)
        self._setup = setup

    def getSetup(self):
        return self._setup
