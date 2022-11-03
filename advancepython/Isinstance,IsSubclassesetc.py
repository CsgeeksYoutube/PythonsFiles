# print(isinstance(3, int))
# print(isinstance('hello',str))

# class A:
#     def func(self):
#         return 'A. func'

# class B(A):
#     def func(self):
#         return 'b. func'

# class C(A):
#     def func(self):
#         return 'c. func'

# class D(C,B):
#     pass

# print(D.mro())
# d= D()
# print(d.func())

class A:pass
class B(A):pass

class C(A):pass

class D(B,A,C):pass


