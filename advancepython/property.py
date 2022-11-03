class Shipping:
    next_serial=1
    @classmethod
    def _get_next_serial(cls):
        result= cls.next_serial
        cls.next_serial +=1
        return result

    @classmethod
    def create_empty(cls,owner_name,*args,**kwargs):
        return cls(owner_name, contents=None,*args,**kwargs)
    
    @classmethod
    def create_with_items(cls,owner_name, items,*args,**kwargs):
        return cls(owner_name, contents=list(items),*args,**kwargs)

    def __init__(self,owner_name,contents):
        self.owner_name = owner_name
        self.contents = contents
        self.serial = Shipping._get_next_serial()

class RefShipping(Shipping):
    Max_celsius=4.0
    @staticmethod
    def _c_to_f(celsius):
        return celsius *9/5 +32
    
    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit -32) *5/9


    def __init__(self, owner_name, contents,celsius):
        super().__init__(owner_name, contents)
        if celsius > RefShipping.Max_celsius:
            raise ValueError("max tem is reach")
        self.celsius= celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self,value):
        if value > RefShipping.Max_celsius:
            raise ValueError("Temp is too high")
        self._celsius= value

    @property
    def fahrenheit(self):
        return RefShipping._c_to_f(self.celsius)
    
    @fahrenheit.setter
    def fahrenheit(self,value):
        self.celsius = RefShipping._f_to_c(value)


r3= RefShipping.create_with_items("MA",['food','textiles','minerals'],celsius=2.0)
print(r3.contents)
print(r3.celsius)
print(r3.fahrenheit)
r3.fahrenheit = -10
print(r3.celsius)

r4= RefShipping.create_empty("Maa", celsius=7.0)




