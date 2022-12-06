class Chess:

    def __new__(cls,*args,**kwargs):
        print("args===",repr(args))
        print("kwargs==",repr(kwargs))
        obj = super().__new__(cls)
        print("id(obj)---",id(obj))
        return obj
    
    def __init__(self,x,y):
        print("id(self)----",id(self))
        self.x=x
        self.y=y

a=Chess(4,5)
