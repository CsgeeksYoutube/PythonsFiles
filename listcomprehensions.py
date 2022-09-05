from unittest import result


mystring = 'hello'
# mylist=[]
# for a in mystring:
#     mylist.append(a)
# print(mylist)
# list2=[a**2 for a in range(0,11) if a%2==0]
# print(list2)

cel =[0,10,20,30,40]
# fah=[]
# for temp in cel:
#     fah.append((9/5)*temp +32)

# print(fah)
# fah2=[((9/5)*temp +32) for temp in cel]
# print(fah2)

# list3=[x*y for x in [2,4,6] for y in [1,10,100]]
# print(list3)
# for x in [2,4,6]:
#     for y in [1,10,100]:
#         list3.append(x*y)
# print(list3)



result =[x if x%2==0 else 'odd number' for x in range(0,4) ]
print(result)
