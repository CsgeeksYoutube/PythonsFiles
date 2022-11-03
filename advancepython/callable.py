print(callable(str))
print(callable(len))
print(callable(list))
num=10
print(callable(num))
def greet():
    print('hello frnd')

print(callable(greet))
class Student:
    def greet(self):
        print('hello')
    def __call__(self):
        print('hello frnds')
std=Student()
print('is student.greet()?',callable(std.greet))
print(callable(Student))
print(callable(std))
std()
