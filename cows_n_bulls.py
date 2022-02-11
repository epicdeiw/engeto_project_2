import random


# Game greets the player
def greeting():
    print("Welcome to the game of cows and bulls!")
    print(makeup())


# Simple divider
def makeup():
    divider = 50 * "="
    return divider


# Read the rules of the game
def rules():
    rules_str = '''The number to be guessed must be a 4 digit number. 
You can use only digits from 1 - 9 and 0.
The guessed number cannot start with zero.
There cannot be any repeated numbers.
Bull - correct number in correct position.
Cow - correct number in wrong possition.
To quit the game, input "END"'''

    while True:
        read_rules = input("Before we start, would you like to read the rules (y,n): ")
        print(makeup())
        if read_rules == "y":
            print(rules_str)
            print(makeup())
            break
        elif read_rules == "n":
            print("Ok, let's continue")
            print(makeup())
            break
        else:
            print("Do you want to read the rules or not?")
            continue
        return rules()


# Creating random 4 digit number
def make_number() -> str:
    while True:
        number = str(random.randint(1000, 9999))
        if len(number) == len(set(number)):
            return number


# Player inputs the guess
def player_guess():
    guess = str(input("Enter your guess: "))
    print(makeup())
    return guess


def cow_check(guess, number_rnd):
    cow = 0
    for num in guess:
        if num in number_rnd:
            cow += 1
    return cow


def bull_check(guess, number_rnd):
    bull = 0
    for y, number_rnd in enumerate(number_rnd):
        if number_rnd in guess[y]:
            bull += 1
    return bull


# Counting sum of cows
def cow_sum(bull, cow):
    sum = cow - bull
    return sum


# Controling correctness of player's inputs
def player_control(guess, number_rnd):
    guess_check = str(guess)
    control = True
    singularity = []
    while True:
        if len(guess_check) == len(set(guess_check)) and guess_check.isnumeric() \
                and not guess_check.startswith("0") and len(guess_check) == 4:
            for num in str(guess_check):
                if num not in singularity:
                    singularity.append(num)
        elif guess.upper() == "END":
            print("Terminating the game!")
            print(f"Your number was {number_rnd}")
            quit()
        else:
            print("That is not a correct input, try again!")
            control = False
            break
        break
    return control


def plural_singular(bull, cow):
    bull_single_plural = ""
    cow_single_plural = ""

    if bull <= 1:
        bull_single_plural = "Bull"
    else:
        bull_single_plural = "Bulls"

    if cow <= 1:
        cow_single_plural = "Cow"
    else:
        cow_single_plural = "Cows"

    return bull_single_plural, cow_single_plural


# Function to replay the game
def play_again():
    while True:
        again = input("Play again (y,n): ")
        print(makeup())
        if again == "y":
            make_number()
            play_game()
        elif again == "n":
            print("Thanks for playing!")
            quit()
        else:
            print("y or n are the only valid answers here")
            print(makeup())
        return play_again()


# Connecting all functions into one
def play_game():
    game_runs = True
    secret_num = make_number()
    attempts = 0
    greeting()
    rules()
    while game_runs:
        player_tip = player_guess()
        player_input_correct = player_control(player_tip, secret_num)
        if player_input_correct == True:
            bull = bull_check(player_tip, secret_num)
            cow = cow_check(player_tip, secret_num)
            number_of_cows = cow_sum(bull, cow)
            # print(secret_num) # Remove to hide the secret number
            print(bull, plural_singular(bull, number_of_cows)[0])
            print(number_of_cows, plural_singular(bull, number_of_cows)[1])
            print(makeup())
            attempts += 1
            if bull == 4:
                print(f"You won the game, your number was {secret_num}")
                print(f"It took you {attempts} attempts")
                game_runs = False

                play_again()


# Calling the function to iniate the game
play_game()
