import random

def Hangman():
    word_list = ["python", "java", "swift", "javascript"]
    random_word = random.choice(word_list)


    random_word_hidden = list(random_word)
    for i in range(len(random_word)):
        random_word_hidden[i] = '-'

    i = 0
    list1 = []

    while i != 8:

        print(f'''\n{"".join(random_word_hidden)}
Input a letter: >''', end=" ")

        inp_word = input()

        random_word = list(random_word)

        if len(inp_word) == 0:
            print("Please, input a single letter.")
            i -= 1
        elif not inp_word.isalnum() or not inp_word.islower():
            print("Please, enter a lowercase letter from the English alphabet.")
            i -= 1
        elif len(inp_word) > 1:
            print("Please, input a single letter")
            i -= 1
        elif inp_word in list1:
            print("You've already guessed this letter.")
            i -= 1
        elif inp_word in random_word:
            i -= 1
            for index, j in enumerate(random_word):
                if j == inp_word:
                    random_word_hidden[index] = inp_word
        elif inp_word not in random_word:
            print("That letter doesn't appear in the word.")

        if "".join(random_word_hidden) == "".join(random_word):
            print(f'''
{"".join(random_word)}
You guessed the word {"".join(random_word)}!
You survived!''')
            break

        list1.append(inp_word)
        i += 1

    if i == 8:
        print("\nYou lost!")
        return 0

print("H A N G M A N")
win = 0
lose = 0



def Pre_Hangman(win, lose):
    print('''Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: >''', end=" ")
    while True:
        game_input = input()
        if game_input != "play" and game_input != "results" and game_input != "exit":
            print('Please, type "play", "results" or "exit" > ', end="")
        else:
            if game_input == "results":
                print(f'''You won: {win} times.
You lost: {lose} times.''')
                Pre_Hangman(win, lose)

            elif game_input == "play":
                if Hangman() == 0:
                    lose += 1
                    Pre_Hangman(win, lose)
                else:
                    win += 1
                    Pre_Hangman(win, lose)

            elif game_input == "exit":
                quit()

Pre_Hangman(win, lose)







