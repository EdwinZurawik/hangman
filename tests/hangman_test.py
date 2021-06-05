import pytest


from src.hangman import Hangman


def test_select_word_from_one_element_list() -> None:
    hangman = Hangman()
    words_list = ["word"]

    assert hangman.select_word(words_list) == words_list[0]


def test_select_word_from_multiple_elements_list() -> None:
    hangman = Hangman()
    words_list = ["word1", "word2", "word3"]

    assert hangman.select_word(words_list) in words_list


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
