# Task 2: Function count that takes a list of words and returns a list of tuples
# with words and their frequencies. The function uses a list comprehension.
# Duplicates are allowed.

def count(words):
    frequency = {word: words.count(word) for word in words}
    return [(word, frequency[word]) for word in words]


# Run def count

result = count("Wenn Fliegen hinter Fliegen fliegen fliegen Fliegen Fliegen nach".split())
print(result)

# The split() method is used to split the example text into individual words.
# The count function expects a list of words, not a single string.
# split() divides the string at whitespace and returns a list of words.