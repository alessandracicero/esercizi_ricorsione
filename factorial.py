def factorial(n):
    #condizione terminale
    if n == 0 or n ==1:
        return 1
    #condizione non terminale, ricorsiva
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    N = 6

    print(factorial(N))