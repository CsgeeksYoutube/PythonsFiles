from fractions import Fraction
a= Fraction(2,3)
print(a)
# b= Fraction(2,0)
# print(b)
print(Fraction(0.5))
print(Fraction(0.1))
print(Fraction('0.1'))
print(Fraction('22/7'))

d=Fraction(2,3)  + Fraction(4,5)
print(d)
e=Fraction(2,3)  - Fraction(4,5)
print(e)
f=Fraction(2,3)  * Fraction(4,5)
print(f)
g=Fraction(2,3)  / Fraction(4,5)
print(g)

from math import floor
k=floor(Fraction('4/3'))
print(k)