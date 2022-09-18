# from collections import Counter

# list =[1,1,1,1,2,2,2,3,3,4,4,5,5]
# print(Counter(list))
# list2=['a','a','a','b','m',10,20,20,10]
# print(Counter(list2))

# sent="hello frnd how r u "
# print(Counter(sent.split()))
# letters='aaaaabbbbbbcccdddffff'
# c=Counter(letters)
# print(c.most_common())

# from collections import defaultdict

# # d={'a':20}
# # print(d)
# # print(d['a'])
# # print(d['b'])

# dic= defaultdict(lambda: 5)
# dic['a']= 200
# dic['b']= 400
# print(dic['c'])


from collections import namedtuple
Cat= namedtuple('cat',['age','breed','name'])
tom = Cat(age=2,breed='roadside',name='tommy')
print(tom)
print(tom.age)
print(tom.breed)