class Human():

    def __init__(self):
        print('human created')
    
    def who_am_i(self):
        print('i am human')

    def eat(self):
        print('i am eating')

class Boys(Human):
    def __init__(self):
        Human.__init__(self)
        print('boy created')

    def eat(self):
        print('boy is eating')

myboys= Boys()
myboys.who_am_i()
myboys.eat()