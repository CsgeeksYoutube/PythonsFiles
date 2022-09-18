text='my phone number is 445-569-152, the second phone number is '
import re
# pattern='number'
# c=re.search(pattern,text)
# print(c)
# print(c.start())
# print(c.end())
# print(c.group())
# print(c.span())
# d=re.findall('phone',text)
# print(len(d))

# phone= re.search(r'\d\d\d-\d\d\d-\d\d\d',text)
# print(phone)
# phone2= re.search(r'\d{3}-\d{3}-\d{3}',text)
# print(phone2)
# phone_pattern=re.compile(r'(\d{3})-(\d{3})-(\d{3})')
# result= re.search(phone_pattern,text)
# print(result.group(3))

# p=re.search(r'dog|cat','i have 2 dogs')
# print(p)
# q=re.findall(r'...at','the cat bat mat rat')
# print(q)

w=re.findall(r'[^!.?%]+','is the !.?% first number 2 and the 1 number is 5')
print(w)