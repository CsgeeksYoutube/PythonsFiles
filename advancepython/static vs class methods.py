from importlib.resources import contents


class Shipping:
    next_serial=1
    @classmethod
    def _get_next_serial(cls):
        result= cls.next_serial
        cls.next_serial +=1
        return result

    @classmethod
    def create_empty(cls,owner_name):
        return cls(owner_name, contents=None)
    
    @classmethod
    def create_with_items(cls,owner_name, items):
        return cls(owner_name, contents=list(items))


    # @staticmethod
    # def _get_next_serial():
    #     result= Shipping.next_serial
    #     Shipping.next_serial +=1
    #     return result

    def __init__(self,owner_name,contents):
        self.owner_name = owner_name
        self.contents = contents
        self.serial = Shipping._get_next_serial()

c3=Shipping.create_empty("YMl")
print(c3.contents)
c4=Shipping.create_with_items("MA",['food','textiles','minerals'])
print(c4.contents)

c1=Shipping("Tata","salt")
print(c1.owner_name)
print(c1.contents)
print(c1.next_serial)
print(c1.serial)
c2=Shipping("Adani","clothes")
print(c2.owner_name)
print(c2.contents)
print(c2.serial)
print(c2.next_serial)