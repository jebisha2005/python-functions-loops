# 1. For Loop,Print numbers from 1 to 10 using a for loop.Concepts: for, range()
for i in range(1, 11):
    print(i)

# 2. While Loop,Print numbers from 1 to 10 using a while loop.Concepts: while
i = 1
while i <= 10:
    print(i)
    i += 1  

# 3. Multiplication Table,Take a number as input and print its multiplication table up to 10.
num=int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    
# 4. Sum of Numbers,Find the sum of numbers from 1 to 100.Concepts: Loop, accumulator
total = 0
for i in range(1, 101):
    total += i
print(f"The sum of numbers from 1 to 100 is: {total}")

# 5. Even and Odd NumbersPrint:Even numbers from 1 to 50,Odd numbers from 1 to 50 Concepts: Conditions inside loops

print("Even numbers from 1 to 50:")
for i in range(1, 51):
    if i % 2 == 0:
        print(f"Even number: {i}")
    if i % 2 != 0:
        print(f"Odd number: {i}")

# 6. Break and Continue,Print numbers from 1 to 20.Skip number 10 using continue,Stop the loop when the number reaches 18 using break
# Concepts: break, continue
for i in range(1, 21):
    if i == 10:
        continue
    if i == 18:
        break
    print(i)

# 7. Nested Loops:Print the following pattern:

# *
# * *
# * * *
# * * * *
# * * * * *

# Concepts: Nested loops
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# 8. Loop Through Collections

# Create:A list,A tuple,A set,A dictionary,Use loops to print all their elements.Concepts: Looping through different data structures
my_list = [1, 2, 3, 4, 5]
my_tuple = (6, 7, 8, 9, 10)
my_set = {11, 12, 13, 14, 15}
my_dict = {"a": 1, "b": 2, "c": 3}

print("Elements in the list:")
for item in my_list:
    print(item)

print("Elements in the tuple:")
for item in my_tuple:
    print(item)

print("Elements in the set:")
for item in my_set:
    print(item)

print("Elements in the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 9. Number Guessing Game,Store a secret number.Ask the user to guess until they enter the correct number.Print:Correct!
# Concepts: while loop, user input

secret_number = 7
guess = None
while guess != secret_number:
    guess = int(input("Guess the secret number: "))
    if guess == secret_number:
        print("Correct!")
    else:
        print("Try again.")