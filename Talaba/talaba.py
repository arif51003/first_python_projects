class Talaba:
    def __init__(self,id,ism,familiya,grade=0):
        self.id=id
        self.ism=ism
        self.familiya=familiya
        self.__grade=0
    def set_grade(self,grade):
        self.grade=grade
        return self.grade
    def __str__(self):
        return f"{self.ism} {self.familiya} {self.grade}"
    def __repr__(self):
        return f"{self.id}#{self.ism}#{self.familiya}#{self.__grade}"
    

# t1=Talaba(4777,"Asror","Baxronov")
# t2=Talaba(123,"Arif","Masharipov")