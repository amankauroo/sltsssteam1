# ============================================================
# 8. IF STATEMENTS (CONDITIONALS)
# ============================================================
# Conditionals let your program make decisions -
# do different things based on different situations.

# ------------------------------------------------------------
# BASIC IF STATEMENT
# ------------------------------------------------------------
print("=== Basic If Statement ===")

age = 18

if age >= 18:
    print("You are an adult!")
    print("You can vote!")

# CRITICAL: Python uses indentation (4 spaces) to show what's inside the if block!

# ✅ CORRECT - indented code is inside the if block
if True:
    print("This is inside the if")
    print("This too")
print("This is outside - always runs")

# ------------------------------------------------------------
# IF-ELSE
# ------------------------------------------------------------
print("\n=== If-Else ===")

age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Another example
temperature = 30

if temperature > 25:
    print("It's hot outside!")
    print("Remember to drink water")
else:
    print("It's not too hot")
    print("Enjoy your day!")

# ------------------------------------------------------------
# IF-ELIF-ELSE
# ------------------------------------------------------------
print("\n=== If-Elif-Else ===")

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score} → Grade {grade}")

# Order matters! Check most specific first
print("\n--- Order Matters Demo ---")

# CORRECT ORDER - check highest first
score = 95
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score} → Grade {grade}")  # A (correct!)

# ------------------------------------------------------------
# COMBINING CONDITIONS
# ------------------------------------------------------------
print("\n=== Combining Conditions ===")

age = 25
has_id = True

# Using 'and' - BOTH must be true
if age >= 21 and has_id:
    print("You can enter the bar")

# Using 'or' - AT LEAST ONE must be true
weather = "rainy"
if weather == "sunny" or weather == "cloudy":
    print("Go outside!")
else:
    print("Stay inside!")

# Using 'not' - flip the condition
is_closed = False
if not is_closed:
    print("The store is open!")

# Complex conditions - use parentheses for clarity
is_student = True

if (age >= 21 or is_student) and has_id:
    print("You get a discount!")

# ------------------------------------------------------------
# NESTED IF STATEMENTS
# ------------------------------------------------------------
print("\n=== Nested If Statements ===")

is_member = True
has_discount = True

if is_member:
    print("Welcome, member!")
    if has_discount:
        print("You get 20% off!")
    else:
        print("No current discounts")
else:
    print("Join us to get member benefits!")

# Better approach - less nesting
print("\n--- Better Approach (less nesting) ---")
if not is_member:
    print("Join us to get member benefits!")
elif has_discount:
    print("Welcome, member! You get 20% off!")
else:
    print("Welcome, member! No current discounts")

# ------------------------------------------------------------
# TERNARY OPERATOR (INLINE IF)
# ------------------------------------------------------------
print("\n=== Ternary Operator ===")

# Traditional if-else
age = 20
if age >= 18:
    status = "adult"
else:
    status = "minor"
print(f"Traditional: {status}")

# Ternary operator (same result, one line!)
status = "adult" if age >= 18 else "minor"
print(f"Ternary: {status}")

# Use for simple assignments
x = 10
message = "positive" if x > 0 else "non-positive"
print(f"x = {x}: {message}")

# Can be nested (but don't overdo it!)
x = 0
message = "positive" if x > 0 else "zero" if x == 0 else "negative"
print(f"x = {x}: {message}")

# ------------------------------------------------------------
# MATCH STATEMENT (Python 3.10+)
# ------------------------------------------------------------
print("\n=== Match Statement (Python 3.10+) ===")

# Match is great for checking specific values
command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "pause":
        print("Pausing...")
    case _:  # Default case (like else)
        print("Unknown command")

# Match with patterns
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On Y-axis at y={y}")
    case (x, 0):
        print(f"On X-axis at x={x}")
    case (x, y):
        print(f"Point at ({x}, {y})")

# ------------------------------------------------------------
# COMMON PATTERNS
# ------------------------------------------------------------
print("\n=== Common Patterns ===")

# Check if string is empty
text = ""
if text:  # Empty string is falsy
    print("Has text")
else:
    print("Empty string!")

# Check if list has items
items = []
if items:  # Empty list is falsy
    print(f"Has {len(items)} items")
else:
    print("List is empty!")

# Check for None
value = None
if value is None:
    print("No value (is None)")

# Multiple conditions with 'in'
color = "red"
if color in ["red", "green", "blue"]:
    print("Primary color!")

# Range check - Python allows chained comparisons!
age = 25
if 18 <= age <= 65:
    print("Working age")

# ------------------------------------------------------------
# PRACTICE EXERCISES
# ------------------------------------------------------------
print("\n=== Practice Exercises ===")

# Exercise 1: Simple age check
age = 17
print(f"\nExercise 1: Age = {age}")
if age >= 18:
    print("  You can vote!")
else:
    print("  Too young to vote")

# Exercise 2: Grade calculator
score = 78
print(f"\nExercise 2: Score = {score}")
if score >= 90:
    print("  A - Excellent!")
elif score >= 80:
    print("  B - Good!")
elif score >= 70:
    print("  C - Average")
elif score >= 60:
    print("  D - Below average")
else:
    print("  F - Needs improvement")

# Exercise 3: Number classifier
num = -5
print(f"\nExercise 3: Number = {num}")
if num > 0:
    print("  Positive")
elif num < 0:
    print("  Negative")
else:
    print("  Zero")

# Exercise 4: Login check
username = "admin"
password = "secret123"
print(f"\nExercise 4: Login attempt")
if username == "admin" and password == "secret123":
    print("  Login successful!")
else:
    print("  Invalid credentials")

# Exercise 5: Discount calculator
is_member = True
purchase = 150
print(f"\nExercise 5: Member={is_member}, Purchase=${purchase}")
if is_member:
    if purchase >= 100:
        discount = 20
    else:
        discount = 10
else:
    discount = 0
print(f"  Your discount: {discount}%")
