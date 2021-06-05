import random
from src import hangman_art as ha

words = ['first', 'second', 'four']

class Hangman():

    def __init__(self):
        pass

    def draw_menu(self):
        print(ha.hangman_title, ha.hangman_stages[-1])

    def select_word(self, words):
        if not isinstance(words, list):
            raise ValueError(f"Method was expecting a list, but got {type(words)} instead.")
        if not words:
            raise ValueError("Words list should not be empty.")
        if not all(isinstance(word, str) for word in words):
            raise ValueError(f"Expected a list of type {str}. It should not contain elements of other types.")
        selected_word = random.choice(words)
        return selected_word

def main():
    end_game = False
    hangman = Hangman()

    while not end_game:
        hangman.draw_menu()
        word = hangman.select_word(words)
        print(f"Your selected word is: {word}")
        input("Press any key to exit.")
        end_game = True

if __name__ == '__main__':
    main()
