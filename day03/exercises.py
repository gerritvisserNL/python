"""Day 3 - Dictionaries and sets.

Same routine: replace `raise NotImplementedError` with your code.

    python -i day03/exercises.py     # try your code
    pytest day03 -v                  # run all tests
    pytest day03 -v -k word_count    # run one exercise

FOCUS POINTS FROM DAY 2
-----------------------
- Use `text.split()` without an argument. `split(" ")` breaks on double
  spaces: "a  b".split(" ") gives ['a', '', 'b'].
- Don't put the type in a name: `words`, not `word_list` or `text_array`.
- Looping over a string gives single characters, not words.
- Don't repeat a check that an earlier `if` already covers:
  after `if score < 5.5`, the `elif` already knows that score >= 5.5.

NEW TODAY
---------
A dictionary (dict) maps keys to values:

    ages = {"ann": 31, "bob": 25}
    ages["ann"]              # 31
    ages["cy"] = 40          # add or change a key
    "bob" in ages            # True    (checks the KEYS)
    ages.get("dan", 0)       # 0       value, or the default if the key is missing
    ages["dan"]              # KeyError: the key does not exist

    for name, age in ages.items():   # loop over key and value together
        print(name, age)

    dict(ages)               # a new dict with the same contents (a copy)
A dict keeps the order in which keys were added.

A set holds unique items, without order:

    letters = set("hello")   # {'h', 'e', 'l', 'o'}  duplicates disappear
    letters.add("x")
    {1, 2, 3} & {2, 3, 4}    # {2, 3}  items in both (intersection)
    sorted({3, 1, 2})        # [1, 2, 3]  sorted() always returns a new list
"""


# 1. Looking up a key ---------------------------------------------------------
def stock_level(stock, product):
    """Return how many of product are in stock. Missing products have 0.

    >>> stock_level({"apple": 3, "pear": 0}, "apple")
    3
    >>> stock_level({"apple": 3}, "banana")
    0

    Hint: one line is enough.
    """
    return stock.get(product, 0)


# 2. Building a dict ----------------------------------------------------------
def word_count(text):
    """Return a dict with how often each word appears in text.

    >>> word_count("the cat saw the dog")
    {'the': 2, 'cat': 1, 'saw': 1, 'dog': 1}
    >>> word_count("")
    {}

    Hint: start with an empty dict. Is the word new? Then its count starts at 1.
    """
    counts = {}

    for word in text.split():
        counts[word] = counts.get(word, 0) + 1

    return counts


# 3. Loop + lookup ------------------------------------------------------------
def total_cost(prices, cart):
    """Return the total price of all items in cart.

    cart is a list of product names; a product can appear more than once.
    Every product in cart exists in prices.

    >>> total_cost({"apple": 0.5, "bread": 2.0}, ["apple", "bread", "apple"])
    3.0
    """
    total = 0

    for item in cart:
        total += prices[item]

    return total


# 4. Looping over items() -----------------------------------------------------
def invert(mapping):
    """Return a new dict with keys and values swapped.

    All values are unique.

    >>> invert({"a": 1, "b": 2})
    {1: 'a', 2: 'b'}
    """

    inverted = {}

    for key, value in mapping.items():
        inverted[value] = key

    return inverted


# 5. No side effects ----------------------------------------------------------
def merge_scores(first, second):
    """Return a new dict with the scores of both dicts added together.

    Neither input dict may be changed.

    >>> merge_scores({"ann": 3, "bob": 1}, {"bob": 2, "cy": 5})
    {'ann': 3, 'bob': 3, 'cy': 5}

    Hint: start from a copy of first, then add the scores from second.
    """
    merged = dict(first)

    for name, score in second.items():
        merged[name] = merged.get(name, 0) + score

    return merged


# 6. A dict of lists ----------------------------------------------------------
def group_by_length(words):
    """Return a dict that maps each word length to the words of that length.

    Keep the words in their original order.

    >>> group_by_length(["cat", "horse", "dog"])
    {3: ['cat', 'dog'], 5: ['horse']}

    Hint: same pattern as word_count(), but the value is a list.
    """
    groups = {}

    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = [word]
        else:
            groups[length].append(word)

    return groups


# 7. Sets ---------------------------------------------------------------------
def unique_letters(text):
    """Return how many different letters text has.

    Ignore uppercase/lowercase and spaces.

    >>> unique_letters("Hello World")
    7
    """
    return len(set(text.lower().replace(" ", "")))


# 8. Set operations -----------------------------------------------------------
def common_items(first, second):
    """Return a sorted list of the items that appear in both lists.

    Every item appears only once in the result.

    >>> common_items([3, 1, 2, 3], [2, 3, 4])
    [2, 3]
    """

    return sorted(set(first) & set(second))


# 9. BONUS: reuse + tie -------------------------------------------------------
def most_common_word(text):
    """Return the word that appears most often in text.

    text always has at least one word. On a tie, return the word that appears
    FIRST in text. Do NOT use max().

    >>> most_common_word("the cat saw the dog")
    'the'
    >>> most_common_word("b a a b")
    'b'

    Hint: reuse word_count(). Then think about day 2's longest_word().
    """

    counts = word_count(text)

    best_count = 0
    best_word = ""

    for word, count in counts.items():
        if count > best_count:
            best_count = count
            best_word = word

    return best_word
