import random

# Computer randomly picks one of: snake(1), water(-1), gun(0)
computer = random.choice([1, -1, 0])

# Take user's choice as a single letter: s / w / g
you = input('Enter your choice : ')

# Map letters to numbers so choices can be compared easily
youdict = {'s': 1, 'w': -1, 'g': 0}

# Reverse map to convert numbers back to readable names for display
reversedict = {1: 'snake', -1: 'water', 0: 'gun'}

# Convert user's letter choice into its number form
youstr = youdict[you]

# Show what both player and computer picked
print(f'In game you chose {reversedict[youstr]} \n And computer chosed {reversedict[computer]}')

# Compare choices to decide the result
if (youstr == computer):
    print('game is draw')
else:
    # Snake vs Water -> snake drinks water, you win
    if (youstr == 1 and computer == -1):
        print('you won')

    # Snake vs Gun -> gun kills snake, you lose
    elif (youstr == 1 and computer == 0):
        print('you lose')

    # Water vs Snake -> snake drinks water, you lose
    elif (youstr == -1 and computer == 1):
        print('you lose')

    # Water vs Gun -> water ruins gun, you win
    elif (youstr == -1 and computer == 0):
        print('you win')

    # Gun vs Snake -> gun kills snake, you won
    elif (youstr == 0 and computer == 1):
        print('you won')

    # Gun vs Water -> water ruins gun, you lose
    elif (youstr == 0 and computer == -1):
        print('you lose')