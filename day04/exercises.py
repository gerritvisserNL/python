"""Day 4 - Tuples and comprehensions.

Same routine: replace `raise NotImplementedError` with your code.

    python -i day04/exercises.py     # try your code
    pytest day04 -v                  # run all tests
    pytest day04 -v -k squares       # run one exercise

FOCUS POINTS FROM DAY 3
-----------------------
- Use what you just learned. Counting is `counts.get(word, 0) + 1`, a copy
  is `dict(first)`, "in both lists" is `set(first) & set(second)`.
- Name things after their content, not their type: `counts`, not `new_dict`.
  Loop with `for word, count in counts.items()`, not `for key, value`.
- Don't build an in-between structure you don't need. In group_by_length the
  extra dict used words as keys, so a word that appeared twice got lost.
- Don't add a special case the general code already handles:
  "".split() is [], so the loop simply does nothing.

NEW TODAY
---------
A tuple is like a list, but it can't be changed. Use it for a fixed group
of values that belong together:

    point = (3, 4)
    point[0]                 # 3
    x, y = point             # unpacking: x is 3, y is 4
    return low, high         # a function can return a tuple

A comprehension builds a new list in one line:

    [n * 2 for n in numbers]               # transform every item
    [n for n in numbers if n > 0]          # keep only some items
    [name for name, age in people]         # unpack tuples while looping

The same idea works for dicts and sets:

    {word: len(word) for word in words}    # dict comprehension
    {word[0] for word in words}            # set comprehension

Read it like a sentence: "n times 2, for every n in numbers".
"""


# 1. Returning a tuple --------------------------------------------------------
def min_max(numbers):
    """Return a tuple with the lowest and the highest number.

    numbers always has at least one number. You may use min() and max().

    >>> min_max([3, 1, 4, 1, 5])
    (1, 5)
    """
    raise NotImplementedError


# 2. Unpacking ----------------------------------------------------------------
def distance(start, end):
    """Return the number of steps between two (x, y) points on a grid.

    You can only move horizontally or vertically, so the distance is the
    difference in x plus the difference in y.

    >>> distance((1, 2), (4, 6))
    7
    >>> distance((4, 6), (1, 2))
    7

    Hint: unpack both points first. abs(-3) is 3.
    """
    raise NotImplementedError


# 3. List comprehension -------------------------------------------------------
def squares(numbers):
    """Return a new list with every number squared.

    Use a comprehension, not a for loop with append().

    >>> squares([1, 2, 3])
    [1, 4, 9]
    """
    raise NotImplementedError


# 4. Comprehension with if ----------------------------------------------------
def even_numbers(numbers):
    """Return a new list with only the even numbers, in their original order.

    >>> even_numbers([1, 2, 3, 4, 6])
    [2, 4, 6]

    Hint: a number is even if dividing by 2 leaves nothing: n % 2 == 0.
    """
    raise NotImplementedError


# 5. Transform + filter -------------------------------------------------------
def shout_long_words(text, min_length):
    """Return the words of text with at least min_length letters, in uppercase.

    >>> shout_long_words("the quick brown fox", 5)
    ['QUICK', 'BROWN']
    """
    raise NotImplementedError


# 6. Unpacking in a comprehension ---------------------------------------------
def passed(students):
    """Return the names of the students with a grade of 5.5 or higher.

    students is a list of (name, grade) tuples.

    >>> passed([("ann", 7.5), ("bob", 5.4), ("cy", 5.5)])
    ['ann', 'cy']
    """
    raise NotImplementedError


# 7. Dict comprehension -------------------------------------------------------
def word_lengths(words):
    """Return a dict that maps every word to its length.

    >>> word_lengths(["cat", "horse"])
    {'cat': 3, 'horse': 5}
    """
    raise NotImplementedError


# 8. Set comprehension --------------------------------------------------------
def first_letters(words):
    """Return a sorted list of the different first letters of the words.

    Ignore uppercase/lowercase. Every word has at least one letter.

    >>> first_letters(["Banana", "apple", "berry"])
    ['a', 'b']
    """
    raise NotImplementedError


# 9. BONUS: a comprehension with two loops ------------------------------------
def flatten(rows):
    """Return one list with all items of all rows, in order.

    >>> flatten([[1, 2], [3], [], [4, 5]])
    [1, 2, 3, 4, 5]

    Hint: write it as two nested for loops first. A comprehension uses the
    for parts in the same order: [item for row in rows for item in row].
    Then explain to yourself why that order is right.
    """
    raise NotImplementedError
