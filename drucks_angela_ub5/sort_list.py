# 5.1: Sorting algorithm
def sort_inplace(some_list):
    # Algorithm starts: iterating over every element in given list (1st loop)
    for i in range(len(some_list)):
        # help variable, for remembering index of last element
        min_index = i
        # Iterating over indices j in list to find the smallest number (2nd loop)
        for j in range(i + 1, len(some_list)):  # +1 because we need the n+1 for comparing
            # Check every element if it is smaller than the one at min_index
            if some_list[j] < some_list[min_index]:
                # If true, update min_index to index of the smaller element
                min_index = j
        # Swap numbers (no triangle-swap needed in python)
        some_list[i], some_list[min_index] = some_list[min_index], some_list[i]
        # print(some_list)


if __name__ == '__main__':
    my_list = [5, 3, 1, 4, 8, 2, 7, 6]

    sort_inplace(my_list)
    print(my_list)