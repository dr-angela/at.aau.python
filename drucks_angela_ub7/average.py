def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)    # sorting elements
    n = len(sorted_numbers)     # n is needed for calculating median
    if n % 2 == 0:  # if list length is even
        middle_left = sorted_numbers[n // 2 - 1]
        middle_right = sorted_numbers[n // 2]
        return (middle_left + middle_right) / 2
    else:
        return sorted_numbers[n // 2]  # if list length is odd

def main(file_path):    # file_path is asked in main
    try:
        with open(file_path, 'r') as file:      # r is reading mode
            # file reading, creating substrings and iterating over them
            numbers = [int(num) for num in file.read().split()]
            average = calculate_average(numbers)
            median = calculate_median(numbers)
            print(f"Der Durchschnitt beträgt {average}.")
            print(f"Der Median beträgt {median}.")
    except FileNotFoundError:
        print("Die angegebene Datei wurde nicht gefunden.")


if __name__ == "__main__":
    file_path = input("Bitte geben Sie den Dateipfad ein: ")
    main(file_path)
