# def hello():
#     print('hello')

# a=hello
# a()
# del hello
# a()
# hello()


# def hello(name='vijay'):
#     print('hello vijay ')

#     def welcomemsg():
#         print('this is welcome msg')
    
#     def comein():
#         print('plz come in')
#         return('this is a come in function')

#     welcomemsg()
#     comein()

#     if name=='vijay':
#         return welcomemsg
#     else:
#         return comein
        

# new_func = hello('ramji')
# print(new_func())

def hello():
    return 'hello frnd'

def func2(func_name):
    print('function is passing as a argument')
    print(func_name())

print(hello())
func2(hello)
