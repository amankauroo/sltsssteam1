# ============================================================
# 10. FUNCTIONS
# ============================================================
# A function is a reusable block of code that does a specific task.
# It's like a recipe you can use over and over.

# ------------------------------------------------------------
# BASIC FUNCTION
# ------------------------------------------------------------
print("=== Basic Functions ===")

# Defining a function


def say_hello():
    print("Hello, World!")


# Calling (using) the function
say_hello()      # Shows: Hello, World!
say_hello()      # Shows: Hello, World! (can call many times)

# ------------------------------------------------------------
# WHY USE FUNCTIONS?
# ------------------------------------------------------------
print("\n=== Why Use Functions ===")

# With functions - reusable!


def print_banner(message):
    print("=" * 40)
    print(message)
    print("=" * 40)


print_banner("Welcome to the program!")
print()
print_banner("Thanks for using the program!")

# ------------------------------------------------------------
# FUNCTIONS WITH PARAMETERS
# ------------------------------------------------------------
print("\n=== Functions with Parameters ===")

# Function with one parameter


def greet(name):
    print(f"Hello, {name}!")


greet("Alice")   # Shows: Hello, Alice!
greet("Bob")     # Shows: Hello, Bob!

# Function with multiple parameters


def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")


add(5, 3)        # Shows: 5 + 3 = 8

# ------------------------------------------------------------
# RETURN VALUES
# ------------------------------------------------------------
print("\n=== Return Values ===")

# Function that returns a value


def add_numbers(a, b):
    return a + b   # Send the result back


result = add_numbers(5, 3)
print(f"add_numbers(5, 3) = {result}")

# You can use the returned value directly
print(f"add_numbers(10, 20) = {add_numbers(10, 20)}")

# Returning multiple values (as a tuple)


def get_name_parts(full_name):
    parts = full_name.split()
    first = parts[0]
    last = parts[-1]
    return first, last  # Returns a tuple


first_name, last_name = get_name_parts("John Doe")
print(f"First: {first_name}, Last: {last_name}")

# Early return (exit function early)


def divide(a, b):
    if b == 0:
        print("Cannot divide by zero!")
        return None  # Exit early
    return a / b


result = divide(10, 0)
print(f"divide(10, 0) = {result}")

result = divide(10, 2)
print(f"divide(10, 2) = {result}")

# ------------------------------------------------------------
# RETURN VS PRINT
# ------------------------------------------------------------
print("\n=== Return vs Print ===")

# print() - just displays, returns None


def greet_print(name):
    print(f"Hello, {name}!")


result1 = greet_print("Alice")
print(f"Return value of greet_print: {result1}")  # None

# return - gives back a value you can use


def greet_return(name):
    return f"Hello, {name}!"


result2 = greet_return("Alice")
print(f"Return value of greet_return: {result2}")
message = result2.upper()  # Can manipulate the returned value!
print(f"Uppercased: {message}")

# ------------------------------------------------------------
# DEFAULT PARAMETERS
# ------------------------------------------------------------
print("\n=== Default Parameters ===")


def greet_with_greeting(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet_with_greeting("Alice")                # Uses default: Hello, Alice!
greet_with_greeting("Bob", "Good morning")  # Good morning, Bob!
greet_with_greeting("Charlie", "Howdy")     # Howdy, Charlie!

# ⚠️ Default parameters must come AFTER non-default parameters


def example(a, b=10, c=20):  # ✅ OK
    print(f"a={a}, b={b}, c={c}")


example(1)
example(1, 2)
example(1, 2, 3)

# ------------------------------------------------------------
# KEYWORD ARGUMENTS
# ------------------------------------------------------------
print("\n=== Keyword Arguments ===")


def describe_pet(name, animal="dog", age=1):
    print(f"{name} is a {age} year old {animal}")


# Positional arguments (order matters)
describe_pet("Buddy")                    # Uses defaults
describe_pet("Whiskers", "cat")          # Override animal
describe_pet("Goldie", "fish", 2)        # Override both

# Keyword arguments (order doesn't matter!)
print("\nWith keyword arguments:")
describe_pet(name="Rex", age=5, animal="dog")
describe_pet(animal="cat", name="Whiskers", age=3)

# Mix positional and keyword (positional must come first)
describe_pet("Buddy", age=5)

# ------------------------------------------------------------
# *ARGS AND **KWARGS
# ------------------------------------------------------------
print("\n=== *args and **kwargs ===")

# *args - accepts any number of positional arguments (as tuple)


def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(f"add_all(1, 2) = {add_all(1, 2)}")
print(f"add_all(1, 2, 3, 4, 5) = {add_all(1, 2, 3, 4, 5)}")

# **kwargs - accepts any number of keyword arguments (as dict)


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


print("\nprint_info with kwargs:")
print_info(name="Alice", age=25, city="NYC")

# Combining all parameter types


def complex_example(required, optional=None, *args, **kwargs):
    print(f"  Required: {required}")
    print(f"  Optional: {optional}")
    print(f"  Args: {args}")
    print(f"  Kwargs: {kwargs}")


print("\ncomplex_example call:")
complex_example("hello", "world", 1, 2, 3, x=10, y=20)

# ------------------------------------------------------------
# SCOPE (VARIABLE VISIBILITY)
# ------------------------------------------------------------
print("\n=== Scope ===")

# Global variable - accessible everywhere
global_var = "I'm global"


def my_function():
    # Local variable - only accessible inside function
    local_var = "I'm local"
    print(f"  Inside function: {global_var}")
    print(f"  Inside function: {local_var}")


my_function()
print(f"Outside function: {global_var}")
# print(local_var)  # ❌ ERROR! local_var doesn't exist here

# To modify a global variable inside a function:
counter = 0


def increment():
    global counter  # Tell Python we want the global one
    counter += 1


increment()
increment()
print(f"Counter after 2 increments: {counter}")

# ------------------------------------------------------------
# LAMBDA FUNCTIONS
# ------------------------------------------------------------
print("\n=== Lambda Functions ===")

# Regular function


def add_regular(a, b):
    return a + b


# Lambda function (same thing, one line)
def add_lambda(a, b): return a + b


print(f"add_regular(5, 3) = {add_regular(5, 3)}")
print(f"add_lambda(5, 3) = {add_lambda(5, 3)}")

# Useful with sorted, map, filter
numbers = [3, 1, 4, 1, 5, 9]

# Sort by custom key
sorted_desc = sorted(numbers, key=lambda x: -x)  # Descending
print(f"\nSorted descending: {sorted_desc}")

# Map: apply function to each element
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled}")

# Filter: keep elements that satisfy condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")

# ------------------------------------------------------------
# DOCSTRINGS
# ------------------------------------------------------------
print("\n=== Docstrings ===")


def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
        length: The length of the rectangle
        width: The width of the rectangle

    Returns:
        The area (length × width)
    """
    return length * width


# Access docstring
print(f"Function docstring:")
print(calculate_area.__doc__)

result = calculate_area(5, 3)
print(f"calculate_area(5, 3) = {result}")

# ------------------------------------------------------------
# PRACTICE EXERCISES
# ------------------------------------------------------------
print("\n=== Practice Exercises ===")

# Exercise 1: Simple function


def square(n):
    return n ** 2


print(f"Exercise 1 - square(5) = {square(5)}")

# Exercise 2: Function with multiple returns


def divide_with_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder


q, r = divide_with_remainder(17, 5)
print(f"\nExercise 2 - 17 ÷ 5 = {q} remainder {r}")

# Exercise 3: Default parameter


def power(base, exponent=2):
    return base ** exponent


print(f"\nExercise 3:")
print(f"  power(3) = {power(3)}")      # 9 (3²)
print(f"  power(2, 10) = {power(2, 10)}")  # 1024 (2¹⁰)

# Exercise 4: Validate input


def is_positive(number):
    return number > 0


print(f"\nExercise 4:")
print(f"  is_positive(5) = {is_positive(5)}")
print(f"  is_positive(-3) = {is_positive(-3)}")

# Exercise 5: Lambda with sorting
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(f"\nExercise 5 - Students sorted by score:")
for name, score in sorted_students:
    print(f"  {name}: {score}")

# Exercise 6: Factorial function


def factorial(n):
    """Calculate n! (factorial of n)"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)  # Recursion!


print(f"\nExercise 6:")
print(f"  5! = {factorial(5)}")  # 120
print(f"  10! = {factorial(10)}")  # 3628800
