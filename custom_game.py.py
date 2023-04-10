# make a host
# explain the rules of the game
# make the formula of the WPMand accuracy
#convert that from import

# TO do: ....

import random
import time
import string # to get the string of alphabet
import os # to clear the terminal


os.system('cls') # clear the terminal
#--MAKE A HOST--#
player = input("                                 PLEASE TYPE YOUR NAME TO BEGIN: ")


print("                                Hello!", player.upper(), "Welcome to the game Called...")

time.sleep(3)
os.system('cls') # clear the terminal

def blink_string(string_to_blink, num_blinks):
    for i in range(num_blinks):
        print(string_to_blink, end='\r') # read the same line or string "carriage return"
        time.sleep(0.05)
        os.system('cls') # clear
        time.sleep(0.05)

# call function to blink "TAP ADDICT" 25 times
blink_string("""
 ________    ___       _______              ___        ______       _____           _____      _______
|__   __|   /   \     | |  ^  \            /   \      ||     \    ||     \    ||   ||____|    |__   __|
   | |     /  ^  \    | |_____/           /  ^  \     ||  @   \   ||  @   \   ||   ||            | |
   | |    /  ___  \   | |                /  ___  \    ||      /   ||      /   ||   ||____        | |
   |_|   /_/     \_\  |_|               /_/     \_\   ||_____/    ||_____/    ||   ||____|       |_|
""", 52)


time.sleep(1.5)

print("""                                 =========================================
                                       Here is the rules of the game
            type the random words that appear as fast as you can 5 times and in a most accurate way
                                       there are 3 levels of the game
                                 ========================================= """)

#--end of the host--#






# --make the imports --#

# define function to generate random words based on the level
def random_words(level):

    # set length of words based on the level
    if level == 1:
        length = 3 # letters
    elif level == 2:
        length = 5
    else:
        length = 8
    words = [] # empty list for the random words


    # generate 20 random words with the specified length
    for i in range(5): # number on random words.
        word = ''.join(random.choice(string.ascii_lowercase) for i in range(length)) # effects of the imports
        words.append(word) # it will append to the empty list
    return words

# make a function for the level
def tap_addict(level):

    # generate random words for the level
    words = random_words(level)
    # print the level number
    print()
    time.sleep(3)
    print(f"                                      Here it comes! Level {level}","Starts in")
    time.sleep(2.5)
    print("                                                     3")
    time.sleep(1)
    print("                                                     2")
    time.sleep(1)
    print("                                                     1")
    time.sleep(1)
    print("                                                    GO!")
    # start timer
    start_time = time.time()
    # initialize variable for number of correctly typed words
    correct_words = 0

    # loop through each word and ask the user to type it
    for word in words: 
        print()
        print(word)
        user_input = input("Type the word: ")
        # if the user types the word correctly, increment the correct_words counter
        if user_input == word:
            correct_words += 1
    # stop timer
    end_time = time.time()
    # calculate accuracy and level time
    accuracy = correct_words / len(words)
    level_time = end_time - start_time
    
    # return accuracy and level time for the level to use in main function
    return accuracy, level_time

# define main function to run the game

def main():
    # make a variables for total time and accuracy
    total_time = 0
    total_accuracy = 0

    # make a loop for the level
    for i in range(1, 4):
        # print message to indicate that the next level is starting
        if i == 2: #or level
            print("                                               Your fast!", player.upper()) # host appear
        elif i == 3:
            print("                                  Are you ready for the BOSS Level", player.upper(),"?") # host appear
        # play the current level and get accuracy and level time
        accuracy, level_time = tap_addict(i)
        # add level time to total time and accuracy to total accuracy
        total_time += level_time
        total_accuracy += accuracy
    # calculate words per minute based on total time and accuracy
    wpm = (total_time / 60 ) * (total_accuracy / 3) # formula
    # print total time, total accuracy, and words per minute
    print()
    print("                                      Good Job!", player.upper(),"here is your result")

    time.sleep(3)
    print(f"                                           Total time: {total_time:.2f} seconds")
    time.sleep(3)
    print(f"                                           Total accuracy: {(total_accuracy / 3) * 100 :.2f}","%") # formula sa accuracy
    time.sleep(3)
    print(f"                                           Words per minute: {wpm:.2f}")
    time.sleep(3)
    print("                              Play again to improve your typing speed and accuracy!!")

# call the function

main()

