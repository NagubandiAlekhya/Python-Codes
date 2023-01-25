class Student:
    student_name="no name"
    def __init__(self,name):
        print("object created")
        print(name)
        print(self.student_name)
        #self.student_name=name
s1=Student("Alekhya")
