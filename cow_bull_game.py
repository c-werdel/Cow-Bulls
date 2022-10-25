import random

def rand():
    rand_list = set()
    for x in range(4):
        n = random.randint(0,9)
        while n in rand_list:
            n = random.randint(0,9)
        rand_list.add(n)

    return(list(rand_list))

def user_list():
    guess = (input('Enter four numbers '))
    guess_log = []
    guess_log.append(guess)
    guess_log = [int(x) for x in str(guess)]
    return guess_log

def game(guess, answer):
    cow = 0
    bull = 0   
    for x in range(0,4):
        if guess[x] == answer[x]:
            cow += 1
        elif guess[x] in answer:
            bull += 1
    print("Cows: "+str(cow),"Bulls: "+str(bull))

#Victory Conditions
def main(rand_list): #will continue the while loop until a victory is True #user input game user check repeat
    while True:
        guess_log = user_list() #guess as an input means they will keep until it the if statement is False
        game(guess_log,rand_list)
        if guess_log == rand_list:
            print("Winner!")
            break 

if __name__ == "__main__":
    print("Welcome to Cows and Bulls")
    # guess_log = user_list()
    # print(f'User input: {guess_log}')
    rand_list = rand()
    # print(f'Random List: {rand_list}')
    main(rand_list)



