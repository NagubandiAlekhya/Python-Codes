class Chairman:
    name="Krishna Rao"
    clgname="Pragati engineering college"
class Director(Chairman):
    name="Sambhu Prasad"
class Principal(Director):
    name="Satya Narayana"
class Hods(Principal):
    name="Radha Krishna"
    dept="cse-ai&ml"
class Teachers(Hods):
    name="Yamuna"
class Students(Teachers):
    name="Alekhya"
    pass
obj=Students()
print(obj.name)
print(obj.clgname)
print(obj.dept)
