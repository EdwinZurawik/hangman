import pytest


from src.hangman import Hangman


# test Hangman.select_word(self, words)
def test_select_word_from_one_element_list() -> None:
    hangman = Hangman()
    words_list = ["word"]

    hangman.select_word(words_list)
    
    assert hangman.selected_word == words_list[0]
    assert len(hangman.guessed_letters) == len(hangman.selected_word)
    assert all([letter == "_" for letter in hangman.guessed_letters])


def test_select_word_from_multiple_elements_list() -> None:
    hangman = Hangman()
    words_list = ["first", "second", "third"]

    hangman.select_word(words_list)

    assert hangman.selected_word in words_list
    assert len(hangman.guessed_letters) == len(hangman.selected_word)
    assert all([letter == "_" for letter in hangman.guessed_letters])


def test_select_word_from_an_empty_list() -> None:
    hangman = Hangman()
    words_list = []

    with pytest.raises(ValueError):
        hangman.select_word(words_list)


def test_select_word_incorrect_argument_type() -> None:
    hangman = Hangman()
    words_list = "word"

    with pytest.raises(ValueError):
        hangman.select_word(words_list)


def test_select_word_list_contains_not_strings() -> None:
    hangman = Hangman()
    words_list = ["word", 123, ("tuple", 1)]

    with pytest.raises(ValueError):
        hangman.select_word(words_list)


# test Hangman.guess_a_letter(self, letter)
def test_guess_a_letter_correct_letter_guessed() -> None:
    hangman = Hangman()
    hangman.select_word(["word"])
    hangman.guessed_letters = ["_", "_", "_", "_"]
    letter = "w"

    hangman.guess_a_letter(letter)
    assert hangman.misses == 0
    assert hangman.selected_word == "word"
    assert hangman.guessed_letters == ["w", "_", "_", "_"]


def test_guess_a_letter_uppercase_letter_guessed() -> None:
    hangman = Hangman()
    hangman.select_word(["word"])
    letter = "D"

    hangman.guess_a_letter(letter)
    assert hangman.misses == 0
    assert hangman.selected_word == "word"
    assert hangman.guessed_letters == ["_", "_", "_", "d"]


def test_guess_a_letter_incorrect_letter_guessed() -> None:
    hangman = Hangman()
    hangman.select_word(["word"])
    letter = "z"

    hangman.guess_a_letter(letter)
    assert hangman.misses == 1
    assert hangman.selected_word == "word"
    assert hangman.guessed_letters == ["_", "_", "_", "_"]


def test_guess_a_letter_incorrect_argument_type() -> None:
    hangman = Hangman()

    with pytest.raises(ValueError):
        hangman.guess_a_letter(1)


def test_guess_a_letter_empty_string() -> None:
    hangman = Hangman()

    with pytest.raises(ValueError):
        hangman.guess_a_letter("")


def test_guess_a_letter_too_long_string() -> None:
    hangman = Hangman()

    with pytest.raises(ValueError):
        hangman.guess_a_letter("word")

def test_guess_a_letter_not_letter() -> None:
    hangman = Hangman()

    with pytest.raises(ValueError):
        hangman.guess_a_letter("1")
