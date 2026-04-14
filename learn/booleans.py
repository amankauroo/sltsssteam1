# ============================================================
# 5. BOOLEANS AND COMPARISONS
# ============================================================
# Booleans are simple: they're either True or False. That's it!

# ------------------------------------------------------------
# CREATING BOOLEAN VARIABLES
# ------------------------------------------------------------
print("=== Boolean Values ===")

is_sunny = True
is_raining = False

print(f"is_sunny = {is_sunny}")
print(f"type(is_sunny) = {type(is_sunny)}")

# Common naming: Start with is_, has_, can_, should_
is_logged_in = True
has_permission = False
can_edit = True
should_continue = False

print(f"\nis_logged_in = {is_logged_in}")
print(f"has_permission = {has_permission}")
print(f"can_edit = {can_edit}")

# ------------------------------------------------------------
# COMPARISON OPERATORS
# ------------------------------------------------------------
print("\n=== Comparison Operators ===")

a = 10
b = 5

# Basic comparisons
print(f"a = {a}, b = {b}")
print(f"a == b  → {a == b}")    # Equal to:              False
print(f"a != b  → {a != b}")    # Not equal to:          True
print(f"a > b   → {a > b}")     # Greater than:          True
print(f"a < b   → {a < b}")     # Less than:             False
print(f"a >= b  → {a >= b}")    # Greater than or equal: True
print(f"a <= b  → {a <= b}")    # Less than or equal:    False

# ⚠️ COMMON MISTAKE: = vs ==
# = is for assignment (putting a value in a variable)
# == is for comparison (checking if two values are equal)
x = 5        # Assignment: x is now 5
result = (x == 5)  # Comparison: Is x equal to 5? True
print(f"\nx = 5; x == 5 → {result}")

# Chained comparisons (Python special feature!)
age = 25
print(f"\nage = {age}")
print(f"18 <= age <= 65 → {18 <= age <= 65}")  # True

# ------------------------------------------------------------
# COMPARING DIFFERENT TYPES
# ------------------------------------------------------------
print("\n=== Comparing Different Types ===")

# Numbers compare by value
print(f"5 == 5.0 → {5 == 5.0}")       # True (int and float with same value)
print(f"5 > 3 → {5 > 3}")             # True

# Strings compare alphabetically (lexicographically)
print(f"'apple' < 'banana' → {'apple' < 'banana'}")   # True
print(f"'Apple' < 'apple' → {'Apple' < 'apple'}")     # True (uppercase first)
print(f"'abc' == 'abc' → {'abc' == 'abc'}")           # True
print(f"'abc' == 'ABC' → {'abc' == 'ABC'}")           # False (case matters!)

# Lists compare element by element
print(f"[1, 2] == [1, 2] → {[1, 2] == [1, 2]}")       # True
print(f"[1, 2] < [1, 3] → {[1, 2] < [1, 3]}")         # True
print(f"[1, 2] < [1, 2, 3] → {[1, 2] < [1, 2, 3]}")   # True

# ------------------------------------------------------------
# LOGICAL OPERATORS
# ------------------------------------------------------------
print("\n=== Logical Operators (and, or, not) ===")

age = 25
has_license = True
is_sober = True
has_vip_pass = False

# AND - ALL conditions must be True
can_drive = age >= 18 and has_license and is_sober
print(f"age >= 18 and has_license and is_sober → {can_drive}")

# OR - ANY condition must be True
can_enter = age >= 21 or has_vip_pass
print(f"age >= 21 or has_vip_pass → {can_enter}")

# NOT - Reverses the boolean
is_minor = not (age >= 18)
print(f"not (age >= 18) → {is_minor}")

# Complex combinations
is_student = True
has_discount = (age < 18) or (age >= 65) or is_student
print(f"(age < 18) or (age >= 65) or is_student → {has_discount}")

# Truth tables demonstration
print("\n--- AND Truth Table ---")
print(f"True  and True  = {True and True}")
print(f"True  and False = {True and False}")
print(f"False and True  = {False and True}")
print(f"False and False = {False and False}")

print("\n--- OR Truth Table ---")
print(f"True  or True  = {True or True}")
print(f"True  or False = {True or False}")
print(f"False or True  = {False or True}")
print(f"False or False = {False or False}")

print("\n--- NOT Truth Table ---")
print(f"not True  = {not True}")
print(f"not False = {not False}")

# ------------------------------------------------------------
# SHORT-CIRCUIT EVALUATION
# ------------------------------------------------------------
print("\n=== Short-Circuit Evaluation ===")

# Python stops evaluating as soon as it knows the answer!
x = 0
# With AND: if first is False, don't check the rest
if x != 0 and 10/x > 1:   # Safe! 10/x never runs because x != 0 is False
    print("This won't print")
else:
    print("Safe! 10/x was not evaluated because x != 0 is False")

# With OR: if first is True, don't check the rest
name = "Alice"
if name or None.something():  # None.something() never runs
    print("Has a name!")

# Useful for "default values":
input_name = ""  # Empty string
user_name = input_name or "Guest"  # Use "Guest" if input_name is empty
print(f"user_name = {user_name}")

# ------------------------------------------------------------
# TRUTHY AND FALSY VALUES
# ------------------------------------------------------------
print("\n=== Truthy and Falsy Values ===")

# FALSY values (treated as False in conditions):
# - False
# - None
# - 0 (zero, including 0.0)
# - "" (empty string)
# - [] (empty list)
# - {} (empty dictionary)
# - () (empty tuple)

# TRUTHY values (treated as True in conditions):
# - Everything else!

print("Falsy values:")
print(f"bool(False) = {bool(False)}")
print(f"bool(None) = {bool(None)}")
print(f"bool(0) = {bool(0)}")
print(f"bool('') = {bool('')}")
print(f"bool([]) = {bool([])}")
print(f"bool({{}}) = {bool({})}")

print("\nTruthy values:")
print(f"bool(True) = {bool(True)}")
print(f"bool(1) = {bool(1)}")
print(f"bool('Hello') = {bool('Hello')}")
print(f"bool([1, 2, 3]) = {bool([1, 2, 3])}")
print(f"bool({{'a': 1}}) = {bool({'a': 1})}")

# Practical use: Check if list has items
items = [1, 2, 3]
if items:             # Same as: if len(items) > 0
    print("\nList has items!")

# Practical use: Check if user entered something
name = ""
if name:
    print(f"Hello, {name}!")
else:
    print("You didn't enter a name!")

# ------------------------------------------------------------
# IDENTITY VS EQUALITY
# ------------------------------------------------------------
print("\n=== Identity vs Equality (== vs is) ===")

# == checks if VALUES are equal
# is checks if they're the SAME OBJECT in memory

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = [1, 2, 3]")
print(f"b = [1, 2, 3]")
print(f"c = a")
print(f"a == b → {a == b}")    # True - same values
print(f"a is b → {a is b}")    # False - different objects in memory
print(f"a is c → {a is c}")    # True - c points to the same object as a

# Use 'is' only for:
# - Checking None
# - Checking True/False
result = None
if result is None:
    print("Result is None")

# ------------------------------------------------------------
# PRACTICE EXERCISES
# ------------------------------------------------------------
print("\n=== Practice Exercises ===")

# Exercise 1: Age verification
age = 17
can_vote = age >= 18
can_drink = age >= 21
print(f"\nExercise 1: Age = {age}")
print(f"Can vote: {can_vote}")
print(f"Can drink: {can_drink}")

# Exercise 2: Password validation
password = "Secret123"
is_long_enough = len(password) >= 8
has_number = any(c.isdigit() for c in password)
is_valid = is_long_enough and has_number
print(f"\nExercise 2: Password validation")
print(f"Password: {password}")
print(f"Long enough (>= 8 chars): {is_long_enough}")
print(f"Has number: {has_number}")
print(f"Valid: {is_valid}")

# Exercise 3: Grade calculator with conditions
score = 85
grade = ""
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"\nExercise 3: Score {score} = Grade {grade}")

# Exercise 4: Truthy/Falsy practice
print("\nExercise 4: Truthy/Falsy check")
values = [0, 1, "", "hello", [], [1], None, True, False]
for v in values:
    print(f"{str(v):10} is {'Truthy' if v else 'Falsy'}")

# Exercise 5: Range check with chained comparison
temperature = 72
is_comfortable = 68 <= temperature <= 76
print(f"\nExercise 5: Temperature = {temperature}")
print(f"Comfortable (68-76): {is_comfortable}")
