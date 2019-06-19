class Imovel:
    def __init__(self, ID, endereco, cidade, estado, num):
        self.ID = ID
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.num = num

    def setID(self, ID):
        self.ID = ID

    def getID(self):
        return self.ID
        
    def setEndereco(self, endereco):
        self.endereco = endereco

    def getEndereco (self):
        return self.endereco

    def setCidade(self, cidade):
        self.cidade = cidade

    def getCidade (self):
        return self.cidade

    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

    def setNum(self, num):
        self.nasc = num

    def getNum (self):
        return self.num