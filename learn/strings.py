# ============================================================
# 3. STRINGS AND TEXT
# ============================================================
# A string is a sequence of characters - letters, numbers,
# symbols, spaces, anything you can type!

# ------------------------------------------------------------
# CREATING STRINGS
# ------------------------------------------------------------
# Single quotes or double quotes - both work exactly the same!
greeting = "Hello"
greeting2 = 'Hello'

# When to use which?
sentence = "It's a beautiful day"    # Use double quotes when text has apostrophe
quote = 'He said "Hello"'            # Use single quotes when text has double quotes
mixed = "He said \"Hello\""          # Or use backslash to escape quotes

# Empty string
nothing = ""

# For longer text, use triple quotes
long_text = """
This is a very long piece of text
that spans multiple lines.
Triple quotes let you do this!
You can include 'single' and "double" quotes freely.
"""

print("=== Creating Strings ===")
print(greeting)
print(sentence)
print(quote)
print(long_text)

# ------------------------------------------------------------
# SPECIAL CHARACTERS (ESCAPE SEQUENCES)
# ------------------------------------------------------------
print("\n=== Special Characters ===")

# Backslash (\) gives special meaning to the next character
print("Hello\nWorld")    # \n = new line

print("Tab\tHere")       # \t = tab space

print("Line1\\Line2")    # \\ = actual backslash

print("She said \"Hi\"")  # \" = quote inside quotes

# Raw strings (ignore escape sequences) - useful for file paths
path = r"C:\Users\Name\Documents"  # The 'r' means raw
print(path)

# ------------------------------------------------------------
# STRING INDEXING AND SLICING
# ------------------------------------------------------------
print("\n=== String Indexing and Slicing ===")

text = "Python"

# Get individual characters by index (position number)
print(f"text[0] = {text[0]}")    # P (first character)
print(f"text[1] = {text[1]}")    # y (second character)
print(f"text[-1] = {text[-1]}")  # n (last character)
print(f"text[-2] = {text[-2]}")  # o (second to last)

# Slicing: get a portion of the string [start:end]
# Note: end is NOT included!
print(f"text[0:3] = {text[0:3]}")  # Pyt (characters 0, 1, 2)
print(f"text[2:5] = {text[2:5]}")  # tho (characters 2, 3, 4)

# Shortcuts
print(f"text[:3] = {text[:3]}")   # Pyt (from beginning to index 3)
print(f"text[3:] = {text[3:]}")   # hon (from index 3 to end)
print(f"text[:] = {text[:]}")     # Python (copy of entire string)

# Step: every nth character [start:end:step]
print(f"text[::2] = {text[::2]}")   # Pto (every 2nd character)
print(f"text[::-1] = {text[::-1]}")  # nohtyP (reversed!)

# ------------------------------------------------------------
# STRING OPERATIONS
# ------------------------------------------------------------
print("\n=== String Operations ===")

name = "Python"

# Get the length (number of characters)
print(f"len(name) = {len(name)}")  # 6

# Make uppercase or lowercase
print(f"name.upper() = {name.upper()}")      # PYTHON
print(f"name.lower() = {name.lower()}")      # python
print(f"name.title() = {name.title()}")      # Python
print(f"name.capitalize() = {name.capitalize()}")  # Python

# Check what's inside
print(f"'th' in name = {'th' in name}")      # True
print(f"'xyz' in name = {'xyz' in name}")    # False
print(f"'th' not in name = {'th' not in name}")  # False

# Repeat strings
print(f"'Ha' * 3 = {'Ha' * 3}")       # HaHaHa
print(f"'-' * 20 = {'-' * 20}")       # --------------------

# ------------------------------------------------------------
# COMBINING STRINGS
# ------------------------------------------------------------
print("\n=== Combining Strings ===")

first = "Hello"
second = "World"

# Method 1: Using + (concatenation)
result = first + " " + second
print(result)            # Hello World

# Method 2: Using f-strings (formatted strings) - BEST METHOD! ⭐
name = "Alice"
age = 25
message = f"My name is {name} and I am {age} years old"
print(message)

# f-strings can include expressions
price = 19.99
quantity = 3
print(f"Total: ${price * quantity}")  # Total: $59.97
print(f"Half of 10 is {10 / 2}")      # Half of 10 is 5.0

# Method 3: Using .format() (older way)
message = "Hello, {}!".format(name)
print(message)           # Hello, Alice!

# ------------------------------------------------------------
# STRING METHODS REFERENCE
# ------------------------------------------------------------
print("\n=== String Methods ===")

text = "  Hello World  "

# --- Whitespace Methods ---
print(f"strip(): '{text.strip()}'")     # "Hello World"
print(f"lstrip(): '{text.lstrip()}'")   # "Hello World  "
print(f"rstrip(): '{text.rstrip()}'")   # "  Hello World"

# --- Case Methods ---
print(f"'hello'.upper() = {'hello'.upper()}")    # "HELLO"
print(f"'HELLO'.lower() = {'HELLO'.lower()}")    # "hello"
print(f"'hello world'.title() = {'hello world'.title()}")  # "Hello World"

# --- Search Methods ---
text = "Hello World"
print(f"text.find('World') = {text.find('World')}")     # 6
print(f"text.find('Python') = {text.find('Python')}")   # -1 (not found)
print(f"text.count('l') = {text.count('l')}")           # 3
print(f"text.startswith('Hello') = {text.startswith('Hello')}")  # True
print(f"text.endswith('World') = {text.endswith('World')}")      # True

# --- Check Methods (return True/False) ---
print(f"'Hello'.isalpha() = {'Hello'.isalpha()}")   # True
print(f"'12345'.isdigit() = {'12345'.isdigit()}")   # True
print(f"'Hello123'.isalnum() = {'Hello123'.isalnum()}")  # True

# --- Modification Methods ---
text = "Hello World"
print(f"text.replace('World', 'Python') = {text.replace('World', 'Python')}")

# --- Split and Join ---
sentence = "apple,banana,cherry"
fruits = sentence.split(",")       # ['apple', 'banana', 'cherry']
print(f"'{sentence}'.split(',') = {fruits}")

# Join list back into string
result = ", ".join(fruits)         # "apple, banana, cherry"
print(f"', '.join(fruits) = {result}")

# ------------------------------------------------------------
# PRACTICE EXERCISES
# ------------------------------------------------------------
print("\n=== Practice Exercises ===")

# Exercise 1: Extract information from a string
text = "My email is john@example.com"
at_position = text.find("@")
print(f"@ symbol is at position: {at_position}")

# Exercise 2: Clean and validate user input
raw_name = "   ALICE   "
clean_name = raw_name.strip().title()
print(f"Hello, {clean_name}!")  # Hello, Alice!

# Exercise 3: Build a sentence from parts
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # Python is awesome

# Exercise 4: Reverse a string
original = "Hello"
reversed_text = original[::-1]
print(f"Reversed: {reversed_text}")  # olleH

# Exercise 5: Count words in a sentence
text = "The quick brown fox jumps over the lazy dog"
word_count = len(text.split())
print(f"Word count: {word_count}")  # 9
