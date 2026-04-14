# ============================================================
# 9. LOOPS
# ============================================================
# A loop lets you repeat code multiple times without writing it over and over.

import time

# ------------------------------------------------------------
# WHILE LOOPS
# ------------------------------------------------------------
print("=== While Loops ===")

# Count from 1 to 5
count = 1

while count <= 5:
    print(f"Count: {count}")
    count = count + 1  # Same as: count += 1

print("Done counting!")

# Common while loop patterns

# Pattern 1: Count up
print("\n--- Count up ---")
i = 0
while i < 5:
    print(i, end=" ")
    i += 1
print()

# Pattern 2: Count down
print("\n--- Countdown ---")
countdown = 5
while countdown > 0:
    print(countdown, end=" ")
    countdown -= 1
print("Liftoff!")

# Pattern 3: Processing until condition met
print("\n--- Sum until >= 10 ---")
total = 0
numbers = [2, 3, 4, 5]
index = 0
while total < 10 and index < len(numbers):
    total += numbers[index]
    print(f"Added {numbers[index]}, total = {total}")
    index += 1

# ------------------------------------------------------------
# INFINITE LOOPS (with break)
# ------------------------------------------------------------
print("\n=== Infinite Loops with Break ===")

# This runs forever until break
counter = 0
while True:
    counter += 1
    print(f"Loop iteration: {counter}")
    if counter >= 3:
        print("Breaking out!")
        break  # Exit the loop

# ⚠️ Be careful! This would run forever:
# while True:
#     print("Help!")  # Will print forever!

# ------------------------------------------------------------
# FOR LOOPS
# ------------------------------------------------------------
print("\n=== For Loops ===")

# Loop through a list
fruits = ["apple", "banana", "cherry"]

print("Fruits:")
for fruit in fruits:
    print(f"  {fruit}")

# Loop through a string (character by character)
print("\nCharacters in 'Hello':")
for letter in "Hello":
    print(f"  {letter}")

# Loop through a dictionary
person = {"name": "Alice", "age": 25}
print("\nPerson info:")
for key in person:
    print(f"  {key}: {person[key]}")

# Better way for dictionaries:
print("\nPerson info (better way):")
for key, value in person.items():
    print(f"  {key}: {value}")

# ------------------------------------------------------------
# RANGE FUNCTION
# ------------------------------------------------------------
print("\n=== Range Function ===")

# range(stop) - 0 to stop-1
print("range(5):", end=" ")
for i in range(5):       # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

# range(start, stop) - start to stop-1
print("range(2, 6):", end=" ")
for i in range(2, 6):    # 2, 3, 4, 5
    print(i, end=" ")
print()

# range(start, stop, step) - with step
print("range(0, 10, 2):", end=" ")
for i in range(0, 10, 2):    # 0, 2, 4, 6, 8
    print(i, end=" ")
print()

# Count backwards
print("range(5, 0, -1):", end=" ")
for i in range(5, 0, -1):    # 5, 4, 3, 2, 1
    print(i, end=" ")
print()

# Repeat something n times
print("\nRepeat 3 times:")
for _ in range(3):    # Use _ when you don't need the variable
    print("  Hello!")

# ------------------------------------------------------------
# ENUMERATE
# ------------------------------------------------------------
print("\n=== Enumerate ===")

fruits = ["apple", "banana", "cherry"]

# With enumerate - get both index AND value
print("With enumerate():")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# Start counting from 1
print("\nStarting from 1:")
for num, fruit in enumerate(fruits, start=1):
    print(f"  {num}. {fruit}")

# ------------------------------------------------------------
# ZIP
# ------------------------------------------------------------
print("\n=== Zip ===")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Loop through multiple lists together
print("Names and ages:")
for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")

# Zip with three lists
scores = [85, 90, 78]
print("\nFull info:")
for name, age, score in zip(names, ages, scores):
    print(f"  {name}, {age}, scored {score}")

# ------------------------------------------------------------
# BREAK AND CONTINUE
# ------------------------------------------------------------
print("\n=== Break and Continue ===")

# break - EXIT the loop immediately
print("Using break:")
for i in range(10):
    if i == 5:
        break  # Stop the loop completely
    print(i, end=" ")
print("(stopped at 5)")

# continue - SKIP to next iteration
print("\nUsing continue (skip 2):")
for i in range(5):
    if i == 2:
        continue  # Skip this iteration
    print(i, end=" ")
print()

# Practical example: Find first negative number
print("\nFind first negative:")
numbers = [1, 5, -3, 2, -8, 10]
for num in numbers:
    if num < 0:
        print(f"  Found negative: {num}")
        break

# Practical example: Sum only positive numbers
print("\nSum positive numbers:")
numbers = [1, -2, 3, -4, 5]
total = 0
for num in numbers:
    if num < 0:
        continue  # Skip negatives
    total += num
print(f"  Sum of positives: {total}")

# ------------------------------------------------------------
# ELSE CLAUSE IN LOOPS
# ------------------------------------------------------------
print("\n=== Else Clause in Loops ===")

# The else block runs ONLY if the loop completes normally (no break)
print("Loop without break:")
for i in range(3):
    print(i, end=" ")
else:
    print("- Loop finished normally!")

# If break is used, else doesn't run
print("\nLoop with break:")
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
else:
    print("- This won't print!")
print("(else didn't run)")

# Practical use: Search pattern
print("\nSearch for 4 in [1, 3, 5, 7, 9]:")
numbers = [1, 3, 5, 7, 9]
target = 4
for num in numbers:
    if num == target:
        print(f"  Found {target}!")
        break
else:
    print(f"  {target} not found in list")

# ------------------------------------------------------------
# NESTED LOOPS
# ------------------------------------------------------------
print("\n=== Nested Loops ===")

# Multiplication table
print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} × {j} = {i * j}")
    print("  ---")

# Grid/matrix example
print("\nGrid pattern:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for cell in row:
        print(cell, end=" ")
    print()  # New line after each row

# ------------------------------------------------------------
# PRACTICE EXERCISES
# ------------------------------------------------------------
print("\n=== Practice Exercises ===")

# Exercise 1: Print numbers 1-10
print("Exercise 1 - Numbers 1-10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# Exercise 2: Calculate sum of 1-100
total = 0
for i in range(1, 101):
    total += i
print(f"\nExercise 2 - Sum of 1-100: {total}")

# Exercise 3: Print even numbers 0-20
print("\nExercise 3 - Even numbers 0-20:")
for i in range(0, 21, 2):
    print(i, end=" ")
print()

# Exercise 4: Find first number divisible by 7
print("\nExercise 4 - First divisible by 7:")
for num in range(1, 100):
    if num % 7 == 0:
        print(f"  First divisible by 7: {num}")
        break

# Exercise 5: Countdown timer (fast version)
print("\nExercise 5 - Fast countdown:")
for i in range(5, 0, -1):
    print(i, end=" ")
    # time.sleep(0.1)  # Uncomment for real delay
print("Liftoff!")

# Exercise 6: Nested loop - print a triangle
print("\nExercise 6 - Triangle:")
for i in range(1, 6):
    print("*" * i)

# Exercise 7: Password attempt simulation
print("\nExercise 7 - Password attempts:")
max_attempts = 3
password = "secret"
# Simulating attempts (normally would use input())
attempts = ["wrong1", "wrong2", "secret"]
for attempt_num, guess in enumerate(attempts, 1):
    print(f"  Attempt {attempt_num}: '{guess}'")
    if guess == password:
        print("  Access granted!")
        break
else:
    print("  Too many failed attempts. Account locked.")
