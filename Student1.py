class Student:
    student_name="no name"
    def __init__(self,name):
        print("object created")
        print(name)
        print(self.student_name)
        #self.student_name=name
s1=Student("Alekhya")
s2=Student("Pravallika")
s3=Student("Akhila")
#s2.student_name="Pravallika Nagubandi
print(s2.student_name)
