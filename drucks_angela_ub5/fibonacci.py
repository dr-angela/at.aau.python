# 5.3: Iterative calculation of fibonacci numbers
def fib_it(number):
    if number <= 1:
        return number
    # else part (no explicit else keyword necessary)
    a, b = 0, 1
    for _ in range(2, number + 1):  # (start, stop)
        a, b = b, a + b
    return b


# 5.4: Recursive calculation of fibonacci numbers
def fib_rec(number):
    if number <= 1:
        return number
    else:   # recursive: (n-1)+(n-2)
        return fib_rec(number - 1) + fib_rec(number - 2)


if __name__ == '__main__':
    n = 10
    # iterative print
    print(f"Die {n}. Fibonacci-Zahl iterativ berechnet lautet: {fib_it(n)}")
    # recursive print
    print(f"Die {n}. Fibonacci-Zahl rekursiv berechnet lautet: {fib_rec(n)}")