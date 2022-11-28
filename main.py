class Client_12:
    def __init__ (self, cod, data, razmer, procent):
        self.cod = cod
        self.data = data
        self.razmer = razmer
        self.procent = procent

class Bank:
    def addClient(self, client):
        clientBase = []
        addClient = client
        clientBase.append(addClient)
    def showByMoney(self, money, client):
        money = int(200)
        if client > money:
            print(client)
    def showBycode(self, cod):
        cod = 12323
        print(self.cod, self.addClient())

    def showByProc(self, proc, client):
        proc = "12%"
        if client > proc:
            print(client)