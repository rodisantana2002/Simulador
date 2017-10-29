class Entity(object):
    def __init__(self):
        self._id=None
        self._descricao=None

    def setId(self, id):
        self._id = id

    def getId(self):
        return self._id

    def setDescricao(self, descricao):
        self._descricao = descricao

    def getDescricao(self):
        return self._descricao
