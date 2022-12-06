class TracingMeta(type):
    def __new__(msc,name,bases,namespace,**kwargs):
        print("kwargs---",kwargs)
        cls= super().__new__(msc,name,bases,namespace)
        return cls

class Vijay(metaclass=TracingMeta,num=26):
    pass
    
    