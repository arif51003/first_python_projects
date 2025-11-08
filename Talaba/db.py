class Database:
    def __init__(self,direct="data.txt"):
        self.direct=direct
    
    def write2file(self,data):
        with open(self.direct,"w") as file:
            file.write(data)
            
    def append2file(self,data):
        with open(self.direct,"a") as file:
            file.write(data)
            
    def readfromfile(self):
        with open(self.direct,"r") as file:
            all_line=file.readlines()
        return all_line