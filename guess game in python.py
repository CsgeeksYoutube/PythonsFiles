from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess=''
    guess = input("choose a number: 0,1,2")
    return int(guess)

def check_guess():
    if mylist[guess] == 'O':
        print("correct")
    else:
        print("wrong guess")
        print(mylist)


mylist =['','O','']
mixedup_list= shuffle_list(mylist)
print(mixedup_list)
guess= player_guess()
check_guess(mixedup_list,guess)
