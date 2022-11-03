# def decor1(func):
#     def inner():
#         x=func()
#         return x*x
#     return inner

# def decor(func):
#     def inner():
#         x= func()
#         return 2 *x
#     return inner

# @decor1
# @decor
# def num():
#     return 10

# print(num())



class Trace:
    def __init__(self):
        self.enabled= True

    def __call__(self,f):
        def wrap(*args):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args)
        return wrap

tracer = Trace()

class IslandMarker:
    def __init__(self, suffix):
        self.suffix= suffix

    @tracer
    def make_island(self, name):
        return name + self.suffix

im= IslandMarker('island')
ip=IslandMarker('Iceland')
print(im.make_island('ramesh'))
print(ip.make_island('ram'))
tracer.enabled=False
print(im.make_island('raj'))
tracer.enabled=True
print(ip.make_island('raju'))
