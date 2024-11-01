def word_length(words):
    result = []
    for word in words:
        word_len_pair = (word, len(word))
        result.append(word_len_pair)
    return result   # hier soll die List Comprehension stehen

# Task 1: Convert def word_length into word_length_comp -> one-liner

def word_length_comp(words):
    return [(word, len(word)) for word in words]


# Run both functions only if this script is executed directly
if __name__ == "__main__":
    words = ['apple', 'banana', 'cherry', 'strawberry', 'raspberry', 'pizza', 'donut']
    result_imperative = word_length(words)
    result_comp = word_length_comp(words)

    print(result_imperative)
    print(result_comp)
