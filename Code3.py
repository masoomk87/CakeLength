def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")
