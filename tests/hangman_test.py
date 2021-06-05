import pytest


from src.hangman import Hangman
from src.hangman_art import hangman_stages


# test Hangman.select_word()
def test_select_word_from_one_element_list() -> None:
    words_list = ["word"]
    hangman = Hangman(words_list)

    hangman.select_word()
    
    assert hangman.selected_word == words_list[0]
    assert len(hangman.guessed_letters) == len(hangman.selected_word)
    assert all([letter == "_" for letter in hangman.guessed_letters])


def test_select_word_from_multiple_elements_list() -> None:
    words_list = ["first", "second", "third"]
    hangman = Hangman(words_list)

    hangman.select_word()

    assert hangman.selected_word in words_list
    assert len(hangman.guessed_letters) == len(hangman.selected_word)
    assert all([letter == "_" for letter in hangman.guessed_letters])


def test_select_word_from_an_empty_list() -> None:
    words_list = []
    hangman = Hangman(words_list)

    with pytest.raises(ValueError):
        hangman.select_word()


def test_select_word_incorrect_argument_type() -> None:
    words_list = "word"
    hangman = Hangman(words_list)

    with pytest.raises(ValueError):
        hangman.select_word()


def test_select_word_list_contains_not_strings() -> None:
    words_list = ["word", 123, ("tuple", 1)]
    hangman = Hangman(words_list)

    with pytest.raises(ValueError):
        hangman.select_word()


# test Hangman.guess_a_letter(self, letter)
def test_guess_a_letter_correct_letter_guessed() -> None:
    words_list = ["word"]
    hangman = Hangman(words_list)
    hangman.select_word()
    hangman.guessed_letters = ["_", "_", "_", "_"]
    letter = "w"

    hangman.guess_a_letter(letter)
    assert hangman.misses == 0
    assert hangman.selected_word == "word"
    assert hangman.guessed_letters == ["w", "_", "_", "_"]


def test_guess_a_letter_uppercase_letter_guessed() -> None:
    words_list = ["word"]
    hangman = Hangman(words_list)
    hangman.select_word()
    letter = "D"

    hangman.guess_a_letter(letter)
    assert hangman.misses == 0
    assert hangman.selected_word == "word"
    assert hangman.guessed_letters == ["_", "_", "_", "d"]


def test_guess_a_letter_incorrect_letter_guessed() -> None:
    words_list = ["word"]
    hangman = Hangman(words_list)
    hangman.select_word()
    letter = "z"

    hangman.guess_a_letter(letter)
    assert hangman.misses == 1
    assert hangman.selected_word == "word"
    assert hangman.guessed_letters == ["_", "_", "_", "_"]


def test_guess_a_letter_incorrect_argument_type() -> None:
    words_list = ["word"]
    hangman = Hangman(words_list)

    with pytest.raises(ValueError):
        hangman.guess_a_letter(1)


def test_guess_a_letter_empty_string() -> None:
    words_list = ["word"]
    hangman = Hangman(words_list)

    with pytest.raises(ValueError):
        hangman.guess_a_letter("")


def test_guess_a_letter_too_long_string() -> None:
    words_list = ["word"]
    hangman = Hangman(words_list)

    with pytest.raises(ValueError):
        hangman.guess_a_letter("word")


def test_guess_a_letter_not_letter() -> None:
    words_list = ["word"]
    hangman = Hangman(words_list)

    with pytest.raises(ValueError):
        hangman.guess_a_letter("1")


def test_guess_a_letter_guessed_multiple_letters() -> None:
    words_list = ["alaska"]
    hangman = Hangman(words_list)
    hangman.select_word()
    letter = "a"

    hangman.guess_a_letter(letter)
    assert hangman.misses == 0
    assert hangman.selected_word == "alaska"
    assert hangman.guessed_letters == ["a", "_", "a", "_", "_", "a"]


def test_check_if_game_ended_lost_game() -> None:
    words_list = ["word"]
    hangman = Hangman(words_list)
    hangman.select_word()

    for stage in hangman_stages:
        hangman.guess_a_letter("a")

    assert hangman.check_if_game_ended() == True


def test_check_if_game_ended_win_game() -> None:
    words_list = ["word"]
    hangman = Hangman(words_list)
    hangman.select_word()

    for letter in "word":
        hangman.guess_a_letter(letter)

    assert hangman.check_if_game_ended() == True


def test_check_if_game_ended_game_started() -> None:
    words_list = ["word"]
    hangman = Hangman(words_list)
    hangman.select_word()

    assert hangman.check_if_game_ended() == False


def test_check_if_game_ended_game_in_play() -> None:
    words_list = ["word"]
    hangman = Hangman(words_list)
    hangman.select_word()

    for letter in "wo":
        hangman.guess_a_letter(letter)

    assert hangman.check_if_game_ended() == False

