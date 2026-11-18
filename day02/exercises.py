"""Day 2 - Strings and lists: indexing, slicing and methods.

Same routine as day 1: replace `raise NotImplementedError` with your code.

    python -i day02/exercises.py     # try your code
    pytest day02 -v                  # run all tests
    pytest day02 -v -k initials      # run one exercise

FOCUS POINTS FROM DAY 1
-----------------------
- Never change the input you receive (no side effects). Build something new.
- Translate boundaries literally: "up to and including 20" is `<= 20`.
- Use descriptive names: `for letter in text`, not `for x in text`.

NEW TODAY
---------
Strings and lists both have positions (indexes), starting at 0:

    word = "python"
    word[0]       # 'p'       first item
    word[-1]      # 'n'       last item
    word[1:4]     # 'yth'     slice: from index 1 up to (NOT including) 4
    word[:2]      # 'py'      from the start
    word[2:]      # 'thon'    to the end
    word[::-1]    # 'nohtyp'  step -1: backwards

Useful methods:

    "a b c".split()          # ['a', 'b', 'c']     text -> list of words
    "-".join(["a", "b"])     # 'a-b'               list of strings -> text
    "hi".upper()             # 'HI'
    "a b".replace(" ", "")   # 'ab'
    len("hello")             # 5   (works on lists too)
"""


# 1. Indexing -----------------------------------------------------------------
def initials(full_name):
    """Return the initials of a name in uppercase, each followed by a dot.

    >>> initials("Ada Lovelace")
    'A.L.'
    >>> initials("guido van rossum")
    'G.V.R.'

    Hint: split the name into words, take the first letter of each word.
    """
    initials = []

    full_name = full_name.split()

    for word in full_name:
        initial_plus_dot = word[0].upper() + "."
        initials.append(initial_plus_dot)
    return "".join(initials)


# 2. Slicing ------------------------------------------------------------------
def reverse_text(text):
    """Return text backwards. Use slicing, not a loop.

    >>> reverse_text("hello")
    'olleh'
    """
    return text[::-1]


# 3. Combining methods --------------------------------------------------------
def is_palindrome(text):
    """Return True if text reads the same forwards and backwards.

    Ignore uppercase/lowercase and spaces.

    >>> is_palindrome("Racecar")
    True
    >>> is_palindrome("Never odd or even")
    True
    >>> is_palindrome("hello")
    False

    Hint: first clean the text, then you can reuse reverse_text().
    """
    text_modified = text.lower().replace(" ", "")

    text_reverted = reverse_text(text_modified)

    return text_modified == text_reverted


# 4. Slicing with a boundary --------------------------------------------------
def last_items(items, n):
    """Return a new list with the last n items.

    n is never negative. If n is larger than the list, return the whole list.

    >>> last_items([1, 2, 3, 4], 2)
    [3, 4]
    >>> last_items([1, 2, 3, 4], 0)
    []

    Watch out: test n = 0 yourself in `python -i`. Is the result what you expect?
    """

    if n == 0:
        return []
    return items[-n:]


# 5. No side effects ----------------------------------------------------------
def without_duplicates(items):
    """Return a new list without duplicates, keeping the original order.

    The list you receive must NOT be changed.

    >>> without_duplicates([3, 1, 3, 2, 1])
    [3, 1, 2]

    Hint: build a new list and use `not in` to check what you already have.
    """
    new_list = []

    for item in items:
        if item not in new_list:
            new_list.append(item)
    return new_list


# 6. split and join -----------------------------------------------------------
def capitalize_words(text):
    """Return text with the first letter of every word in uppercase.

    The rest of each word stays as it was. Do NOT use .title() or .capitalize().

    >>> capitalize_words("hello big world")
    'Hello Big World'
    >>> capitalize_words("learn python")
    'Learn Python'

    Hint: word[0] is the first letter, word[1:] is the rest.
    """
    text = text.split()

    text_uppercase_words = []

    for word in text:
        uppercase_word = word[0].upper() + word[1:]
        text_uppercase_words.append(uppercase_word)

    return " ".join(text_uppercase_words)


# 7. Boundaries ---------------------------------------------------------------
def grade_label(score):
    """Return a label for a school grade between 1.0 and 10.0.

    - below 5.5                              -> "fail"
    - 5.5 up to 8.0   (5.5 included, 8.0 not) -> "pass"
    - 8.0 and higher                         -> "excellent"

    >>> grade_label(6.0)
    'pass'
    """
    if score < 5.5:
        return "fail"
    elif score < 8.0:
        return "pass"
    else:
        return "excellent"


# 8. Loop + compare -----------------------------------------------------------
def longest_word(text):
    """Return the longest word in text. text always has at least one word.

    If several words are equally long, return the FIRST one.
    Do NOT use max() here.

    >>> longest_word("I love Python a lot")
    'Python'
    >>> longest_word("cat dog")
    'cat'

    Hint: think about day 1's largest(). Which comparison keeps the first word
    on a tie: > or >= ?
    """

    long_word = ""

    for word in text.split():
        if len(word) > len(long_word):
            long_word = word
    return long_word


# 9. BONUS: slicing in a loop -------------------------------------------------
def chunk(items, size):
    """Split items into lists of `size` items. The last chunk may be smaller.

    size is always at least 1.

    >>> chunk([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]

    Hint: range(start, stop, step) can count in steps: range(0, 5, 2) gives
    0, 2, 4. Each of those is the start of a slice.
    """
    chunks = []

    for start in range(0, len(items), size):
        chunks.append(items[start : start + size])
    return chunks
