from meneger import Manager
from talaba import Talaba

menu = """
1.See all students
2.Add student
3.Set grade
4.Delete student
5.Exit
"""
manager = Manager("a", "A")

while True:
    print(menu)
    choice = input("# ")
    if choice == "1":
        students = manager.get_students()
        for student in students:
            print(student)
        if not students:
            print("Empty list")
    
    elif choice == "2":
        id = input("id = ")
        ism = input("ism = ")
        fam = input("fam = ")
        student=Talaba(id, ism, fam)
        manager.add_student(student)
    
    elif choice == "3":
        id = input("id = ")
        grade = input("grade = ")
        if manager.set_grade(id, grade):
            print("Successfully graded")
        else:
            print("Id not found")
    
    elif choice == "4":
        id = input("id = ")
        if manager.del_student(id):
            print("Student successfully deleted")
        else:
            print(f"Student not found with {id}")
    
    elif choice == "5":
        break
