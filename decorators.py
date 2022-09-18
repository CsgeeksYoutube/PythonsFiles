def gift_dec(func):
    def wrap_the_gift():
        print('extra code is added before original function')
        func()
        print('extra code is added after original fucntion')

    return wrap_the_gift

# def gift_need_decoration():
#     print('i need wrapping')

# gift_need_decoration()

# decorated_func = gift_dec(gift_need_decoration)
# decorated_func()

# @gift_dec
def gift_need_decoration():
    print('i need wrapping')

gift_need_decoration()