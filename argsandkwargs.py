# def func(*args):
#     for item in args:
#         print(item)

# func(45,56,56,45,69,25)

# def func(**kwargs):
#     print(kwargs)
#     if 'name' in kwargs:
#         print('my name is {}'.format(kwargs['name']))
#     else:
#         print('there is no vijay here')

# func(name='vijay',sname='manral')


def func(*args,**kwargs):
    print(args)
    print(kwargs)
    print('i like {} {}'.format(args[0],kwargs['food']))

func(10,20,30,fruit='orange',food='eggs')