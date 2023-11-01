from functools import reduce

factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1)) if n else 1

num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")
