questions = [
    # [question, option_a, option_b, option_c, option_d, correct_option_number]
    ["Which language was used to create Facebook (backend)? ", 'python', 'french', 'javascript', 'php', 4],
    ["Which company created Python? ", 'Google', 'CWI (Guido van Rossum)', 'Microsoft', 'Facebook', 2],
    ["What does HTML stand for? ", 'HighText Machine Language', 'HyperText and Markup Language', 'HyperText Markup Language', 'Home Tool Markup Language', 3],
    ["Which company owns GitHub? ", 'Google', 'Amazon', 'Microsoft', 'Apple', 3],
]

# Prize money for each level (question index -> reward)
levels = [1000, 2000, 3000, 4000, 40000, 10000, 20000, 40000, 1000001]

money = 0  # tracks total winnings
i = 0

# Loop through each question one by one
for i in range(0, len(questions)):
    question = questions[i]  # current question's data

    print(f'question for rs. {levels[i]}')
    # Print the 4 options (a, b, c, d) stored at index 1-4 of the question list
    print(f'a. {question[1]}         b. {question[2]}')
    print(f'c. {question[3]}         d. {question[4]}')

    # Take user's answer as option number (1-4)
    reply = int(input('Enter your answer: '))

    # Check if the answer matches the correct option (stored as last item, index -1)
    if (reply == question[-1]):
        print(f'Correct answer, you won have won rs {levels[i]}')

        # Special bonus levels (currently unreachable since there are only 4 questions)
        if (i == 4):
            money = 4000
        elif (i == 9):
            money = 1000000
    else:
        print('wrong answer ')
        break  # game ends immediately on a wrong answer
