from random import shuffle


# list1=shuffle(example)
# print(list1)
def shuffle_list(list):
    shuffle(list)
    return list

def player_guess():
    guess1=''
    while guess1 not in ['0','1','2']:
        guess1 = input("pick a number:0,1,2")
    return int(guess1)

def check_guess(list,guess1):
    if list[guess1]=='B':
        print('correct')
    else:
        print("wrong number")
        print(list)


list=['','B','']
mix_list= shuffle_list(list)
guess = player_guess()
check_guess(mix_list,guess)