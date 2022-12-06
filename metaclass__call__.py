# class TricingMeta(type):
#     @classmethod
#     def __prepare__(mcs,name,bases,**kwargs):
#         print('tracing meta __prepare__')
#         print("mcs =",mcs)
#         print("name = ", name)
#         print("bases = ", bases)
#         print("kwargs = ", kwargs)
#         namespace=super().__prepare__(name,bases)
#         print("namespace===",namespace)
#         print()
#         return namespace

#     def __new__(mcs,name,bases,namespace,**kwargs):
#         print('tracing meta __new__')
#         print("mcs =",mcs)
#         print("name = ", name)
#         print("bases = ", bases)
#         print("kwargs = ", kwargs)
#         print("namespace===",namespace)
#         cls=super().__new__(mcs,name,bases,namespace)
#         print("cls===",cls)
#         print()
#         return cls
    
#     def __init__(cls,name,bases,namespace,**kwargs):
#         print('tracing meta __init__')
#         print("cls =",cls)
#         print("name = ", name)
#         print("bases = ", bases)
#         print("kwargs = ", kwargs)
#         print("namespace===",namespace)
#         print()
#         super().__init__(name,bases,namespace)  
    
#     def __call__(cls,*args,**kwargs):
#         print('tracing meta __call__')
#         print("cls =",cls)
#         print("args = ", args)
#         print("kwargs = ", kwargs)
#         print("Print about call type")
#         obj=super().__call__(*args,**kwargs)
#         print("retruned from call")
#         print("obj====",obj)
#         print()
#         return obj

# class TracingClass(metaclass=TricingMeta):
#     def __new__(cls,*args,**kwargs):
#         print('tracing class __new__')
#         print("cls =",cls)
#         print("args = ", args)
#         print("kwargs = ", kwargs)
#         obj=super().__new__(cls)
#         print("obj===",obj)
#         print()
#         return obj
    
#     def __init__(self,*args,**kwargs):
#         print('tracing class __init__')
#         print("self =",self)
#         print("args = ", args)
#         print("kwargs = ", kwargs)
#         print()
        
# t=TracingClass(42,keyword='clef')

class Keyword(type):
    def __call__(cls,*args,**kwargs):
        if args:
            raise TypeError("args is pass")
        return super().__call__(cls,**kwargs)

class Constrained(metaclass=Keyword):
    def __init__(self,*args,**kwargs):
        print('args---',args)
        print("kwargs---",kwargs)

c =Constrained(color='white') 