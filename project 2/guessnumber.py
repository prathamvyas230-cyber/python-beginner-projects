import random

# Generate a random secret number between 1 and 100
commputer = random.randint(1, 100)

a = -1              # stores the user's current guess (-1 so the loop starts)
guess = 0           # counts how many guesses have been made
total_guess = 10    # max number of attempts allowed
low = 1             # current lower bound of possible answer
high = 100          # current upper bound of possible answer

# Keep looping until the user guesses the correct number
while (a != commputer):
    guess += 1  # increment guess count on every attempt

    try:
        # Take user input and convert it to an integer
        a = int(input(f'Guess a number between {low} and {high}: '))

        if (a > commputer):
            # Guess too high -> narrow the upper bound
            high = a - 1
            print('Guess the lower number')

        elif (a == commputer):
            # Correct guess -> show number of attempts taken
            print(f'Your guess is right the number is{commputer} in the number of guesses is {guess}')

        else:
            # Guess too low -> narrow the lower bound
            low = a + 1
            print('Guess the higher number')

        # Check if attempts are used up (but only if the answer is still wrong)
        if (guess >= total_guess and a != commputer):
            print('You completed your total attempts')
            again = input('Do you want to play again yes/no:  ?')

            if again != 'yes':
                print('Thank for using game')
                break   # exit the loop if user doesn't want to continue

    except ValueError:
        # Handles non-numeric input so the program doesn't crash
        print('Please enter a valid number')