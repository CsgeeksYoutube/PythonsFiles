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
@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

l=[1,2,3]
l=rotate_list(l)
print(l)
l=rotate_list(l)
print(l)
tracer.enabled=False
l=rotate_list(l)
print(l)
