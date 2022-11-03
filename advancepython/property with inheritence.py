from turtle import width


class Shipping:
    next_serial=1
    Height=8
    width=8
    @classmethod
    def _get_next_serial(cls):
        result= cls.next_serial
        cls.next_serial +=1
        return result

    @classmethod
    def create_empty(cls,owner_name,lenght,*args,**kwargs):
        return cls(owner_name,lenght, contents=None,*args,**kwargs)
    
    @classmethod
    def create_with_items(cls,owner_name,lenght, items,*args,**kwargs):
        return cls(owner_name,lenght, contents=list(items),*args,**kwargs)

    def __init__(self,owner_name,lenght,contents):
        self.owner_name = owner_name
        self.lenght= lenght
        self.contents = contents
        self.serial = Shipping._get_next_serial()

    @property
    def volume(self):
        return Shipping.Height* Shipping.width* self.lenght

class RefShipping(Shipping):
    Max_celsius=4.0
    Fridge_volume=100
    @staticmethod
    def _c_to_f(celsius):
        return celsius *9/5 +32
    
    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit -32) *5/9


    def __init__(self, owner_name,length, contents,celsius):
        super().__init__(owner_name,length, contents)
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

    @property
    def volume(self):
        return super().volume - RefShipping.Fridge_volume

class HeatedRefShipping(RefShipping):
    Min_Celsius=-20
    @RefShipping.celsius.setter
    def celsius(self,value):
        if value < HeatedRefShipping.Min_Celsius:
            raise ValueError("temp is too cold")
        RefShipping.celsius.fset(self,value)



# r3= Shipping.create_empty("YYY",lenght=20)
# print(r3.volume)
h1= HeatedRefShipping.create_empty("yyy",lenght=20,celsius=-18)
print(h1.celsius)
# h1.celsius =-26
h1.fahrenheit= -14




