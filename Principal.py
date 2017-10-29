from model.Fabrica import Fabrica

if __name__ == '__main__':
    x=6
    fabricas = []

    for i in range(1, x):
        fabrica = Fabrica()
        fabrica.setId(i)
        fabrica.setDescricao("Fabrica %i" %(i))
        print(fabrica.getDescricao())
        fabricas.append(fabrica)

    print(fabricas[3].getDescricao())

