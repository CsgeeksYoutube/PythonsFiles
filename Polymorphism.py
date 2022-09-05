# print(2+3)
# print('2'+'3')
class Man():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name+"says i am the best"

class Women():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name+"say i am the women"

raju= Man("raju")
rani=Women("rani")

print(raju.speak())
print(rani.speak())


    