import csv
data = open('example.csv',encoding='utf-8')
csvread= csv.reader(data)
lines= list(csvread)
# print(lines)
# print(len(lines))
# for line in lines[:6]:
#     print(line)
# print(lines[2][4])
# allstatus= []
# for line in lines[1:25]:
#     allstatus.append(line[4])

# print(allstatus)


fileoutput = open('save_file.csv', mode='w',newline='')
csvwrite= csv.writer(fileoutput,delimiter=',')
csvwrite.writerow(['a','b','c'])
csvwrite.writerows([['1','2','3'],['11','22','33']])
