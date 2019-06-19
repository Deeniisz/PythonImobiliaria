class Contrato:
    def __init__(self, ID, data, corretor, cotratante, imovel):
        self.ID = ID
        self.data = data
        self.corretor = corretor
        self.cotratante = cotratante
        self.imovel = imovel

    def setID(self, ID):
        self.ID = ID

    def getID(self):
        return self.ID

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def getCorretor (self):
        return self.corretor

    def getContratante (self):
        return self.cotratante

    def getImovel (self):
        return self.imovel