class Circle():
    pi=3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius*radius*Circle.pi

    def circumfrence(self):
        return self.radius * Circle.pi *2


mycircle= Circle(30)
print(mycircle.pi)
print(mycircle.area)
a=mycircle.circumfrence()
print(a)