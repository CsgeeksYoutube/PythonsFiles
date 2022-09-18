import datetime
# time= datetime.time(15,45,20,60)
# print(time.second)
# print(time)
# today= datetime.date.today()
# # print(today.month)
# print(today.ctime())

from datetime import datetime
# datetime1= datetime(2023,10,3,15,25,26)
# print(datetime1)
# datetime1=datetime1.replace(year=2022)
# print(datetime1)

from datetime import date
date1= date(2021,11,15)
date2=date(2022,11,16)
result = date1-date2
print(result)
print(result.days)

datetime1= datetime(2020,11,5,22,0)
datetime2=datetime(2021,11,5,12,0)
result1=datetime1-datetime2
print(result1)
