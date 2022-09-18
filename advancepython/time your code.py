# def func1(n):
#     return [str(num) for num in range(n)]

# # print(func1(10))

# def func2(n):
#     return list(map(str,range(n)))

# print(func2(10))

# import time
# starttime= time.time()
# result= func1(1000)
# endtime= time.time()
# elapsedtime=endtime-starttime
# print(elapsedtime)


# starttime= time.time()
# result= func2(1000)
# endtime= time.time()
# elapsedtime=endtime-starttime
# print(elapsedtime)

import timeit
stmt= '''
func1(100)
'''
setup='''
def func1(n):
    return [str(num) for num in range(n)]
'''

stmt2= '''
func2(100)
'''
setup2='''
def func2(n):
    return list(map(str,range(n)))
'''

a=timeit.timeit(stmt,setup,number=100000)
b=timeit.timeit(stmt2,setup2,number=100000)

print(a)
print(b)