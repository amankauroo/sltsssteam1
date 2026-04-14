# ============================================================
# 13. ERROR HANDLING (TRY/EXCEPT)
# ============================================================
# When something goes wrong, Python "raises an exception" (throws an error).
# If not handled, your program crashes.

import traceback

# ------------------------------------------------------------
# WHAT ARE EXCEPTIONS?
# ------------------------------------------------------------
print("=== What Are Exceptions? ===")

# Without error handling, errors crash the program
# result = 10 / 0  # This would crash with ZeroDivisionError!

# Common exception types demonstrated:
print("Common exception types:")
print("  ZeroDivisionError: 10 / 0")
print("  ValueError: int('hello')")
print("  TypeError: 'hello' + 5")
print("  KeyError: dict['missing_key']")
print("  IndexError: list[999]")
print("  FileNotFoundError: open('missing.txt')")

# ------------------------------------------------------------
# BASIC TRY-EXCEPT
# ------------------------------------------------------------
print("\n=== Basic Try-Except ===")

# Basic try-except
try:
    # Code that might fail
    result = 10 / 0
except:
    # What to do if it fails
    print("Oops! Something went wrong")
    result = 0

print(f"Result: {result}")

# ------------------------------------------------------------
# CATCHING SPECIFIC ERRORS
# ------------------------------------------------------------
print("\n=== Catching Specific Errors ===")

# Catch specific error type
try:
    number = int("not a number")
except ValueError:
    print("ValueError: That's not a valid number!")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError: Can't divide by zero!")

# Why catch specific errors?
# - You know exactly what went wrong
# - You can handle different errors differently
# - You don't accidentally hide other bugs

# ------------------------------------------------------------
# MULTIPLE EXCEPT BLOCKS
# ------------------------------------------------------------
print("\n=== Multiple Except Blocks ===")


def process_input(user_input, divisor):
    try:
        number = int(user_input)      # Could raise ValueError
        result = 100 / divisor         # Could raise ZeroDivisionError
        return result
    except ValueError:
        print("  ValueError: Not a valid number!")
        return None
    except ZeroDivisionError:
        print("  ZeroDivisionError: Can't divide by zero!")
        return None
    except Exception as e:
        # Catch any OTHER error
        print(f"  Unexpected error: {e}")
        return None


print("Testing process_input:")
print(f"  Result 1: {process_input('abc', 1)}")  # ValueError
print(f"  Result 2: {process_input('10', 0)}")   # ZeroDivisionError
print(f"  Result 3: {process_input('10', 2)}")   # Works!

# ------------------------------------------------------------
# THE 'AS' KEYWORD
# ------------------------------------------------------------
print("\n=== The 'as' Keyword ===")

# Get information about the error
try:
    result = 10 / 0
except ZeroDivisionError as error:
    print(f"Error type: {type(error).__name__}")
    print(f"Error message: {error}")

# Useful for logging or displaying error details
try:
    data = {"name": "Alice"}
    print(data["age"])
except KeyError as e:
    print(f"KeyError - Missing key: {e}")

# ------------------------------------------------------------
# TRY-EXCEPT-ELSE
# ------------------------------------------------------------
print("\n=== Try-Except-Else ===")

# The else block runs only if NO error occurred


def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("  Error: Cannot divide by zero")
        return None
    else:
        # Only runs if try succeeded
        print(f"  Success: {a} / {b} = {result}")
        return result


print("Testing safe_divide:")
safe_divide(10, 2)   # Success
safe_divide(10, 0)   # Error

# ------------------------------------------------------------
# FINALLY BLOCK
# ------------------------------------------------------------
print("\n=== Finally Block ===")

# Code that runs no matter what (success or error)


def demo_finally(value):
    try:
        result = 10 / value
        print(f"  Result: {result}")
    except ZeroDivisionError:
        print("  Error: Division by zero!")
    finally:
        # This ALWAYS runs
        print("  Cleanup: This always executes!")


print("With value = 2:")
demo_finally(2)

print("\nWith value = 0:")
demo_finally(0)

# ------------------------------------------------------------
# RAISING EXCEPTIONS
# ------------------------------------------------------------
print("\n=== Raising Exceptions ===")

# You can create your own errors


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Caught our custom error: {e}")

# Raise with validation


def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    return age


try:
    set_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")

# ------------------------------------------------------------
# CREATING CUSTOM EXCEPTIONS
# ------------------------------------------------------------
print("\n=== Custom Exceptions ===")

# Define your own exception class


class InsufficientFundsError(Exception):
    """Raised when bank account has insufficient funds."""
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw ${amount}. Balance: ${self.balance}"
            )
        self.balance -= amount
        return amount


# Use it
account = BankAccount(100)
try:
    account.withdraw(200)
except InsufficientFundsError as e:
    print(f"Custom exception: {e}")

# ------------------------------------------------------------
# COMMON PATTERNS
# ------------------------------------------------------------
print("\n=== Common Patterns ===")

# Pattern 1: Default value on error


def safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


print("Pattern 1 - safe_int:")
print(f"  safe_int('42') = {safe_int('42')}")
print(f"  safe_int('hello') = {safe_int('hello')}")
print(f"  safe_int('100', -1) = {safe_int('100', -1)}")

# Pattern 2: Log and continue


def risky_operation(value):
    try:
        return 10 / value
    except Exception:
        print("  Error occurred, but continuing...")
        # traceback.print_exc()  # Uncomment to see full traceback
        return None


print("\nPattern 2 - Log and continue:")
result = risky_operation(0)
print(f"  Continuing after error, result = {result}")

# Pattern 3: Safe dictionary access


def get_value(dictionary, key, default="Not found"):
    try:
        return dictionary[key]
    except KeyError:
        return default


print("\nPattern 3 - Safe dictionary access:")
data = {"name": "Alice"}
print(f"  get_value(data, 'name') = {get_value(data, 'name')}")
print(f"  get_value(data, 'age') = {get_value(data, 'age')}")

# Pattern 4: Multiple exception types


def flexible_convert(value):
    try:
        return float(value)
    except (ValueError, TypeError) as e:
        print(f"  Cannot convert: {type(e).__name__}")
        return None


print("\nPattern 4 - Multiple exception types:")
print(f"  flexible_convert('3.14') = {flexible_convert('3.14')}")
print(f"  flexible_convert('hello') = {flexible_convert('hello')}")
print(f"  flexible_convert(None) = {flexible_convert(None)}")

# ------------------------------------------------------------
# PRACTICE EXERCISES
# ------------------------------------------------------------
print("\n=== Practice Exercises ===")

# Exercise 1: Safe division


def safe_divide_ex(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


print("Exercise 1 - Safe division:")
print(f"  safe_divide(10, 2) = {safe_divide_ex(10, 2)}")
print(f"  safe_divide(10, 0) = {safe_divide_ex(10, 0)}")

# Exercise 2: Input validation (simulated)


def validate_age(age_str):
    try:
        age = int(age_str)
        if age < 0 or age > 150:
            raise ValueError("Age out of range")
        return age
    except ValueError as e:
        return f"Invalid: {e}"


print("\nExercise 2 - Age validation:")
print(f"  validate_age('25') = {validate_age('25')}")
print(f"  validate_age('abc') = {validate_age('abc')}")
print(f"  validate_age('-5') = {validate_age('-5')}")

# Exercise 3: File reading with error handling


def read_file_safe(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: No permission to read '{filename}'"


print("\nExercise 3 - File reading:")
print(f"  {read_file_safe('nonexistent.txt')}")

# Exercise 4: Dictionary with default


def get_nested_value(data, *keys, default=None):
    try:
        result = data
        for key in keys:
            result = result[key]
        return result
    except (KeyError, TypeError):
        return default


print("\nExercise 4 - Nested dictionary access:")
nested = {"user": {"name": "Alice", "age": 25}}
print(
    f"  get_nested_value(nested, 'user', 'name') = {get_nested_value(nested, 'user', 'name')}")
print(
    f"  get_nested_value(nested, 'user', 'email') = {get_nested_value(nested, 'user', 'email')}")
