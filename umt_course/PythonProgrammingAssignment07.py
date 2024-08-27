import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


name = input("Hello! What's your name? ")


print(f"Nice to meet you, {name}! Please tell me three of your favorite numbers.")
numbers = []

for i in range(1, 4):
    while True:
        try:
          
            num = int(input(f"Enter number {i}: ").strip())
            numbers.append(num)
            break
        except ValueError:
            print("That doesn't seem to be a valid number. Please try again.")


even_odd = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]


print(f"\nThank you, {name}! Let's explore your favorite numbers together.")


print("\nHere's whether each of your favorite numbers is even or odd:")
for num, eo in even_odd:
    print(f"{num} is {eo}.")


print("\nLet's see what happens when we square each of your favorite numbers:")
squares = [(num, num ** 2) for num in numbers]
for num, square in squares:
    print(f"The square of {num} is {square}.")


sum_numbers = sum(numbers)
print(f"\nThe sum of your favorite numbers is: {sum_numbers}")

print(f"Great job, {name}! {sum_numbers} is a fascinating number!")


if is_prime(sum_numbers):
    print(f"Wow! Did you know that {sum_numbers} is a prime number? That's pretty cool!")
else:
    print(f"By the way, {sum_numbers} is not a prime number, but it's still interesting!")


print(f"\nThanks for exploring numbers with me, {name}! Have a wonderful day!")

