import random
def start_text():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return difficulty

def create_number():
    number_for_guessing = random.randint(1, 100)
    return number_for_guessing

def checking_number(guess_number):
    number = input("Make a guess: ")
    flag = False
    if number > guess_number:
        print("Too low.")
    elif number < guess_number:
        print("Too high.")
    else:
        print("You win")
        flag = True
    if flag == False:
        print("Guess again")
    return  flag





def main():
    start_text()
    print(create_number())

if __name__ == '__main__':
    main()