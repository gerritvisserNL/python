from day04.exercises import (
    distance,
    even_numbers,
    first_letters,
    flatten,
    min_max,
    passed,
    shout_long_words,
    squares,
    word_lengths,
)


def test_min_max():
    assert min_max([3, 1, 4, 1, 5]) == (1, 5)
    assert min_max([-2, -7]) == (-7, -2)
    assert min_max([4]) == (4, 4)


def test_min_max_returns_tuple():
    assert isinstance(min_max([1, 2]), tuple)


def test_distance():
    assert distance((1, 2), (4, 6)) == 7
    assert distance((4, 6), (1, 2)) == 7
    assert distance((0, 0), (0, 0)) == 0
    assert distance((-1, 3), (2, -1)) == 7


def test_squares():
    assert squares([1, 2, 3]) == [1, 4, 9]
    assert squares([-3]) == [9]
    assert squares([]) == []


def test_squares_does_not_change_input():
    numbers = [1, 2, 3]
    squares(numbers)
    assert numbers == [1, 2, 3]


def test_even_numbers():
    assert even_numbers([1, 2, 3, 4, 6]) == [2, 4, 6]
    assert even_numbers([0, -2, -3]) == [0, -2]
    assert even_numbers([1, 3]) == []


def test_shout_long_words():
    assert shout_long_words("the quick brown fox", 5) == ["QUICK", "BROWN"]
    assert shout_long_words("the quick brown fox", 3) == ["THE", "QUICK", "BROWN", "FOX"]
    assert shout_long_words("a  bb", 2) == ["BB"]
    assert shout_long_words("", 1) == []


def test_passed():
    assert passed([("ann", 7.5), ("bob", 5.4), ("cy", 5.5)]) == ["ann", "cy"]
    assert passed([("bob", 1.0)]) == []
    assert passed([]) == []


def test_word_lengths():
    assert word_lengths(["cat", "horse"]) == {"cat": 3, "horse": 5}
    assert word_lengths(["cat", "cat"]) == {"cat": 3}
    assert word_lengths([]) == {}


def test_first_letters():
    assert first_letters(["Banana", "apple", "berry"]) == ["a", "b"]
    assert first_letters(["Zoo", "Apple"]) == ["a", "z"]
    assert first_letters([]) == []


def test_flatten():
    assert flatten([[1, 2], [3], [], [4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten([]) == []
    assert flatten([[], []]) == []
