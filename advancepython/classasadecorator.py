class CallCount:
    def __init__(self,f):
        self.f=f
        self.count=0
    def __call__(self,*args):
        self.count +=1
        return self.f(*args)

@CallCount
def hello(name):
    print('hello {}'.format(name))


hello('hello')
hello('csgeeks')
print(hello.count)