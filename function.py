# def name_of_function(name='Vijay'):
#     print(f'hello{name}')

# name_of_function('ajay')
# # print(a)

def even_check(num_list):
    for number in num_list:
        if number %2 ==0:
            return True
        else:
            pass
    return False

a=even_check([1,5,3])
print(a)