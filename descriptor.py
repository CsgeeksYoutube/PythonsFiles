# class Planet:
#     def __init__(self,name,radius,mass):
#         self.name=name
#         self.radius= radius
#         self.mass=mass

# planet_x=Planet(name='x',radius=10e3,mass=-50)
# print(planet_x.radius)
# print(planet_x.name)
# print(planet_x.mass)

# class Planet:
#     def __init__(self,name,radius,mass):
#         self.name=name
#         self.radius= radius
#         self.mass=mass

#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self,value):
#         if not value:
#             raise ValueError("Cannot set empty Planet name")
#         self._name = value

#     @property
#     def radius(self):
#         return self._radius
    
#     @radius.setter
#     def radius(self,value):
#         if value <=0:
#             raise ValueError("Cannot set -ve value")
#         self._radius = value
    
#     @property
#     def mass(self):
#         return self._mass
    
#     @mass.setter
#     def mass(self,value):
#         if value <=0:
#             raise ValueError("Cannot set -ve value")
#         self._mass = value

# planet_x=Planet(name='x',radius=10e3,mass=-50)
# print(planet_x.radius)
# print(planet_x.name)
# print(planet_x.mass)

# class Planet:
#     def __init__(self,name,radius,mass):
#         self.name=name
#         self.radius= radius
#         self.mass=mass

    
#     def get_name(self):
#         return self._name
    
    
#     def set_name(self,value):
#         if not value:
#             raise ValueError("Cannot set empty Planet name")
#         self._name = value
    
#     name = property(fget=get_name, fset=set_name)

    
#     def get_radius(self):
#         return self._radius
    
    
#     def set_radius(self,value):
#         if value <=0:
#             raise ValueError("Cannot set -ve value")
#         self._radius = value
    
#     radius = property(fget=get_radius, fset=set_radius)
    
#     def get_mass(self):
#         return self._mass
    
    
#     def set_mass(self,value):
#         if value <=0:
#             raise ValueError("Cannot set -ve value")
#         self._mass = value

#     mass = property(fget=get_mass, fset=set_mass)

# planet_x=Planet(name='x',radius=10e3,mass=-50)
# print(planet_x.radius)
# print(planet_x.name)
# print(planet_x.mass)

from weakref import WeakKeyDictionary

class Positive:
    def __init__(self):
        self._instance_data=WeakKeyDictionary()
    
    def __get__(self, instance,owner):
        return self._instance_data[instance]

    def __set__(self,instance,value):
        if value <= 0:
            raise ValueError("value {} is not positive".format(value))
        self._instance_data[instance]=value
    
    def __delete__(self,instance):
        raise AttributeError("Cannot delete attribute")

class Planet:
    def __init__(self,name,radius,mass):
        self.name=name
        self.radius= radius
        self.mass=mass

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if not value:
            raise ValueError("Cannot set empty Planet name")
        self._name = value

    radius = Positive()
    mass = Positive()

planet_x=Planet(name='x',radius=10e3,mass=50)
print(planet_x.radius)
print(planet_x.name)
print(planet_x.mass)