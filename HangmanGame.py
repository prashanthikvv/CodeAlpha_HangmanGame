import random

list_of_words = ['grape', 'light', 'table', 'plant', 'pillow']
random_word = random.choice(list_of_words) #Randomly chooses one word.
guessed_letters = []
tries = 6

print("------WELCOME TO HUNGMAN------")
print("Guess the word, one letter at a time...")
print('_ '*len(random_word))

while tries>0:
    guess_a_letter = input("\nEnter a letter: ").lower()

    #Check if the guess is a single alphabet and its length is 1.
    if not guess_a_letter.isalpha() or len(guess_a_letter) != 1:
        print("Please enter only a single alphabet.")
        continue

    if guess_a_letter in guessed_letters:
        print("You have already guessed the letter.")
        continue
    guessed_letters.append(guess_a_letter)

    if guess_a_letter in random_word:
        print("Correct guess!!")
    else:
        print("Wrong guess, try again!!")
        tries-=1

    #Check is letters in random_word are present in the guessed_letters.
    display_word = ''
    for letter in random_word:
        if letter in guessed_letters:
            display_word+=letter+" "
        else:
            display_word+="_ "

    print("Word: ", display_word.strip())
    print("Tries left: ",tries)

    if all(letter in guessed_letters for letter in random_word):
        print("\nYou guessed the word ",random_word," correctly!!")
        break 

if tries==0:
    print("\nSorry!! The game is over.\nBetter luck next time.")
    print("\nThe word was: ", random_word)