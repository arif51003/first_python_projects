from talaba import Talaba
from db import Database

class Manager:
    def __init__(self,ism,familiya):
        self.ism = ism
        self.familiya = familiya
        self.database = Database()
        
    def add_student(self, student):
        self.database.append2file(repr(student)+"\n")
        
    def get_students(self):
        all_student=self.database.readfromfile()
        students=[]
        
        for data in all_student:
            id,ism,fam,grade=data.split("#")
            student=Talaba(id,ism,fam)
            student.set_grade(grade)
            students.append(student)
        return students
    
    def set_grade(self,id,grade):
        students = self.get_students()
        get_grade  = False
        
        for student in students:
            if id==student.id:
                student.set_grade(grade)
        self.database.write2file(students)
        
        return get_grade
    
    
    def del_student(self,id):
        students=self.get_students()
        
        for i in students:
            if  i.id==id:
                students.pop(i)
                self.database.write2file(students)
                break
                

