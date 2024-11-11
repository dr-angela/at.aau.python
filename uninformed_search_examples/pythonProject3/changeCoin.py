def changeCoin(arr, total):
    print("Input Array:", arr)
    print("Total amount:", total)

    if len(arr) == 0:
        # case: empty array
        print("Array is empty.")
        return -1

    if total <= 0:
        # case: no coin used
        print("No coin(s) used.")
        return 0

    if min(arr) > total:
        # case: coin denominations too big
        print("Coin denominations too big.")
        return -1

    # Sort the array in descending order
    arr = sorted(arr, reverse=True)
    print("Sorted Array (Descending):", arr)

    num = 0  # Number of coins used
    for i in arr:
        if total >= i:
            count = int(total / i)  # How many coins of this denomination can be used
            num += count
            total = total % i  # Remaining amount after using this denomination
            print(f"Using {count} coin(s) of {i}-cent denomination.")
            print("Remaining total after using coins:", total)

        if total == 0:
            print("Exact amount achieved. Total coins used:", num)
            return num

    # If exact amount cannot be achieved
    print("Cannot achieve exact amount with given denominations.")
    return -1


if __name__ == "__main__":
    print("Final result:", changeCoin([1, 2, 5, 10, 20, 50], 99))