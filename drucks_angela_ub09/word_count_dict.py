# Task 3: Function count_dict that takes a list of words and returns a dictionary
# with words as keys and their frequencies as values. The function uses a dict comprehension.

# List: An ordered collection of elements that can contain duplicates.
# Set: An unordered collection of unique elements. A set does not allow duplicates.
# Dictionary (Dict): An unordered collection of key-value pairs where each key is unique.

def count_dict(words):
    # Use a dict comprehension to create a dictionary with word counts
    # The set(words) ensures each word is counted only once as a key in the dictionary
    return {word: words.count(word) for word in set(words)}


# Run Task 3
result = count_dict("Wenn Fliegen hinter Fliegen fliegen fliegen Fliegen Fliegen nach".split())
print(result)
