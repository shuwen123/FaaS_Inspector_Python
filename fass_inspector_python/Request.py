class Resquest:
    name = ""

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def __init__(self, name):
        self.name = name