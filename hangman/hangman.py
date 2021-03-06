#!/usr/bin/env python3
import random
import os
from hangman import hangman_art as ha
from hangman import helpers


class Hangman():

    def __init__(self, words):
        self.words = words
        self.selected_word = ""
        self.guessed_letters = []
        self.misses = 0

    def guess_a_letter(self, letter):
        if not isinstance(letter, str):
            raise ValueError(
                    f"Expected a string but got {type(letter)} instead.")
        if len(letter) != 1:
            raise ValueError(
                    "Expected a single character string but got"
                    f" {len(letter)} characters instead.")
        if not letter.isalpha():
            raise ValueError(f"Expected a letter but got {letter} instead.")
        letter = letter.lower()
        for index, l in enumerate(self.selected_word):
            if letter == l:
                self.guessed_letters[index] = letter
        if letter not in self.guessed_letters:
            self.misses += 1
            if self.misses > len(ha.hangman_stages) - 1:
                self.misses = len(ha.hangman_stages) - 1

    def select_word(self):
        if not isinstance(self.words, list):
            raise ValueError(
                    "Method was expecting a list, but got "
                    f"{type(self.words)} instead.")
        if not self.words:
            raise ValueError("Words list should not be empty.")
        if not all(isinstance(word, str) for word in self.words):
            raise ValueError(
                    f"Expected a list of type {str}. "
                    "It should not contain elements of other types.")
        self.selected_word = random.choice(self.words)
        self.guessed_letters = ["_" for letter in self.selected_word]

    def check_if_game_ended(self):
        if ((self.misses >= len(ha.hangman_stages)-1)
                or list(self.selected_word) == self.guessed_letters):
            return True
        return False


def draw_menu():
    print(ha.hangman_title, ha.hangman_stages[-1])
    print("1. Start a new game.\n2. Exit.\n")


def draw_game_table(hangman):
    print(" ".join(hangman.guessed_letters))
    print(ha.hangman_stages[hangman.misses])


def print_end_game_communicate(hangman):
    if "_" not in hangman.guessed_letters:
        print("Congratulations! You have guessed a word: "
              f"\"{hangman.selected_word.upper()}\".")
    else:
        print("You have lost, the word was "
              f"\"{hangman.selected_word.upper()}\". "
              "But don't worry, you can try one more time!\n")


def main():
    exit_program = False
    words_path = os.path.join(os.path.dirname(
        os.path.dirname(__file__)), "words.csv")
    words = helpers.read_csv(words_path)

    while not exit_program:
        draw_menu()
        choice = input("Your choice: ")

        if choice == "1":
            end_game = False
            hangman = Hangman(words)
            try:
                hangman.select_word()
            except ValueError:
                print("Program is unable to read list of words. "
                      f"Please check {words_path}.")
                input("\nPress any key to exit program...")
                break
            draw_game_table(hangman)
            while not end_game:
                try:
                    hangman.guess_a_letter(input("Select a letter: "))
                except ValueError:
                    print("You have entered an incorrect value. Try again.")
                draw_game_table(hangman)
                end_game = hangman.check_if_game_ended()
            print_end_game_communicate(hangman)
            input("Press any key to continue.")
        elif choice == "2":
            exit_program = True


if __name__ == '__main__':
    main()
