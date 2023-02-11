import random
def start_text():
    '''Output gretting text, and choose difficulty'''
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return difficulty

def create_number():
    '''Create number, that you must guess'''
    number_for_guessing = random.randint(1, 100)
    return number_for_guessing

def checking_number(guess_number):
    '''Checking input number to equal guess number'''
    number = int(input("Make a guess: "))
    flag = False
    if number > guess_number:
        print("Too high.")
    elif number < guess_number:
        print("Too low.")
    else:
        print("You win")
        flag = True
    return flag

def loop_for_guessing(difficulty, guess_number):
    '''Loop for guess number'''
    i = difficulty
    while i > 0:
        print(f"You have {i} attempts remaining to guess the number")
        flag = checking_number(guess_number)
        if flag == True:
            break
        if i == 1:
            print("You lose")
        i -= 1

def choose_difficulty(difficulty):
    '''Choose difficulty (hard or easy)'''
    number = create_number()
    if difficulty == 'hard':
        loop_for_guessing(5, number)
    else:
        loop_for_guessing(10, number)



def main():
    '''run program'''
    difficulty = start_text()
    choose_difficulty(difficulty)


if __name__ == '__main__':
    main()