import random
from words import words
import string
def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    lives=6
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    # getting user input
    while len(word_letters)>0 and lives>0:
        #letters used
        print('You have', lives, 'livesleft and you have used these letters: ', ' '.join(used_letters))
        #what current word is (ie W- R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ' '.join(word_list))
        user_letter = input("guess a letter : ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives=lives-1
        elif user_letter in used_letters:
            print("you have already used that character. please try againn.")
        else:
            print("Invalid character. please try again.")

    #gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print("You have died! Sorry the word was", word)
    else :
        print("you have won! The word", word, "!!")
# user_input = input("Type Something: ")
# print(user_input)
hangman()