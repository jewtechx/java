class Student:
    def __init__(student,name,house):
        student.name = name
        student.house = house

    def details(student):
        return f"{student.name} is in {student.house}"
    
    @property
    def sname(student):
        return student.name
        
    @sname.setter
    def sname(student,name):
        student.name = name

studentObj = Student('Jew','WhiteHouse')
print(studentObj.details())
print(studentObj.sname)

