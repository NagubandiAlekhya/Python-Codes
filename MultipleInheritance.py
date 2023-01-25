#multiple inheritance has diamond problem
'''
class P1:
    def m1(self):
        print("in parent class 1")
class P2:
    def m1(self):
        print("in parent class 2")
class C(P2,P1):
    pass
obj=C()
obj.m1()
'''
class Mother:
    color="fair"
    height="5.2"
    pass
class Father:
    color="black"
    height="5.5"
    pass
class Child(Mother,Father):
    pass
obj=Child()
print(obj.color)
print(obj.height)
