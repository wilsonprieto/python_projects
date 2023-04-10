# hangman_game rules is there is a word need to guessd
# but the input is only a letter until the word will display
# display each corrected letters
# give a hint the number of letters of the word
# set the max guess to 8
# set the max time to 30 seconds
# make a host for the game!

import random
import time



print("""
    __    __       ___      .__   __.     _____  .___  ___.      ___      .__   __.
   |  |  |  |     /   \     |  \ |  |   /  ____| |   \/   |     /   \     |  \ |  |
   |  |__|  |    /  ^  \    |   \|  |  |  |  __  |  \  /  |    /  ^  \    |   \|  |
   |  |  |  |   / _____ \   |  |\   |  |  |__| | |  |  |  |   /  ____ \   |  |\   |
   |__|  |__|  /_/     \_\  |__| \__|   \______| |__|  |__|  /_/     \_\  |__  \__|""")
    
# make a host

print("Welcome to HANGMAN GAME!!")
time.sleep(2)
print("There is a random word and our category is PROGRAMMING LANGUAGE")
time.sleep(1)
print("You only have 30 second to guessed and a maximum of 8 guesses only.")
time.sleep(3)
print("So be fast and wise. LETS GO!")

# make a list where we can have a source for a random word.

word_list = ["python", "java", "ruby", "javascript",
             "html", "css", "php", "swift", "sql", "perl"]

# set the max guessed
max_guesses = 8
# set the maxtimer in seconds
max_time = 30
mistakes = {
    7:"""
   +---+
   |   |
       |
       |
       |
       |
=========""",
6:"""
   +---+
   |   |
   O   |
       |
       |
       |
=========""",

5:"""
   +---+
   |   |
   O   |
   |   |
       |
       |
=========""",
4:"""
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========""",
 3:"""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========""",
2:"""
     +---+
     O   |
    /|\  |
    /    |
        ===
    """,
1:"""
     +---+
     O   |
    /|\  |
    / \  |
        ===
    """,
0:"""+---+
     O   |
    /|\  |
    / \  |
        ===
    """,
}
# make a function for taking ramdom word from a the list provided
def word_random():
    
    # use return to call the function (word random)
    return random.choice(word_list)
# use function or make a function for the game
def play_game():
    max_guesses = 8
    word = word_random()
    guessed = [] # make a list for the letters
    print("The word has", len(word), "letters") # give a hint
    time_start = time.time()

    # make a loop for the time and for the guessed

    while max_guesses > 0:
        if time.time() - time_start > max_time:
            print("Time ended. The word was `{}`".format(word).upper())

            # get the user input
        guess = input("please input your letter guess for the word: ").lower()

        # input is only 1 letter at a time or guess
        if len(guess) != 1 or not guess.isalpha(): # need to be a letter
            print("Invalid guessed input only one letter for the guessed word!")
            continue  # continue the loop

        # if letter is already guessed make a if
        if guess in guessed:
            print("You already guessed that letter. please try another!")
            continue  # continue the loop

        # store the input to guessed, use append to store
        guessed.append(guess)

        # if corrrect letter guess
        if guess in word:
            print("That is a Correct Letter!")
        else:
            max_guesses -= 1

            print("Sorry! Incorrect letter.", end=' ') # put end so the mistakes will not add to guessed list.

            print(mistakes[max_guesses])

        current_letter = ""
        for letter in word:
            if letter in guessed:
                current_letter += letter
            else:
                current_letter += "_"  # use underscore for the letter not guessed
        print(current_letter)
        # check if the player win
        if "_"not in current_letter:
            print("Congratulations! You guessed the word. You win 1 million. sana all!")
            return
        # print the remaining guessed
        print("You have {} remaining guess".format(max_guesses))
        
    print("You use all your 8 guesses sorry! The word was `{}`".format(word).upper())


play_game()






