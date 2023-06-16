print("-----演習１-----")


def fizzbuzz(a, b):
    for i in range(a, b + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

fizzbuzz(1, 100)

print("-----演習２-----")
def fizzbuzz2(start=1, end=100):
    for i in range(start, end + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

fizzbuzz2()
fizzbuzz2(start=10, end=20)
