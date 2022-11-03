# from math import factorial as fac
# print(fac(1000))
# import sys
# print(sys.float_info)
# print(float(10))
# print(2**53)
# print(float(2**53+1))
# print(float(2**53+2))
# print(float(2**53+3))
# print(float(2**53+4))
# a=float(0.8)
# b=float(0.7)
# print(a-b)

import decimal
print(decimal.getcontext())
from decimal import Decimal
# print(Decimal(6))
# print(Decimal('0.8'))
# a=Decimal('0.8')
# b=Decimal('0.7')
# print(a-b)

# a=Decimal(3)
# b=Decimal('3.0')
# c=Decimal('3.00')
# print(a*2)
# print(b*2)
# print(c*2)

# decimal.getcontext().prec=6
# d=Decimal('1.234567')
# print(d+Decimal(1))

# c= (-7) % 3
# print(c)

# d= Decimal(-7) % Decimal(3)
# print(d)
def is_odd(n):
    return n%2 != 0

print(is_odd(2))
print(is_odd(3))
print(is_odd(-3))
print(is_odd(-2))
print(is_odd(2.0))
print(is_odd(3.0))
print(is_odd(-2.0))
print(is_odd(-3.0))
print(is_odd(Decimal(2)))
print(is_odd(Decimal(3)))
print(is_odd(Decimal(-2)))
print(is_odd(Decimal(-3)))
print(Decimal(-3) % 2)


