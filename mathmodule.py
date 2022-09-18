
# import math
# value = 5.64
# c=math.floor(value)
# print(c)
# d=math.ceil(value)
# print(d)
# print(round(4.54))
# from math import pi
# print(pi)
# print(math.e)
# print(math.inf)
# print(math.log(1000,10))
# print(math.sin(10))
# print(math.degrees(pi/2))
# print(math.radians(180))

import random

# c=random.randint(0,100)
# print(c)
list1= list(range(0,40))
# print(list1)
# d=random.choice(list1)
# print(d)
# with replacement
g=random.choices(population=list1, k=5)
print(g)
# without replacement

f= random.sample(population=list1,k=6)
print(f)
print(list1)
random.shuffle(list1)
print(list1)