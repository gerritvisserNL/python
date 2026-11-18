from day01.exercises import (
    count_vowels,
    describe_temperature,
    fizzbuzz,
    greet,
    is_even,
    largest,
    only_positive,
    rectangle_area,
    sum_numbers,
)


def test_greet():
    assert greet("Ann") == "Hello, Ann!"
    assert greet("Bob") == "Hello, Bob!"


def test_rectangle_area():
    assert rectangle_area(3, 4) == 12
    assert rectangle_area(5, 1) == 5


def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(0) is True


def test_describe_temperature():
    assert describe_temperature(5) == "cold"
    assert describe_temperature(10) == "mild"
    assert describe_temperature(15) == "mild"
    assert describe_temperature(20) == "mild"
    assert describe_temperature(25) == "warm"


def test_sum_numbers():
    assert sum_numbers([1, 2, 3]) == 6
    assert sum_numbers([]) == 0
    assert sum_numbers([-1, 1]) == 0


def test_count_vowels():
    assert count_vowels("Hello World") == 3
    assert count_vowels("AEIOU") == 5
    assert count_vowels("xyz") == 0


def test_largest():
    assert largest([3, 8, 2]) == 8
    assert largest([-5, -2, -9]) == -2
    assert largest([7]) == 7


def test_only_positive():
    assert only_positive([3, -1, 0, 5]) == [3, 5]
    assert only_positive([-1, -2]) == []


def test_fizzbuzz():
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizzbuzz(15)[-1] == "FizzBuzz"
