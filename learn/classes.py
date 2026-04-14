# ============================================================
# 11. CLASSES AND OBJECTS
# ============================================================
# A class is like a blueprint for creating objects.
# Think of it like:
# - Class = Blueprint for a house
# - Object = An actual house built from that blueprint

# ------------------------------------------------------------
# BASIC CLASS
# ------------------------------------------------------------
print("=== Basic Class ===")

# Define a class (the blueprint)


class Dog:
    pass  # Empty class for now


# Create objects (instances) from the class
my_dog = Dog()
another_dog = Dog()

print(f"my_dog: {my_dog}")
print(f"another_dog: {another_dog}")
print("(Different memory addresses = different objects!)")

# ------------------------------------------------------------
# THE __INIT__ METHOD (CONSTRUCTOR)
# ------------------------------------------------------------
print("\n=== The __init__ Method ===")


class Dog:
    def __init__(self, name, age):
        # 'self' refers to this specific dog being created
        self.name = name    # Store the name
        self.age = age      # Store the age


# Create dogs with different names and ages
dog1 = Dog("Buddy", 3)   # __init__ runs with name="Buddy", age=3
dog2 = Dog("Max", 5)     # __init__ runs with name="Max", age=5

print(f"dog1.name = {dog1.name}")
print(f"dog2.name = {dog2.name}")
print(f"dog1.age = {dog1.age}")
print(f"dog2.age = {dog2.age}")

# ------------------------------------------------------------
# CONSTRUCTOR WITH DEFAULT VALUES
# ------------------------------------------------------------
print("\n=== Constructor with Defaults ===")


class User:
    def __init__(self, username, email, role="member"):
        self.username = username
        self.email = email
        self.role = role


# Create with default role
user1 = User("alice", "alice@example.com")
print(f"user1.role = {user1.role}")  # member

# Create with custom role
admin = User("bob", "bob@example.com", "admin")
print(f"admin.role = {admin.role}")  # admin

# ------------------------------------------------------------
# WHAT IS 'SELF'?
# ------------------------------------------------------------
print("\n=== Understanding 'self' ===")


class Dog:
    def __init__(self, name):
        self.name = name    # "MY name" for this specific dog

    def bark(self):
        # self.name refers to THIS dog's name
        print(f"{self.name} says: Woof!")

    def introduce(self):
        print(f"Hi, I'm {self.name}!")


dog1 = Dog("Buddy")
dog2 = Dog("Max")

dog1.bark()       # Buddy says: Woof!
dog2.bark()       # Max says: Woof!
dog1.introduce()  # Hi, I'm Buddy!

# ------------------------------------------------------------
# METHODS (FUNCTIONS IN A CLASS)
# ------------------------------------------------------------
print("\n=== Methods ===")


class Calculator:
    def __init__(self):
        self.result = 0   # Start with 0

    def add(self, number):
        self.result = self.result + number
        return self       # Return self for chaining

    def subtract(self, number):
        self.result = self.result - number
        return self

    def multiply(self, number):
        self.result = self.result * number
        return self

    def reset(self):
        self.result = 0
        return self

    def get_result(self):
        return self.result


# Using the calculator
calc = Calculator()
calc.add(10)
calc.subtract(3)
print(f"10 - 3 = {calc.get_result()}")

# Method chaining (because methods return self)
calc.reset().add(5).multiply(3).subtract(2)
print(f"5 * 3 - 2 = {calc.get_result()}")

# ------------------------------------------------------------
# INSTANCE VS CLASS VARIABLES
# ------------------------------------------------------------
print("\n=== Instance vs Class Variables ===")


class Dog:
    # CLASS VARIABLE - shared by ALL dogs
    species = "Canis lupus familiaris"
    dog_count = 0

    def __init__(self, name, age):
        # INSTANCE VARIABLES - unique to each dog
        self.name = name
        self.age = age
        Dog.dog_count += 1  # Increment class variable


# Create dogs
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Instance variables are different
print(f"dog1.name = {dog1.name}")
print(f"dog2.name = {dog2.name}")

# Class variables are shared
print(f"dog1.species = {dog1.species}")
print(f"dog2.species = {dog2.species}")
print(f"Dog.dog_count = {Dog.dog_count}")

# ------------------------------------------------------------
# PRACTICAL EXAMPLE: BANK ACCOUNT
# ------------------------------------------------------------
print("\n=== Bank Account Example ===")


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            print(f"Deposited ${amount}. New balance: ${self.balance}")
            return True
        print("Invalid deposit amount!")
        return False

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
            return False
        if amount > self.balance:
            print("Insufficient funds!")
            return False
        self.balance -= amount
        self.transactions.append(f"Withdrawal: -${amount}")
        print(f"Withdrew ${amount}. New balance: ${self.balance}")
        return True

    def get_balance(self):
        return self.balance

    def print_statement(self):
        print(f"\n=== Statement for {self.owner} ===")
        for t in self.transactions:
            print(f"  {t}")
        print(f"Current Balance: ${self.balance}")
        print("=" * 30)


# Create accounts
alice = BankAccount("Alice", 100)
bob = BankAccount("Bob", 50)

# Transactions
alice.deposit(50)
alice.withdraw(30)
bob.withdraw(100)  # Insufficient funds!

alice.print_statement()

# ------------------------------------------------------------
# PRIVATE ATTRIBUTES (CONVENTION)
# ------------------------------------------------------------
print("\n=== Private Attributes ===")


class User:
    def __init__(self, username, password):
        self.username = username      # Public
        self._email = None            # "Protected" (single underscore)
        self.__password = password    # "Private" (double underscore)

    def set_password(self, new_password):
        if len(new_password) >= 8:
            self.__password = new_password
            return True
        return False

    def verify_password(self, password):
        return self.__password == password


user = User("alice", "secret123")
print(f"user.username = {user.username}")  # Public - accessible
# Protected - accessible but shouldn't use
print(f"user._email = {user._email}")
# print(user.__password)  # Error! Private - not directly accessible
print(
    f"user.verify_password('secret123') = {user.verify_password('secret123')}")

# ------------------------------------------------------------
# STATIC AND CLASS METHODS
# ------------------------------------------------------------
print("\n=== Static and Class Methods ===")


class MathUtils:
    # Static method - doesn't need self or cls
    @staticmethod
    def add(a, b):
        return a + b

    # Class method - gets the class as first argument
    @classmethod
    def describe(cls):
        return f"This is the {cls.__name__} class"


# Call without creating an object
print(f"MathUtils.add(5, 3) = {MathUtils.add(5, 3)}")
print(f"MathUtils.describe() = {MathUtils.describe()}")

# ------------------------------------------------------------
# INHERITANCE
# ------------------------------------------------------------
print("\n=== Inheritance ===")

# Parent class (base class)


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

    def move(self):
        print(f"{self.name} moves")

# Child class (inherits from Animal)


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call parent's __init__
        self.color = color

    def speak(self):  # Override parent's method
        print(f"{self.name} says: Meow!")

    def purr(self):  # New method specific to Cat
        print(f"{self.name} purrs")

# Child class


class Dog(Animal):
    def speak(self):  # Override parent's method
        print(f"{self.name} says: Woof!")


# Using inheritance
cat = Cat("Whiskers", "orange")
dog = Dog("Buddy")

cat.speak()   # Meow! (overridden)
cat.move()    # moves (inherited)
cat.purr()    # purrs (cat-specific)
print(f"cat.color = {cat.color}")

dog.speak()   # Woof! (overridden)
dog.move()    # moves (inherited)

# ------------------------------------------------------------
# PRACTICE EXERCISES
# ------------------------------------------------------------
print("\n=== Practice Exercises ===")

# Exercise 1: Simple class


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rect = Rectangle(5, 3)
print(f"Exercise 1:")
print(f"  Area: {rect.area()}")
print(f"  Perimeter: {rect.perimeter()}")

# Exercise 2: Class with state tracking


class Counter:
    def __init__(self, start=0):
        self.value = start

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def reset(self):
        self.value = 0


counter = Counter()
counter.increment()
counter.increment()
counter.increment()
print(f"\nExercise 2 - Counter value: {counter.value}")

# Exercise 3: Student class


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


student = Student("Alice")
student.add_grade(85)
student.add_grade(90)
student.add_grade(78)
print(f"\nExercise 3 - {student.name}'s average: {student.average():.1f}")
