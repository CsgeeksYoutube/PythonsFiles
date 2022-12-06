class Vector:
    def __init__(self,x,y):
        self.x=y
        self.y=y
    
    def __repr__(self):
        return "{} ({},{})".format(self.__class__.__name__,self.x,self.y)

v=Vector(5,3)
# print(v)
# print(dir(v))
# print(v.__dict__)
# print(v.__dict__['x'])
# print(v.__dict__['y'])
# v.__dict__['x'] = 14
# print(v.__dict__['x'])
# del v.__dict__['x']
# print(v.x)
v.__dict__['z'] = 12
print(v.z)

print(getattr(v,'y'))
print(hasattr(v,'x'))
delattr(v,'z')
setattr(v,'x',45)
print(v.x)