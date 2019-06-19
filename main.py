import pymongo
from Corretor import Corretor
from Contratante import Contratante
from Imovel import Imovel
from Contrato import Contrato
import xlrd

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["imobiliaria"]
col1 = mydb["corretor"]
col2 = mydb["contratante"]
col3 = mydb["imovel"]
col4 = mydb["contrato"]

corretorobj = []
contratanteobj = []
imovelobj = []
contratoobj = []

i = 100

while (i != 0):
    print("--------------------------")
    print("1 - Cadastrar Corretor")
    print("2- Importar Corretores Planilha")
    print("3 - Listar Corretores")
    print("4 - Cadastrar Contratante")
    print("5 - Importar Contratantes Planilha")
    print("6 - Listar Contratantes")
    print("7 - Cadastrar Imovel")
    print("8 - Importar Imoveis Planilha")
    print("9 - Listar Imoveis")
    print("10 - Gerar Contrato")
    print("11 - Listar Contratos")
    print("12 - Gerar arquivo de Saída")
    print("0 - Sair")
    print("Escolhida :")
    x = int(input())

    if(x == 1):
        print("---------------------------")
        print("-----CADASTRO CORRETOR-----")
        print("ID Corretor: ")
        a = input()
        print("Nome : ")
        b = input()
        print("Telefone : ")
        c = input()
        print("Endereço : ")
        d = input()
        print("Cidade : ")
        e = input()
        print("Estado : ")
        f = input()
        print("Nasc : ")
        g = input()
        print("Salário : ")
        h = input()
        print("---------------------------")
        z = Corretor(a, b, c, d, e, f, g, h)

        corretorobj.append(z)
        
        col1.insert_one({"ID" : z.getID(),
                                "Nome" : z.getNome(),
                                "Telefone" : z.getTelefone(),
                                "Endereco" : z.getEndereco(),
                                "Cidade" : z.getCidade(),
                                "Estado" : z.getEstado(),
                                "Nascimento" : z.getNasc(),
                                "Salário" : z.getSal()})

    if(x == 2):
        book = xlrd.open_workbook("corretor.xls")

        sh = book.sheet_by_index(0)

        print("-----------------------------")
        print("A Planilha Foi Lida !")
        print("-----------------------------")

        i = 1
        while (i < 6):
            a = int(sh.cell_value(rowx=0, colx=i))
            b = (sh.cell_value(rowx=1, colx=i))
            c = (sh.cell_value(rowx=2, colx=i))
            d = (sh.cell_value(rowx=3, colx=i))
            e = (sh.cell_value(rowx=4, colx=i))
            f = (sh.cell_value(rowx=5, colx=i))
            g = str(sh.cell_value(rowx=6, colx=i))
            h = (sh.cell_value(rowx=7, colx=i))
            i += 1
            z = Corretor(a, b, c, d, e, f, g, h)
            corretorobj.append(z)

            col1.insert_one({"ID" : z.getID(),
                                "Nome" : z.getNome(),
                                "Telefone" : z.getTelefone(),
                                "Endereco" : z.getEndereco(),
                                "Cidade" : z.getCidade(),
                                "Estado" : z.getEstado(),
                                "Nascimento" : z.getNasc(),
                                "Salário" : z.getSal()})

    if(x == 3):
        for i in corretorobj:
            print("------------------------")
            print((" ID: {} \n Nome: {} \n Telefone: {} \n Endereço: {} \n Cidade: {} \n Estado: {} \n Nascimento: {} \n Salário: {} \n").format(
            i.getID(),
            i.getNome(), 
            i.getTelefone(), 
            i.getEndereco(), 
            i.getCidade(), 
            i.getEstado(), 
            i.getNasc(), 
            i.getSal()))

    if(x == 4):
        print("------------------------------")
        print("-----CADASTRO CONTRATANTE-----")
        print("ID Contratante: ")
        a = input()
        print("Nome : ")
        b = input()
        print("Telefone : ")
        c = input()
        print("Endereço : ")
        d = input()
        print("Cidade : ")
        e = input()
        print("Estado : ")
        f = input()
        print("Nasc : ")
        g = input()
        print("---------------------------")
        z = Contratante(a, b, c, d, e, f, g)

        contratanteobj.append(z)
        
        col2.insert_one({"ID" : z.getID(),
                                "Nome" : z.getNome(),
                                "Telefone" : z.getTelefone(),
                                "Endereco" : z.getEndereco(),
                                "Cidade" : z.getCidade(),
                                "Estado" : z.getEstado(),
                                "Nascimento" : z.getNasc()})

    if(x == 5):
        book = xlrd.open_workbook("contratante.xls")

        sh = book.sheet_by_index(0)

        print("-----------------------------")
        print("A Planilha Foi Lida !")
        print("-----------------------------")

        i = 1
        while (i < 6):
            a = int(sh.cell_value(rowx=0, colx=i))
            b = (sh.cell_value(rowx=1, colx=i))
            c = (sh.cell_value(rowx=2, colx=i))
            d = (sh.cell_value(rowx=3, colx=i))
            e = (sh.cell_value(rowx=4, colx=i))
            f = (sh.cell_value(rowx=5, colx=i))
            g = str(sh.cell_value(rowx=6, colx=i))
            i += 1

            z = Contratante(a, b, c, d, e, f, g)
            contratanteobj.append(z)

            col2.insert_one({"ID" : z.getID(),
                                "Nome" : z.getNome(),
                                "Telefone" : z.getTelefone(),
                                "Endereco" : z.getEndereco(),
                                "Cidade" : z.getCidade(),
                                "Estado" : z.getEstado(),
                                "Nascimento" : z.getNasc()})

    if(x == 6):
        for i in contratanteobj:
            print("------------------------")
            print((" ID: {} \n Nome: {} \n Telefone: {} \n Endereço: {} \n Cidade: {} \n Estado: {} \n Nascimento: {} \n").format(
            i.getID(),
            i.getNome(), 
            i.getTelefone(), 
            i.getEndereco(), 
            i.getCidade(), 
            i.getEstado(), 
            i.getNasc()))

    if(x == 7):
        print("---------------------------")
        print("-----CADASTRO IMOVEL-----")
        print("ID Imovel: ")
        a = input()
        print("Endereço : ")
        b = input()
        print("Cidade : ")
        c = input()
        print("Estado : ")
        d = input()
        print("Numero : ")
        e = input()
        print("---------------------------")
        z = Imovel(a, b, c, d, e)

        imovelobj.append(z)
        
        col3.insert_one({"ID" : z.getID(),
                                "Endereco" : z.getEndereco(),
                                "Cidade" : z.getCidade(),
                                "Estado" : z.getEstado(),
                                "Número" : z.getNum()})

    if(x == 8):
        book = xlrd.open_workbook("imovel.xls")

        sh = book.sheet_by_index(0)

        print("-----------------------------")
        print("A Planilha Foi Lida !")
        print("-----------------------------")

        i = 1
        while (i < 6):
            a = int(sh.cell_value(rowx=0, colx=i))
            b = (sh.cell_value(rowx=1, colx=i))
            c = (sh.cell_value(rowx=2, colx=i))
            d = (sh.cell_value(rowx=3, colx=i))
            e = (sh.cell_value(rowx=4, colx=i))
            i += 1

            z = Imovel(a, b, c, d, e)
            imovelobj.append(z)

            col3.insert_one({"ID" : z.getID(),
                            "Endereco" : z.getEndereco(),
                            "Cidade" : z.getCidade(),
                            "Estado" : z.getEstado(),
                            "Num" : z.getNum()})
        
    if(x == 9):
        for i in imovelobj:
            print("------------------------")
            print((" ID: {} \n Endereço: {} \n Cidade: {} \n Estado: {} \n Numero: {} \n").format(
            i.getID(),
            i.getEndereco(), 
            i.getCidade(), 
            i.getEstado(), 
            i.getNum()))

    if(x == 10):
        print("------------------------")
        print("-----Gerar Contrato-----")
        print("ID Contrato: ")
        a = input()
        print("Data : ")
        b = input()

        print("ID do Corretor : ")
        c = input()
        for i in corretorobj:
            if (c == i.getID()):
                c = i

        print("ID do Contratante : ")
        d = input()
        for i in contratanteobj:
            if (d == i.getID()):
                d = i

        print("ID do Imovel : ")
        e = input()
        for i in imovelobj:
            if (e == i.getID()):
                e = i

        print("---------------------------")
        z = Contrato(a, b, c, d, e)

        contratoobj.append(z)
        
        col4.insert_one({"ID" : z.getID(),
                        "Data" : z.getData(),
                        "Corretor" : z.getCorretor(),
                        "Contratante" : z.getContratante(),
                        "Imovel" : z.getImovel()})
        
    if(x == 11):
        for i in contratoobj:
            print("------------------------")
            print((" ID: {} \n Data: {} \n Corretor: {} \n Contratante: {} \n Imovel: {} \n").format(
            i.getID(),
            i.getData(), 
            i.getCorretor(), 
            i.getContratante(), 
            i.getImovel()))

    if(x == 12):   
        arq = open("D:\corretorsaida.txt", "w")
        for i in corretorobj:
            arq.writelines(str(i.getID()) + "\n")
            arq.writelines(str(i.getNome()) + "\n") 
            arq.writelines(str(i.getTelefone()) + "\n") 
            arq.writelines(str(i.getEndereco()) + "\n") 
            arq.writelines(str(i.getCidade()) + "\n") 
            arq.writelines(str(i.getEstado()) + "\n") 
            arq.writelines(str(i.getNasc()) + "\n")
            arq.writelines(str(i.getSal()) + "\n")
            arq.writelines("\n")
        arq.close()
        print("corretorsaída.txt Gerado ! ")

        arq = open("D:\contratantesaida.txt", "w")
        for i in contratanteobj:
            arq.writelines(str(i.getID()) + "\n")
            arq.writelines(str(i.getNome()) + "\n") 
            arq.writelines(str(i.getTelefone()) + "\n") 
            arq.writelines(str(i.getEndereco()) + "\n") 
            arq.writelines(str(i.getCidade()) + "\n") 
            arq.writelines(str(i.getEstado()) + "\n") 
            arq.writelines(str(i.getNasc()) + "\n")
            arq.writelines("\n")
        arq.close()
        print("contratantesaída.txt Gerado ! ")

        arq = open("D:\imovelsaida.txt", "w")
        for i in imovelobj:
            arq.writelines(str(i.getID()) + "\n") 
            arq.writelines(str(i.getEndereco()) + "\n") 
            arq.writelines(str(i.getCidade()) + "\n") 
            arq.writelines(str(i.getEstado()) + "\n") 
            arq.writelines(str(i.getNum()) + "\n")
            arq.writelines("\n")
        arq.close()
        print("imovelsaida.txt Gerado ! ")

        arq = open("D:\contratosaida.txt", "w")
        for i in contratoobj:
            arq.writelines(str(i.getID()) + "\n")
            arq.writelines(str(i.getData()) + "\n") 
            arq.writelines(str(i.getCorretor()) + "\n") 
            arq.writelines(str(i.getContratante()) + "\n") 
            arq.writelines(str(i.getImovel()) + "\n")
            arq.writelines("\n")
        arq.close()
        print("contratosaída.txt Gerado ! ")

    if(x == 0):
        i = 0