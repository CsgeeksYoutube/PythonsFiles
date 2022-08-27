price=[('apple',200),('mango',100),('grapes',50)]
# for item in price:
#     print(item)

# for name,item in price:
#     print(name)
exam_number=[('vijay',200),('ajay',1000),('ramesh',50)]
def number_check(exam_number1):
    max_value=0
    student_name=''

    for name,number1 in exam_number1:
        if number1 > max_value:
            max_value= number1
            student_name = name
        else:
            pass

    return(student_name,max_value)

a,b=number_check(exam_number)
print(a)
print(b)

