from random import randint
import time

from model.Fabrica import Fabrica
from model.Maquina import Maquina
from model.Setup import Setup

if __name__ == '__main__':
    setup = Setup("Produto A", 10, 10)
    fabrica = Fabrica(1, "Fabrica %i" % 1, setup)

    maquinas = []
    for i in range(setup.getQtdeMaquinas()):
        maquina = Maquina(i, "Maquina %i" % i, fabrica)
        maquinas.append(maquina)

    for maq in maquinas:
        maq.start()
