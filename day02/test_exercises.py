from day02.exercises import (
    capitalize_words,
    chunk,
    grade_label,
    initials,
    is_palindrome,
    last_items,
    longest_word,
    reverse_text,
    without_duplicates,
)


def test_initials():
    assert initials("Ada Lovelace") == "A.L."
    assert initials("guido van rossum") == "G.V.R."
    assert initials("Cher") == "C."


def test_reverse_text():
    assert reverse_text("hello") == "olleh"
    assert reverse_text("") == ""


def test_is_palindrome():
    assert is_palindrome("Racecar") is True
    assert is_palindrome("Never odd or even") is True
    assert is_palindrome("hello") is False


def test_last_items():
    assert last_items([1, 2, 3, 4], 2) == [3, 4]
    assert last_items([1, 2, 3, 4], 0) == []
    assert last_items([1, 2], 5) == [1, 2]


def test_without_duplicates():
    assert without_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert without_duplicates([]) == []


def test_without_duplicates_does_not_change_input():
    numbers = [3, 1, 3, 2, 1]
    without_duplicates(numbers)
    assert numbers == [3, 1, 3, 2, 1]


def test_capitalize_words():
    assert capitalize_words("hello big world") == "Hello Big World"
    assert capitalize_words("learn python") == "Learn Python"
    assert capitalize_words("iPhone mcDonald") == "IPhone McDonald"


def test_grade_label():
    assert grade_label(1.0) == "fail"
    assert grade_label(5.49) == "fail"
    assert grade_label(5.5) == "pass"
    assert grade_label(7.99) == "pass"
    assert grade_label(8.0) == "excellent"
    assert grade_label(10.0) == "excellent"


def test_longest_word():
    assert longest_word("I love Python a lot") == "Python"
    assert longest_word("cat dog") == "cat"
    assert longest_word("hello") == "hello"


def test_chunk():
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk([1, 2, 3], 3) == [[1, 2, 3]]
    assert chunk([], 2) == []
