def fizz_buzz(n, i=1):
    if i == n:
        return

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBazz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Bazz")

    print(i)
    fizz_buzz(n, i + 1)


fizz_buzz(17)
