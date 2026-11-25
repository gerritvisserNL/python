from day03.exercises import (
    common_items,
    group_by_length,
    invert,
    merge_scores,
    most_common_word,
    stock_level,
    total_cost,
    unique_letters,
    word_count,
)


def test_stock_level():
    assert stock_level({"apple": 3, "pear": 0}, "apple") == 3
    assert stock_level({"apple": 3, "pear": 0}, "pear") == 0
    assert stock_level({"apple": 3}, "banana") == 0
    assert stock_level({}, "banana") == 0


def test_word_count():
    assert word_count("the cat saw the dog") == {"the": 2, "cat": 1, "saw": 1, "dog": 1}
    assert word_count("hi  hi") == {"hi": 2}
    assert word_count("") == {}


def test_total_cost():
    prices = {"apple": 0.5, "bread": 2.0}
    assert total_cost(prices, ["apple", "bread", "apple"]) == 3.0
    assert total_cost(prices, []) == 0


def test_invert():
    assert invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert invert({}) == {}


def test_merge_scores():
    assert merge_scores({"ann": 3, "bob": 1}, {"bob": 2, "cy": 5}) == {
        "ann": 3,
        "bob": 3,
        "cy": 5,
    }
    assert merge_scores({}, {"ann": 1}) == {"ann": 1}


def test_merge_scores_does_not_change_input():
    first = {"ann": 3, "bob": 1}
    second = {"bob": 2, "cy": 5}
    merge_scores(first, second)
    assert first == {"ann": 3, "bob": 1}
    assert second == {"bob": 2, "cy": 5}


def test_group_by_length():
    assert group_by_length(["cat", "horse", "dog"]) == {3: ["cat", "dog"], 5: ["horse"]}
    assert group_by_length(["cat", "dog", "cat"]) == {3: ["cat", "dog", "cat"]}
    assert group_by_length([]) == {}


def test_unique_letters():
    assert unique_letters("Hello World") == 7
    assert unique_letters("aA a") == 1
    assert unique_letters("") == 0


def test_common_items():
    assert common_items([3, 1, 2, 3], [2, 3, 4]) == [2, 3]
    assert common_items([5, 4], [4, 5]) == [4, 5]
    assert common_items([1, 2], [3, 4]) == []


def test_most_common_word():
    assert most_common_word("the cat saw the dog") == "the"
    assert most_common_word("b a a b") == "b"
    assert most_common_word("hello") == "hello"
