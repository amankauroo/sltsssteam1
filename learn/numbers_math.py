# ============================================================
# 4. NUMBERS AND MATH
# ============================================================
# Python has two main types of numbers: integers and floats

from decimal import Decimal
import math

# ------------------------------------------------------------
# TYPES OF NUMBERS
# ------------------------------------------------------------
print("=== Types of Numbers ===")

# Integers (whole numbers) - no decimal point
count = 10
negative = -5
big_number = 1000000
zero = 0

# Use underscores for readability (Python 3.6+)
million = 1_000_000           # Same as 1000000
phone = 555_123_4567          # Easier to read!

print(f"Integer: {count}, type: {type(count)}")
print(f"Million with underscores: {million}")

# Floats (decimal numbers) - has decimal point
price = 19.99
pi = 3.14159
temperature = -2.5
tiny = 0.0001
percentage = 0.75             # 75%

print(f"Float: {price}, type: {type(price)}")
print(f"Pi: {pi}")

# Scientific notation for very large/small numbers
speed_of_light = 3e8          # 3 × 10^8 = 300,000,000
electron_mass = 9.109e-31     # Very tiny number

print(f"Speed of light: {speed_of_light}")
print(f"Electron mass: {electron_mass}")

# ------------------------------------------------------------
# MATH OPERATIONS
# ------------------------------------------------------------
print("\n=== Math Operations ===")

a = 10
b = 3

# Basic operations
print(f"{a} + {b} = {a + b}")     # Addition:       13
print(f"{a} - {b} = {a - b}")     # Subtraction:    7
print(f"{a} * {b} = {a * b}")     # Multiplication: 30
# Division:       3.3333... (always returns float!)
print(f"{a} / {b} = {a / b}")
# Floor Division: 3 (removes decimal, returns int)
print(f"{a} // {b} = {a // b}")
# Modulo:         1 (the remainder after division)
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")   # Power:          1000 (10 × 10 × 10)

# Order of operations (PEMDAS/BODMAS)
result1 = 2 + 3 * 4      # = 14 (multiplication first)
result2 = (2 + 3) * 4    # = 20 (parentheses first)
print(f"2 + 3 * 4 = {result1}")
print(f"(2 + 3) * 4 = {result2}")

# ------------------------------------------------------------
# DIVISION EXPLAINED
# ------------------------------------------------------------
print("\n=== Division Types ===")

# Regular division (/) always returns a float
print(f"10 / 2 = {10 / 2}")      # 5.0 (not 5!)
print(f"10 / 3 = {10 / 3}")      # 3.3333...

# Floor division (//) rounds DOWN to nearest integer
print(f"10 // 3 = {10 // 3}")    # 3 (removes .333...)
print(f"7 // 2 = {7 // 2}")      # 3 (removes .5)
print(f"-7 // 2 = {-7 // 2}")    # -4 (rounds DOWN, not toward zero!)

# Modulo (%) gives the remainder
print(f"10 % 3 = {10 % 3}")      # 1 (because 10 = 3×3 + 1)
print(f"17 % 5 = {17 % 5}")      # 2 (because 17 = 5×3 + 2)
print(f"10 % 2 = {10 % 2}")      # 0 (no remainder - 10 is even!)

# Useful: Check if number is even or odd
number = 42
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")

# ------------------------------------------------------------
# SHORTHAND OPERATORS
# ------------------------------------------------------------
print("\n=== Shorthand Operators ===")

x = 10
print(f"Start with x = {x}")

x += 5      # Add 5 to x
print(f"x += 5  →  x = {x}")

x -= 3      # Subtract 3
print(f"x -= 3  →  x = {x}")

x *= 2      # Multiply by 2
print(f"x *= 2  →  x = {x}")

x /= 4      # Divide by 4
print(f"x /= 4  →  x = {x}")

x //= 2     # Floor divide by 2
print(f"x //= 2  →  x = {x}")

x **= 2     # Square it
print(f"x **= 2  →  x = {x}")

# ------------------------------------------------------------
# USEFUL NUMBER FUNCTIONS
# ------------------------------------------------------------
print("\n=== Built-in Functions ===")

# --- Type Conversion ---
text_number = "42"
real_number = int(text_number)    # Convert string to integer
print(f"int('42') + 8 = {real_number + 8}")

decimal = float("3.14")           # Convert string to float
print(f"float('3.14') = {decimal}")

# Warning: int() truncates, doesn't round!
print(f"int(3.9) = {int(3.9)}")    # 3 (not 4!)
print(f"int(-3.9) = {int(-3.9)}")  # -3 (not -4!)

# --- Rounding ---
print(f"round(3.7) = {round(3.7)}")        # 4
print(f"round(3.14159, 2) = {round(3.14159, 2)}")  # 3.14
print(f"round(3.5) = {round(3.5)}")        # 4 (banker's rounding)
print(f"round(2.5) = {round(2.5)}")        # 2 (rounds to even)

# --- Absolute Value ---
print(f"abs(-5) = {abs(-5)}")              # 5
print(f"abs(5) = {abs(5)}")                # 5
print(f"abs(-3.14) = {abs(-3.14)}")        # 3.14

# --- Min and Max ---
print(f"min(1, 5, 3) = {min(1, 5, 3)}")    # 1
print(f"max(1, 5, 3) = {max(1, 5, 3)}")    # 5

# --- Sum ---
numbers = [1, 2, 3, 4, 5]
print(f"sum([1, 2, 3, 4, 5]) = {sum(numbers)}")  # 15

# --- Power and Division ---
print(f"pow(2, 3) = {pow(2, 3)}")          # 8
print(f"divmod(17, 5) = {divmod(17, 5)}")  # (3, 2)

# ------------------------------------------------------------
# MATH MODULE
# ------------------------------------------------------------
print("\n=== Math Module ===")

# --- Constants ---
print(f"math.pi = {math.pi}")
print(f"math.e = {math.e}")

# --- Rounding Functions ---
print(f"math.floor(3.9) = {math.floor(3.9)}")   # 3
print(f"math.ceil(3.1) = {math.ceil(3.1)}")     # 4
print(f"math.trunc(3.9) = {math.trunc(3.9)}")   # 3

# --- Square Root ---
print(f"math.sqrt(16) = {math.sqrt(16)}")       # 4.0
print(f"math.sqrt(2) = {math.sqrt(2)}")         # 1.4142135...

# --- Trigonometry ---
print(f"math.sin(math.pi / 2) = {math.sin(math.pi / 2)}")  # 1.0
print(f"math.cos(0) = {math.cos(0)}")           # 1.0

# ------------------------------------------------------------
# COMMON PATTERNS AND FORMULAS
# ------------------------------------------------------------
print("\n=== Common Patterns ===")

# Calculate average
scores = [85, 90, 78, 92, 88]
average = sum(scores) / len(scores)
print(f"Average of {scores}: {average}")

# Calculate percentage
correct = 8
total = 10
percentage = (correct / total) * 100
print(f"Score: {percentage}%")

# Temperature conversion
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Distance formula
x1, y1 = 0, 0
x2, y2 = 3, 4
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"Distance from ({x1},{y1}) to ({x2},{y2}): {distance}")

# Area of a circle
radius = 5
area = math.pi * radius ** 2
print(f"Circle with radius {radius}: Area = {area:.2f}")

# ------------------------------------------------------------
# FLOATING POINT PRECISION
# ------------------------------------------------------------
print("\n=== Floating Point Precision ===")

# ⚠️ Floats are NOT always exact!
print(f"0.1 + 0.2 = {0.1 + 0.2}")  # 0.30000000000000004 (not exactly 0.3!)

# Solutions:
# 1. Round for display
print(f"round(0.1 + 0.2, 1) = {round(0.1 + 0.2, 1)}")  # 0.3

# 2. Compare with tolerance
a = 0.1 + 0.2
b = 0.3
print(f"abs(a - b) < 0.0001 = {abs(a - b) < 0.0001}")  # True

# 3. Use Decimal for money/precision
price = Decimal("0.1") + Decimal("0.2")
print(f"Decimal('0.1') + Decimal('0.2') = {price}")  # 0.3 (exact!)

# ------------------------------------------------------------
# PRACTICE EXERCISES
# ------------------------------------------------------------
print("\n=== Practice Exercises ===")

# Exercise 1: Calculator
num1 = 15
num2 = 4
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} % {num2} = {num1 % num2}")

# Exercise 2: Check if a number is even or odd
print("\nEven/Odd check:")
for num in [1, 2, 3, 4, 5]:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# Exercise 3: Calculate tip
bill = 85.50
tip_percentage = 15
tip = bill * (tip_percentage / 100)
total = bill + tip
print(f"\nBill: ${bill:.2f}")
print(f"Tip ({tip_percentage}%): ${tip:.2f}")
print(f"Total: ${total:.2f}")

# Exercise 4: Find the average of scores
scores = [92, 85, 78, 90, 88]
average = sum(scores) / len(scores)
print(f"\nAverage score: {average:.1f}")

# Exercise 5: Count down from 10
print("\nCountdown:")
for i in range(10, 0, -1):
    print(i, end=" ")
print("Liftoff!")
