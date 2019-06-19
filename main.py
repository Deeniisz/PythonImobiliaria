import pymongo
from Corretor import Corretor
from Contratante import Contratante
from Imovel import Imovel
from Contrato import Contrato

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["imobiliaria"]
col1 = mydb["cliente"]
col2 = mydb["contratante"]
col3 = mydb["imovel"]

corretorobj = []
contratanteobj = []
imovelobj = []
contratoobj = []

i = 100

while (i != 0):
    print("--------------------------")
    print("1 - Cadastrar Corretor")
    print("2 - Listar Corretores")
    print("3 - Cadastrar Contratante")
    print("4 - Listar Contratantes")
    print("5 - Cadastrar Imovel")
    print("6 - Listar Imoveis")
    print("7 - Gerar Contrato")
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
        for i in corretorobj:
            print("------------------------")
            print(("ID: {} \n Nome: {} \n Telefone: {} \n Endereço: {} \n Cidade: {} \n Estado: {} \n Nascimento: {} \n Salário: {} \n").format(
            i.getID(),
            z.getNome(), 
            i.getTelefone(), 
            i.getEndereco(), 
            i.getCidade(), 
            i.getEstado(), 
            i.getNasc(), 
            i.getSal()))

    if(x == 3):
        print("---------------------------")
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

    if(x == 4):
        for i in contratanteobj:
            print("------------------------")
            print(("ID: {} \n Nome: {} \n Telefone: {} \n Endereço: {} \n Cidade: {} \n Estado: {} \n Nascimento: {} \n").format(
            i.getID(),
            z.getNome(), 
            i.getTelefone(), 
            i.getEndereco(), 
            i.getCidade(), 
            i.getEstado(), 
            i.getNasc()))

    if(x == 5):
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

    if(x == 6):
        for i in imovelobj:
            print("------------------------")
            print(("ID: {} \n Endereço: {} \n Cidade: {} \n Estado: {} \n Numero: {} \n").format(
            i.getID(),
            i.getEndereco(), 
            i.getCidade(), 
            i.getEstado(), 
            i.getNum()))

    if(x == 7):
        print("---------------------------")
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
        
        col3.insert_one({"ID" : z.getID(),
                                "Data" : z.getData(),
                                "Corretor" : z.getCorretor(),
                                "Contratante" : z.getContratante(),
                                "Imovel" : z.getImovel()})
        
    if(x == 0):
        i = 0