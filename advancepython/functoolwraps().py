import functools
def nofun(f):
    @functools.wraps(f)
    def no_function():
        return f()
    return no_function

@nofun
def hello():
    "print a well know msg"
    print("hello frnds")

print(hello.__name__)
print(hello.__doc__)
help(hello)
