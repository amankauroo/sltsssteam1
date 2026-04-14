# ============================================================
# 7. DICTIONARIES
# ============================================================
# A dictionary stores pairs of keys and values.
# Like a real dictionary: the word is the key, the definition is the value.

from collections import defaultdict

# ------------------------------------------------------------
# CREATING DICTIONARIES
# ------------------------------------------------------------
print("=== Creating Dictionaries ===")

# Creating a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(f"person = {person}")

# Other ways to create dictionaries
empty_dict = {}
empty_dict2 = dict()

# From list of tuples
pairs = dict([("a", 1), ("b", 2), ("c", 3)])
print(f"From tuples: {pairs}")

# From keyword arguments
person2 = dict(name="Bob", age=30, city="Boston")
print(f"From kwargs: {person2}")

# ------------------------------------------------------------
# ACCESSING VALUES
# ------------------------------------------------------------
print("\n=== Accessing Values ===")

person = {"name": "Alice", "age": 25, "city": "New York"}

# --- Using [] (bracket notation) ---
print(f"person['name'] = {person['name']}")
print(f"person['age'] = {person['age']}")
# print(person["email"])     # ⚠️ KeyError! Key doesn't exist

# --- Using .get() (SAFER - won't crash!) ---
print(f"person.get('name') = {person.get('name')}")
print(f"person.get('email') = {person.get('email')}")  # None
print(f"person.get('email', 'No email') = {person.get('email', 'No email')}")

# When to use which?
# - Use [] when you're SURE the key exists
# - Use .get() when the key MIGHT not exist

# ------------------------------------------------------------
# CHECKING IF KEY EXISTS
# ------------------------------------------------------------
print("\n=== Checking If Key Exists ===")

person = {"name": "Alice", "age": 25}

# Check if key exists
if "name" in person:
    print(f"Name exists: {person['name']}")

# Check if key doesn't exist
if "email" not in person:
    print("No email on file")

# Get all keys and values
print(f"person.keys() = {list(person.keys())}")
print(f"person.values() = {list(person.values())}")
print(f"person.items() = {list(person.items())}")

# ------------------------------------------------------------
# MODIFYING DICTIONARIES
# ------------------------------------------------------------
print("\n=== Modifying Dictionaries ===")

person = {"name": "Alice", "age": 25}
print(f"Original: {person}")

# --- Add or Change Values ---
person["email"] = "alice@example.com"  # Add new key
person["age"] = 26                      # Change existing value
print(f"After add/change: {person}")

# Add only if key doesn't exist
person.setdefault("city", "Unknown")  # Adds "city": "Unknown"
person.setdefault("name", "Bob")      # Does nothing (name already exists)
print(f"After setdefault: {person}")

# --- Update Multiple Values at Once ---
person.update({"age": 27, "phone": "555-1234"})
print(f"After update: {person}")

# --- Remove Values ---
del person["phone"]                   # Delete by key
print(f"After del phone: {person}")

email = person.pop("email")           # Remove and return value
print(f"pop('email') returned: {email}")

city = person.pop("city", None)       # Safe removal
print(f"After pop city: {person}")

# popitem() removes last item
person["temp"] = "value"
last_item = person.popitem()          # Remove and return last item
print(f"popitem() returned: {last_item}")

# clear() removes ALL items
person_copy = {"a": 1, "b": 2}
person_copy.clear()
print(f"After clear(): {person_copy}")

# ------------------------------------------------------------
# ITERATING OVER DICTIONARIES
# ------------------------------------------------------------
print("\n=== Iterating Over Dictionaries ===")

person = {"name": "Alice", "age": 25, "city": "NYC"}

# Loop through keys (default)
print("Keys:")
for key in person:
    print(f"  {key}")

# Loop through values
print("\nValues:")
for value in person.values():
    print(f"  {value}")

# Loop through both keys and values (most common)
print("\nKey-Value pairs:")
for key, value in person.items():
    print(f"  {key}: {value}")

# ------------------------------------------------------------
# NESTED DICTIONARIES
# ------------------------------------------------------------
print("\n=== Nested Dictionaries ===")

# A dictionary containing other dictionaries
users = {
    "user1": {
        "name": "Alice",
        "email": "alice@example.com"
    },
    "user2": {
        "name": "Bob",
        "email": "bob@example.com"
    }
}

# Access nested values
print(f"users['user1']['name'] = {users['user1']['name']}")
print(f"users['user2']['email'] = {users['user2']['email']}")

# Safe nested access
email = users.get("user3", {}).get("email", "No email")
print(f"user3 email (safe access): {email}")

# Settings example (common pattern)
settings = {
    "video": {
        "resolution": "1080p",
        "framerate": 30
    },
    "audio": {
        "volume": 80,
        "mute": False
    }
}

print(f"Resolution: {settings['video']['resolution']}")
print(f"Volume: {settings['audio']['volume']}")

# Modify nested value
settings["audio"]["volume"] = 90
print(f"New volume: {settings['audio']['volume']}")

# ------------------------------------------------------------
# DICTIONARY COMPREHENSIONS
# ------------------------------------------------------------
print("\n=== Dictionary Comprehensions ===")

# Create dictionary from lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = {name: age for name, age in zip(names, ages)}
print(f"From two lists: {people}")

# Create from range
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# With condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Transform values
prices = {"apple": 1.50, "banana": 0.75, "cherry": 2.00}
discounted = {item: round(price * 0.9, 2) for item, price in prices.items()}
print(f"10% discount: {discounted}")

# ------------------------------------------------------------
# COMMON DICTIONARY PATTERNS
# ------------------------------------------------------------
print("\n=== Common Patterns ===")

# Count occurrences
text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(f"Character count: {char_count}")

# Using defaultdict (better for counting)
word_count = defaultdict(int)  # Default value is 0
words = ["apple", "banana", "apple", "cherry", "apple"]
for word in words:
    word_count[word] += 1
print(f"Word count: {dict(word_count)}")

# Group items
students = [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("Diana", "B")
]
by_grade = defaultdict(list)
for name, grade in students:
    by_grade[grade].append(name)
print(f"Grouped by grade: {dict(by_grade)}")

# Merge dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# merged = dict1 | dict2  # Python 3.9+
merged = {**dict1, **dict2}  # Works in all Python 3.x
print(f"Merged: {merged}")

# ------------------------------------------------------------
# PRACTICE EXERCISES
# ------------------------------------------------------------
print("\n=== Practice Exercises ===")

# Exercise 1: Create and access a dictionary
student = {
    "name": "John",
    "grade": 10,
    "subjects": ["Math", "Science", "English"]
}
print(f"Exercise 1:")
print(f"  Name: {student['name']}")
print(f"  First subject: {student['subjects'][0]}")

# Exercise 2: Safe access with .get()
config = {"debug": True, "timeout": 30}
verbose = config.get("verbose", False)  # Returns False (default)
print(f"\nExercise 2:")
print(f"  verbose (with default): {verbose}")

# Exercise 3: Count letter frequency
text = "mississippi"
count = {}
for letter in text:
    count[letter] = count.get(letter, 0) + 1
print(f"\nExercise 3:")
print(f"  Letter count in 'mississippi': {count}")

# Exercise 4: Dictionary comprehension
numbers = [1, 2, 3, 4, 5]
cubes = {n: n**3 for n in numbers}
print(f"\nExercise 4:")
print(f"  Cubes: {cubes}")

# Exercise 5: Merge two dictionaries
defaults = {"color": "blue", "size": "medium"}
custom = {"size": "large", "font": "Arial"}
final = {**defaults, **custom}  # custom overrides defaults
print(f"\nExercise 5:")
print(f"  Merged settings: {final}")
