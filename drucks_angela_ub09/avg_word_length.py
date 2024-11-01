# Task 4:

# Import the word_length_comp function from the previous task
from word_length import word_length_comp

# Import the mean function from the statistics module
from statistics import mean

def avg_word_length(words):
    # Get the word lengths using the imported function
    word_lengths = word_length_comp(words)
    # Use a list comprehension to extract the lengths
    lengths = [length for word, length in word_lengths]
    # Calculate and return the mean of the lengths
    return mean(lengths)


# Example text to test the function
example_text = "Wenn Fliegen hinter Fliegen fliegen fliegen Fliegen Fliegen nach".split()
average_length = avg_word_length(example_text)

# Output the average word length
print(f"{average_length:.3f}")