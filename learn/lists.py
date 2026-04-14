# ============================================================
# 6. LISTS AND COLLECTIONS
# ============================================================
# A list is an ordered collection of items.

import copy

# ------------------------------------------------------------
# CREATING LISTS
# ------------------------------------------------------------
print("=== Creating Lists ===")

# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]  # Can mix types!
empty_list = []
nested = [[1, 2], [3, 4], [5, 6]]  # List of lists!

# Using list() constructor
letters = list("hello")   # ['h', 'e', 'l', 'l', 'o']
from_range = list(range(5))  # [0, 1, 2, 3, 4]

print(f"fruits = {fruits}")
print(f"numbers = {numbers}")
print(f"mixed = {mixed}")
print(f"nested = {nested}")
print(f"list('hello') = {letters}")
print(f"list(range(5)) = {from_range}")

# ------------------------------------------------------------
# ACCESSING ITEMS
# ------------------------------------------------------------
print("\n=== Accessing Items ===")

fruits = ["apple", "banana", "cherry", "date"]
#            0         1         2        3    <- positive indexes
#           -4        -3        -2       -1    <- negative indexes

# Single item access
print(f"fruits[0] = {fruits[0]}")     # apple (first item)
print(f"fruits[1] = {fruits[1]}")     # banana (second item)
print(f"fruits[-1] = {fruits[-1]}")   # date (last item)
print(f"fruits[-2] = {fruits[-2]}")   # cherry (second to last)

# Safe access with bounds checking
if len(fruits) > 10:
    print(fruits[10])
else:
    print("Index 10 is out of range!")

# ------------------------------------------------------------
# SLICING LISTS
# ------------------------------------------------------------
print("\n=== Slicing Lists ===")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#            0         1         2        3          4

# [start:end] - end is NOT included!
print(f"fruits[1:4] = {fruits[1:4]}")    # ['banana', 'cherry', 'date']
print(f"fruits[:3] = {fruits[:3]}")      # ['apple', 'banana', 'cherry']
print(f"fruits[2:] = {fruits[2:]}")      # ['cherry', 'date', 'elderberry']
print(f"fruits[:] = {fruits[:]}")        # Copy entire list

# [start:end:step]
print(f"fruits[::2] = {fruits[::2]}")    # ['apple', 'cherry', 'elderberry']
print(f"fruits[::-1] = {fruits[::-1]}")  # Reversed!

# Slicing creates a NEW list (original unchanged)
first_two = fruits[:2]
first_two[0] = "CHANGED"
print(f"After changing slice, original: {fruits[0]}")  # Still 'apple'

# ------------------------------------------------------------
# MODIFYING LISTS
# ------------------------------------------------------------
print("\n=== Modifying Lists ===")

fruits = ["apple", "banana", "cherry"]
print(f"Original: {fruits}")

# --- Changing Items ---
fruits[0] = "apricot"
print(f"After fruits[0] = 'apricot': {fruits}")

# --- Adding Items ---
fruits.append("date")           # Add ONE item to end
print(f"After append('date'): {fruits}")

fruits.insert(1, "blueberry")   # Insert at specific position
print(f"After insert(1, 'blueberry'): {fruits}")

fruits.extend(["elderberry", "fig"])  # Add MULTIPLE items
print(f"After extend(['elderberry', 'fig']): {fruits}")

# Difference between append and extend:
list1 = [1, 2, 3]
list1.append([4, 5])     # Adds [4, 5] as ONE element
print(f"append([4, 5]): {list1}")  # [1, 2, 3, [4, 5]]

list2 = [1, 2, 3]
list2.extend([4, 5])     # Adds 4 and 5 as separate elements
print(f"extend([4, 5]): {list2}")  # [1, 2, 3, 4, 5]

# --- Removing Items ---
fruits = ["apple", "banana", "cherry", "banana", "date"]
print(f"\nOriginal: {fruits}")

fruits.remove("banana")         # Remove first occurrence
print(f"After remove('banana'): {fruits}")

last = fruits.pop()             # Remove and return LAST item
print(f"After pop(): {fruits}, removed: {last}")

item = fruits.pop(0)            # Remove and return item at index 0
print(f"After pop(0): {fruits}, removed: {item}")

del fruits[0]                   # Delete item at index
print(f"After del fruits[0]: {fruits}")

fruits.clear()                  # Remove ALL items
print(f"After clear(): {fruits}")

# ------------------------------------------------------------
# LIST OPERATIONS
# ------------------------------------------------------------
print("\n=== List Operations ===")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"numbers = {numbers}")

# --- Basic Operations ---
print(f"len(numbers) = {len(numbers)}")      # 8
print(f"sum(numbers) = {sum(numbers)}")      # 31
print(f"min(numbers) = {min(numbers)}")      # 1
print(f"max(numbers) = {max(numbers)}")      # 9

# Membership testing
print(f"4 in numbers = {4 in numbers}")      # True
print(f"7 in numbers = {7 in numbers}")      # False
print(f"7 not in numbers = {7 not in numbers}")  # True

# Count occurrences
print(f"numbers.count(1) = {numbers.count(1)}")  # 2

# Find index of item
print(f"numbers.index(4) = {numbers.index(4)}")  # 2

# --- Combining Lists ---
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
repeated = list1 * 3
print(f"[1, 2, 3] + [4, 5, 6] = {combined}")
print(f"[1, 2, 3] * 3 = {repeated}")

# --- Sorting ---
numbers = [3, 1, 4, 1, 5, 9]
print(f"\nOriginal: {numbers}")

numbers.sort()               # Sort IN PLACE
print(f"After sort(): {numbers}")

numbers.sort(reverse=True)   # Sort descending
print(f"After sort(reverse=True): {numbers}")

# sorted() returns NEW list
original = [3, 1, 4, 1, 5]
new_sorted = sorted(original)
print(f"Original unchanged: {original}")
print(f"sorted(original): {new_sorted}")

# --- Reversing ---
numbers = [1, 2, 3, 4, 5]
numbers.reverse()            # Reverse IN PLACE
print(f"After reverse(): {numbers}")

# Create reversed copy
reversed_copy = numbers[::-1]
print(f"Reversed copy: {reversed_copy}")

# ------------------------------------------------------------
# ITERATING OVER LISTS
# ------------------------------------------------------------
print("\n=== Iterating Over Lists ===")

fruits = ["apple", "banana", "cherry"]

# Simple loop
print("Simple loop:")
for fruit in fruits:
    print(f"  {fruit}")

# With index using enumerate()
print("\nWith enumerate():")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# Start enumeration at different number
print("\nStarting from 1:")
for num, fruit in enumerate(fruits, start=1):
    print(f"  {num}. {fruit}")

# ------------------------------------------------------------
# LIST COMPREHENSIONS
# ------------------------------------------------------------
print("\n=== List Comprehensions ===")

# Traditional way
squares = []
for x in range(5):
    squares.append(x ** 2)
print(f"Traditional squares: {squares}")

# List comprehension (same result, one line!)
squares = [x ** 2 for x in range(5)]
print(f"Comprehension squares: {squares}")

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers: {evens}")

# Transform strings
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Uppercase words: {upper_words}")

# Filter and transform
numbers = [-3, -1, 0, 1, 4, 9]
positive_squares = [n ** 2 for n in numbers if n > 0]
print(f"Positive squares: {positive_squares}")

# ------------------------------------------------------------
# COPYING LISTS
# ------------------------------------------------------------
print("\n=== Copying Lists ===")

# ⚠️ Be careful with list copying!
original = [1, 2, 3]

# This does NOT create a copy!
reference = original
reference[0] = 99
print(f"After reference[0] = 99, original = {original}")  # [99, 2, 3]!

# To create an actual copy:
original = [1, 2, 3]

# Method 1: slice
copy1 = original[:]

# Method 2: list()
copy2 = list(original)

# Method 3: copy()
copy3 = original.copy()

# Now changing the copy doesn't affect original
copy1[0] = 99
print(f"After copy1[0] = 99, original = {original}")  # [1, 2, 3]

# For nested lists, use deepcopy
nested = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(nested)
deep_copy[0][0] = 99
print(f"After deep_copy[0][0] = 99, nested = {nested}")  # [[1, 2], [3, 4]]

# ------------------------------------------------------------
# PRACTICE EXERCISES
# ------------------------------------------------------------
print("\n=== Practice Exercises ===")

# Exercise 1: Create and modify a list
shopping = ["milk", "bread", "eggs"]
shopping.append("butter")
shopping.insert(0, "coffee")
shopping.remove("bread")
print(f"Exercise 1 - Shopping list: {shopping}")

# Exercise 2: Find the largest number
numbers = [45, 22, 88, 14, 67, 93, 31]
largest = max(numbers)
print(f"Exercise 2 - Largest: {largest}")

# Exercise 3: Calculate average
scores = [85, 92, 78, 90, 88]
average = sum(scores) / len(scores)
print(f"Exercise 3 - Average: {average:.1f}")

# Exercise 4: List comprehension - Even squares
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(f"Exercise 4 - Even squares: {even_squares}")

# Exercise 5: Reverse without reverse()
original = [1, 2, 3, 4, 5]
reversed_list = original[::-1]
print(f"Exercise 5 - Reversed: {reversed_list}")

# Exercise 6: Remove duplicates (keep order)
with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
unique = list(dict.fromkeys(with_duplicates))
print(f"Exercise 6 - Unique: {unique}")
