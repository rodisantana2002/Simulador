import mysql.connector

if __name__ == '__main__':
    try:
        cnn = mysql.connector.connect(
            user='horacerta',
            password='123Perkons',
            host="localhost",
            database='horacerta')

        queryPessoa = "SELECT * FROM Pessoa"
        cursor = cnn.cursor(buffered=True)

        cursor.execute(queryPessoa)

        print(cursor.column_names)
        print("----------------------------------------")
        for (result) in cursor:
            print(result)

        cnn.close
    except mysql.connector.Error as erro:
        print(erro)

    # pagina = "http://wildfly-papers.a3c1.starter-us-west-1.openshiftapps.com/services/destino/list"
    # # objeto = urllib.request.urlretrieve(pagina, "teste.json", None, None)
    # objeto = urllib.request.urlopen(pagina)
    # print(objeto.read())

    # setup = Setup("Produto A", 10, 10)
    # fabrica = Fabrica(1, "Fabrica %i" % 1, setup)
    #
    # maquinas = []
    # for i in range(setup.getQtdeMaquinas()):
    #     maquina = Maquina(i, "Maquina %i" % i, fabrica)
    #     maquina.start()
    #     maquinas.append(maquina)
    #
    # for maq in maquinas:
    #     print(maq.getDescricao())
    #     maq.join()
