class Dog():
    def __init__(self,name,owner,length):
        self.name=name
        self.owner=owner
        self.length=length

    def __str__(self):
        return f"{self.name} owner {self.owner}"
    def __len__(self):
        return(self.length)

a = Dog('rocky','vijay',500)

print(str(a))
print(len(a))

c=[1,2,3,4]
print(c)
print(len(c))

