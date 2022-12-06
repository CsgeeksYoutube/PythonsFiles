# class TricingMeta(type):
#     @classmethod
#     def __prepare__(mcs,name,bases,**kwargs):
#         namespace=super().__prepare__(name,bases)
#         return

#     def __new__(mcs,name,bases,namespace,**kwargs):
#         cls=super().__new__(mcs,name,bases,namespace)
#         return cls
    
#     def __init__(cls,name,bases,namespace,**kwargs):
#         super().__init__(name,bases,namespace)


class TricingMeta(type):
    @classmethod
    def __prepare__(mcs,name,bases,**kwargs):
        print("mcs =",mcs)
        print("name = ", name)
        print("bases = ", bases)
        print("kwargs = ", kwargs)
        namespace=super().__prepare__(name,bases)
        print("namespace===",namespace)
        return namespace

    def __new__(mcs,name,bases,namespace,**kwargs):
        print("mcs =",mcs)
        print("name = ", name)
        print("bases = ", bases)
        print("kwargs = ", kwargs)
        print("namespace===",namespace)
        cls=super().__new__(mcs,name,bases,namespace)
        print("cls===",cls)
        return cls
    
    def __init__(cls,name,bases,namespace,**kwargs):
        print("cls =",cls)
        print("name = ", name)
        print("bases = ", bases)
        print("kwargs = ", kwargs)
        print("namespace===",namespace)
        super().__init__(name,bases,namespace)  
    
    def metamethod(cls):
        print("tracing metamethod")
        print("cls===",cls)
        print()
    
class Widget(metaclass=TricingMeta):
    pass




# class Widget(metaclass=TricingMeta):
#     def action(message):
#         print(message)
#     the_answer = 42