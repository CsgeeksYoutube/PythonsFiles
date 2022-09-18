import importexample
def func1():
    print('this is function 1')

importexample.func22()


print('top level of code is running')
if __name__ == '__main__':
    print('main example is running')
else:
    print('this mainexample.py file is imported')

