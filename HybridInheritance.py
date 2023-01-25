#hybrid inheritance
class Factory:
    item="chocolate product"
class Cadbury(Factory):
    prep="only chocolate"
class Nestle(Factory):
    prep="biscuit type chocolate"
class Choco_product(Cadbury,Nestle):
    pass
obj=Choco_product()
print(obj.item)
print(obj.prep)
