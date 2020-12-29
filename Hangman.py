import random

print("H A N G M A N")
menu = (input('Type "play" to play the game, "exit" to quit: '))
print()
word = random.choice(['python', 'java', 'kotlin', 'javascript'])
chances = 0

word_so_far = list('-' * len(word))
no_improvements_list = []
string_definition = "abcdefghijklmnopqrstuvwxyz"

if menu == "play":
    while chances < 8:
        print()
        string = "".join(word_so_far)
        print(string)
        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("You should input a single letter")
        elif guess not in string_definition:
            print("Please enter a lowercase English letter")
        
        else:
            if guess not in word and guess not in no_improvements_list:
                print("That letter doesn't appear in the word")
                chances += 1
                no_improvements_list.append(guess)
                if chances == 8:
                    print("You lost!")
            elif guess in word and guess not in no_improvements_list:
                no_improvements_list.append(guess)
                for num in range(len(word)):
                    if guess == word[num]:
                        word_so_far[num] = guess
                    if "-" not in word_so_far and chances < 8:
                        chances = 8
                        print(f"You guessed the word {word}!")
                        print("You survived!")
                        break
            elif guess in no_improvements_list:
                print("You've already guessed this letter")
else:
    pass
