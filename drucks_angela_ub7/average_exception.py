def average(lst):
    numbers = [x for x in lst if isinstance(x, int)]  # Consider only numbers
    return sum(numbers) / len(numbers) if numbers else 0    # if numbers is not null, ternäre Auswertung

def median(lst):
    numbers = [x for x in lst if isinstance(x, int)]  # Consider only numbers
    sorted_lst = sorted(numbers)
    n = len(sorted_lst)
    if n % 2 == 0:
        return (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2 if n > 0 else 0
    else:
        return sorted_lst[n//2] if n > 0 else 0

def calculate_average_and_median(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = []

            for element in file.read().split():
                try:
                    number = int(element)   # converting into ganzzahl
                    numbers.append(number)  # move element into numbers[]
                except ValueError:
                    pass    # if error, move on with loop

        average_value = average(numbers)
        median_value = median(numbers)

        print(f"The average is {average_value}.")
        print(f"The median is {median_value}.")

    except FileNotFoundError:
        print("The file was not found.")


file_path = input("Please enter the file path: ")
calculate_average_and_median(file_path)
