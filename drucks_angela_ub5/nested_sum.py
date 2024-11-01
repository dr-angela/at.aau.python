# 5.5: Nested list, calculating  sum
def get_nested_sum(nested_list):
    total = 0
    # Iterating over all elements of given list
    for element in nested_list:
        # check if current element is a list, if true: recursive call for this element
        if isinstance(element, list):
            total += get_nested_sum(element)
        elif isinstance(element, int):  # if no list, just adding number to total
            total += element
    return total


# Beispiel
if __name__ == "__main__":
    nested_list_test = [1, [2, 3], [[4, 5], 6], 7]
    print(get_nested_sum(nested_list_test))