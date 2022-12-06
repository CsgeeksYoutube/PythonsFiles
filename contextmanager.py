# with open('data.txt','w') as f:
#     f.write('tha password is 4')
 
# f = open('data.txt','w')
# with f as g:
#     print(f is g)

# class LogContMang:
#     def __enter__(self):
#         print('u r in enter block')
#         return 'you r in with block'
#     def __exit__(self,exc_type,exc_val,exc_tb):
#         if exc_type is None:
#             print('u r in exit block ')
#         else:
#             print('exception is {}{}{}'.format(exc_type,exc_val,exc_tb))
#             return True
# try:    
#     with LogContMang() as x:
#         print(x)
#         raise ValueError('Some is not right')
# except ValueError:
#     print('Value error is detected ')

    
import contextlib
# @contextlib.contextmanager
# def nest_test(name):
#     print('entery',name)
#     yield
#     print('exit',name)

# with nest_test('inner'):
#     print('BOdy')
# @contextlib.contextmanager
# def logContext():
#     print('enter')
#     try:
#         print('hello')
#         yield ' u r in with block'
#         print('exit')
#     except Exception:
#         print('exception')

# with logContext():
#     raise TypeError('error')


@contextlib.contextmanager
def PropagateExc(name, propagate):
    print('enter', name)
    try:
        print('entry 2 ',name)
        yield
        print(name,'exit without exception')
    except Exception:
        print(name,'received an exception')
        if propagate:
            raise
    
with PropagateExc('outer', True):
    with PropagateExc('inner',True):
        raise TypeError('error error mera naam')
