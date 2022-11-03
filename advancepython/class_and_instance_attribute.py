class Shipping:
    next_serial=1
    def __init__(self,owner_name,contents):
        self.owner_name = owner_name
        self.contents = contents
        # self.serial= Shipping.next_serial
        # Shipping.next_serial +=1
        self.serial= self.next_serial
        self.next_serial +=1

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