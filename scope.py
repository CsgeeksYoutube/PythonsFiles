# Local scope: The names that you define in 
# this scope are only available or visible to the code within the scope.

# Enclosing or nonlocal scope is observed when you 
# nest functions inside other functions. The enclosing 
# scope was added in Python 2.2. It takes the form of the 
# local scope of any enclosing function’s local scopes. 

# Global scope: The names that you define in this 
# scope are available to all your code.

# The built-in scope is a special Python scope that’s 
# implemented as a standard library module named builtins 
# in Python 3.x. All of Python’s built-in objects live in this module. 
# LEGB

# a=50
# def scopes():
#     a=75
#     return a

# print(scopes())


# name = 'global variable'
# def scopes():
#     # name= 'vijay'
#     def hello():
#         # name='ajay'
#         print('hello'+name)

#     hello()

# scopes()


a=75
def func(a):
    print(f'value of a is{a}')
    a=750
    print(f'new value of a is{a}')
    return a 
a=func(a)
print(a)



#   What is the Output?
