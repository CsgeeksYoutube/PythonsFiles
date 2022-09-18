# def sqr(n):
    
#     for x in range(n):
#         yield x**2
        
# for x in sqr(10):
#     print(x)

# def gen():
#     for x in range(3):
#         yield x

# # for number in gen():
# #     print(number)

# g= gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

a='vijay'

# for letter in a:
#     print(letter)

a_iter =iter(a)
print(next(a_iter))
print(next(a_iter))
print(next(a_iter))
print(next(a_iter))
print(next(a_iter))