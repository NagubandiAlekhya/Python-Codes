class Product():
    type="watch"
    pulse_rate="not present"
    pass
class Titan(Product):
    pass
class Sonata(Product):
    pass
class Boat(Product):
    type="smart watch"
    pulse_rate="present"
    pass
class Samsung(Product):
    pass
class Realme(Product):
    pass
obj=Boat()
print(obj.type)
print(obj.pulse_rate)
