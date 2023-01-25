class Student:
    student_name="no name"
    def __init__(self,name):
        self.student_name=name
    def update_name(self,new_name):
        self.student_name=new_name
s1=Student("Alekhya")
s2=Student("Pravallika")
s3=Student("Akhila")
print(s2.student_name)
s2.update_name("Pravallika Nagubandi")
print(s2.student_name)

