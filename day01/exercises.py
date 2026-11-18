"""Day 1 - Back to basics: functions, if/else and loops.

HOW THIS WORKS
--------------
Each exercise is a function. The first line (`def ...`) is already written.
Replace `raise NotImplementedError` with your own code.

A function receives input (parameters) and gives back a result with `return`:

    def double(number):
        return number * 2

    double(4)   # gives back 8

Note: `return` gives a value back; `print` only shows it on screen.
The tests check what you *return*, so always use `return`.

TRY YOUR CODE
-------------
    python -i day01/exercises.py     # loads this file, then lets you type:
    >>> greet("Ann")
    'Hello, Ann!'
    >>> exit()

RUN THE TESTS
-------------
    pytest day01 -v                  # all exercises
    pytest day01 -v -k greet         # only one exercise

Don't change the function names: the tests depend on them.
"""


# 1. Strings ------------------------------------------------------------------
def greet(name):
    """Return a greeting for name.

    >>> greet("Ann")
    'Hello, Ann!'

    Hint: an f-string puts a variable inside text: f"Hi {name}"
    """
    return f"Hello, {name}!"


# 2. Arithmetic ---------------------------------------------------------------
def rectangle_area(width, height):
    """Return the area of a rectangle.

    >>> rectangle_area(3, 4)
    12
    """
    return width * height


# 3. Booleans -----------------------------------------------------------------
def is_even(number):
    """Return True if number is even, otherwise False.

    >>> is_even(4)
    True
    >>> is_even(7)
    False

    Hint: the % operator gives the remainder of a division: 7 % 2 == 1
    """
    return number % 2 == 0


# 4. if / elif / else ---------------------------------------------------------
def describe_temperature(celsius):
    """Describe the temperature in one word.

    - below 10        -> "cold"
    - 10 up to 20     -> "mild"   (10 and 20 included)
    - above 20        -> "warm"

    >>> describe_temperature(15)
    'mild'

    Hint:
        if condition:
            ...
        elif other_condition:
            ...
        else:
            ...
    """
    if celsius < 10:
        return "cold"
    elif celsius <= 20:
        return "mild"
    else:
        return "warm"


# 5. for loop -----------------------------------------------------------------
def sum_numbers(numbers):
    """Return the sum of all numbers in the list.

    Do NOT use the built-in sum() here: practice the loop.

    >>> sum_numbers([1, 2, 3])
    6

    Hint: start with total = 0, then loop:
        for number in numbers:
            ...
    """
    total = 0

    for number in numbers:
        total += number
    return total


# 6. Looping over a string ----------------------------------------------------
def count_vowels(text):
    """Return how many vowels (a, e, i, o, u) are in text.

    Uppercase vowels count too.

    >>> count_vowels("Hello World")
    3

    Hint: `"e" in "aeiou"` is True. And "A".lower() gives "a".
    """
    vowels = "aeiou"
    count = 0

    for letter in text.lower():
        if letter in vowels:
            count += 1
    return count


# 7. Loop + if combined -------------------------------------------------------
def largest(numbers):
    """Return the largest number in the list. The list is never empty.

    Do NOT use the built-in max() here.

    >>> largest([3, 8, 2])
    8

    Hint: assume the first number (numbers[0]) is the largest,
    then check every number and update when you find a bigger one.
    """

    biggest = numbers[0]
    for number in numbers:
        if number > biggest:
            biggest = number
    return biggest


# 8. Building a list ----------------------------------------------------------
def only_positive(numbers):
    """Return a new list with only the numbers greater than 0.

    >>> only_positive([3, -1, 0, 5])
    [3, 5]

    Hint: start with an empty list result = [] and use result.append(...)
    """
    result = []

    for number in numbers:
        if number > 0:
            result.append(number)
    return result


# 9. BONUS: everything together -----------------------------------------------
def fizzbuzz(n):
    """Return a list with the FizzBuzz sequence from 1 up to and including n.

    - multiples of 3 become "Fizz"
    - multiples of 5 become "Buzz"
    - multiples of both 3 and 5 become "FizzBuzz"
    - all other numbers become the number as a string, e.g. "4"

    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']

    Hint: range(1, n + 1) gives 1, 2, ..., n. str(4) gives "4".
    Think about which check has to come first.
    """
    result = []
    for x in range(1, n + 1):
        if x % 15 == 0:
            result.append("FizzBuzz")
        elif x % 5 == 0:
            result.append("Buzz")
        elif x % 3 == 0:
            result.append("Fizz")
        else:
            result.append(str(x))

    return result
