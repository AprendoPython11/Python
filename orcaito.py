import random
from words import words #Se importa de nuestro archivo words.py
import string #para traer el alfabeto


def get_word(param_words):
    word = random.choice(param_words)

    while '-' in word or ' ' in word:
        word = random.choise(param_words)

    return word



def game_orcaito():
    own_word = get_word(words)
    letters_word = set(own_word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()

    
    while len(letters_word) > 0:
        word_list = [letter if letter in used_letters else " - " for letter in own_word]
        print("Current word ", ''.join(word_list))

        user_letter = input("Enter some letter for guess the word ").lower()

        # in es para saber si está y - es para saber si no está incluido
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in letters_word:
                letters_word.remove(user_letter)
                num_letter = len(letters_word)
               
        elif user_letter in used_letters:
            print("You alredy used this character, please try again")
        
        else:
            print("That was a invalid character, please try again")

    return f"You did! {own_word} it was the word."
            
print(game_orcaito())
