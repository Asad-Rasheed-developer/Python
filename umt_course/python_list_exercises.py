
# Exercise 3-1: Names
names = ['Alice', 'Bob', 'Charlie']
for name in names:
    print(name)

# Exercise 3-2: Greetings
names = ['Alice', 'Bob', 'Charlie']
for name in names:
    print(f"Hello, {name}! How are you?")

# Exercise 3-3: Your Own List
transportations = ['Honda motorcycle', 'Tesla car', 'Boeing airplane']
for transportation in transportations:
    print(f"I would like to own a {transportation}.")

# Exercise 3-4: Guest List
guests = ['Albert Einstein', 'Marie Curie', 'Isaac Newton']
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner!")

# Exercise 3-5: Changing Guest List
guests = ['Albert Einstein', 'Marie Curie', 'Isaac Newton']
print(f"Unfortunately, {guests[1]} can't make it.")
guests[1] = 'Galileo Galilei'
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner!")

# Exercise 3-6: More Guests
guests = ['Albert Einstein', 'Galileo Galilei', 'Isaac Newton']
print("Good news! We found a bigger table.")
guests.insert(0, 'Leonardo da Vinci')
guests.insert(2, 'Nikola Tesla')
guests.append('Aristotle')
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner!")

# Exercise 3-7: Shrinking Guest List
guests = ['Leonardo da Vinci', 'Albert Einstein', 'Nikola Tesla', 'Galileo Galilei', 'Isaac Newton', 'Aristotle']
print("Unfortunately, I can only invite two people for dinner.")
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")
for guest in guests:
    print(f"{guest}, you're still invited to dinner.")
del guests[0]
del guests[0]
print(f"Final guest list: {guests}")  # Should be an empty list

# Exercise 3-8: Seeing the World
places = ['Tokyo', 'New York', 'Paris', 'Istanbul', 'Sydney']
print("Original order:", places)
print("Alphabetical order:", sorted(places))
print("Original order after sorted():", places)
print("Reverse alphabetical order:", sorted(places, reverse=True))
print("Original order after reverse sorted():", places)
places.reverse()
print("Order after reverse():", places)
places.reverse()
print("Order after second reverse():", places)
places.sort()
print("Order after sort():", places)
places.sort(reverse=True)
print("Order after sort(reverse=True):", places)

# Exercise 3-9: Every Function
languages = ['Python', 'Java', 'C++', 'Ruby', 'JavaScript']
print("Original list:", languages)
languages.append('Go')
print("After append():", languages)
languages.insert(2, 'Swift')
print("After insert(2, 'Swift'):", languages)
languages.remove('Ruby')
print("After remove('Ruby'):", languages)
popped_language = languages.pop()
print(f"After pop(): {languages}, Popped: {popped_language}")
languages.sort()
print("After sort():", languages)
languages.reverse()
print("After reverse():", languages)

# Exercise 3-10: Intentional Error
languages = ['Python', 'Java', 'C++']
# Intentional error by accessing an out-of-range index
# print(languages[3])  # Uncommenting this line will cause an IndexError
# Correcting the error
print(languages[-1])  # Accessing the last element correctly
