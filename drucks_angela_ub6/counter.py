from collections import Counter


# 1.1. Dictionary
def count_elements_dict(list):
    counts = Counter(list)  # Count the number of items in the list; Counter is a python collection module
    return dict(counts)  # dict function -> creates a dictionary


# 1.1. Another solution
def count_elements(list):
    counts = {}
    for element in list:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts

# 1.2. Tuple, lambda arguments : expression, (Element, Häufigkeit), [0]: Element, [1]: Häufigkeit
def count_elements_tuple(list):
    counts = Counter(list)
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts

# 1.2. Tuple, using function from 1.1.
def count_elements_tuple2(list):
    counts_dict = count_elements_dict(list)
    sorted_counts = sorted(counts_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts


myList = ['a', 'b', 'b', 'a', 'c', 'a', 'b', 'b']
result1 = count_elements_dict(myList)  # 1.1
result2 = count_elements(myList)  # 1.1
result3 = count_elements_tuple(myList)  # 1.2
result4 = count_elements_tuple2(myList)  # 1.2
print(result1)
print(result2)
print(result3)
print(result4)
