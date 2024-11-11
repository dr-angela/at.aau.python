def changeCoin(arr, total):
    if len(arr) == 0:  # case: empty array
        return -1
    if total <= 0:  # case: no coin used
        return 0
    if min(arr) > total:  # case: coin denominations too big
        return -1

    arr = sorted(arr, reverse=True)
    num = 0
    for i in arr:
        if total >= i:
            num += int(total / i)
            total = total % i
        if total == 0:
            return num
    return -1

if __name__ == "__main__":
    print(changeCoin([1, 2, 5, 10, 20, 50], 99))