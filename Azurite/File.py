import os

baseDir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
databaseDir = os.path.join(baseDir,'database')

class dataBase():
    def __init__(self, name, type, dir):
        self.name = name
        self.type = type
        super().__init__()
    def Write(self):
        pass