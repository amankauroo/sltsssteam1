# ============================================================
# 12. IMPORTING LIBRARIES
# ============================================================
# Libraries (also called modules or packages) are collections of
# pre-written code that you can use.

# ------------------------------------------------------------
# BASIC IMPORT
# ------------------------------------------------------------
import importlib.metadata
from random import randint, choice
import time
import random
from datetime import datetime
import os.path
from os import path
import json as j
import math as m
from math import sqrt, pi, ceil
import json
import sys
import os
import math
print("=== Basic Import ===")

# Import an entire library

# Use functions from the library with library.function()
print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"math.pi = {math.pi}")
print(f"math.floor(3.7) = {math.floor(3.7)}")
print(f"math.ceil(3.2) = {math.ceil(3.2)}")

# Import multiple libraries

# ------------------------------------------------------------
# IMPORT SPECIFIC THINGS
# ------------------------------------------------------------
print("\n=== Import Specific Items ===")

# Import just what you need

# No need for "math." prefix
print(f"sqrt(16) = {sqrt(16)}")
print(f"pi = {pi}")
print(f"ceil(3.2) = {ceil(3.2)}")

# Import everything (generally NOT recommended)
# from math import *    # Imports all functions from math
# Why avoid import *?
# - Hard to know where functions came from
# - Can overwrite your own variables
# - Makes code harder to read

# ------------------------------------------------------------
# IMPORT WITH ALIAS
# ------------------------------------------------------------
print("\n=== Import with Alias ===")

# Give a library a shorter name (alias)

# Now use the short name
print(f"m.sqrt(25) = {m.sqrt(25)}")

# Common aliases you'll see:
# numpy → np
# pandas → pd
# matplotlib.pyplot → plt
# tensorflow → tf

# Example (these need to be installed):
# import numpy as np
# import pandas as pd

# ------------------------------------------------------------
# IMPORT FROM SUBMODULES
# ------------------------------------------------------------
print("\n=== Import from Submodules ===")

# Some libraries have submodules (sub-libraries)

print(f"os.path.exists('importing.py') = {path.exists('importing.py')}")

# You can also import the module directly
print(f"os.path.dirname('/a/b/c.txt') = {os.path.dirname('/a/b/c.txt')}")

# ------------------------------------------------------------
# COMMON STANDARD LIBRARIES
# ------------------------------------------------------------
print("\n=== Common Standard Libraries ===")

# MATH - Mathematical functions
print(f"\nMATH:")
print(f"  math.sqrt(16) = {math.sqrt(16)}")
print(f"  math.pi = {math.pi:.4f}")
print(f"  math.floor(3.7) = {math.floor(3.7)}")
print(f"  math.ceil(3.2) = {math.ceil(3.2)}")

# OS - Operating system interaction
print(f"\nOS:")
print(f"  os.getcwd() = {os.getcwd()}")
print(f"  os.name = {os.name}")

# SYS - System-specific parameters
print(f"\nSYS:")
print(f"  sys.version = {sys.version.split()[0]}")
print(f"  sys.platform = {sys.platform}")

# JSON - Work with JSON data
print(f"\nJSON:")
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)  # Convert to JSON string
print(f"  json.dumps(data) = {json_string}")
back_to_dict = json.loads(json_string)  # Convert back
print(f"  json.loads() = {back_to_dict}")

# DATETIME - Dates and times
print(f"\nDATETIME:")
now = datetime.now()
print(f"  datetime.now() = {now.strftime('%Y-%m-%d %H:%M:%S')}")

# RANDOM - Random numbers
print(f"\nRANDOM:")
print(f"  random.randint(1, 10) = {random.randint(1, 10)}")
print(f"  random.choice(['a', 'b', 'c']) = {random.choice(['a', 'b', 'c'])}")

# TIME - Time-related functions
print(f"\nTIME:")
print(f"  time.time() = {time.time():.0f} (Unix timestamp)")
# time.sleep(1)  # Wait 1 second (commented to avoid delay)

# ------------------------------------------------------------
# CHECKING IF LIBRARY IS INSTALLED
# ------------------------------------------------------------
print("\n=== Checking if Library is Installed ===")

# Method 1: Try to import it
try:
    import requests
    print("requests is installed!")
except ImportError:
    print("requests is NOT installed. Run: pip install requests")

try:
    import numpy
    print(f"numpy is installed! Version: {numpy.__version__}")
except ImportError:
    print("numpy is NOT installed. Run: pip install numpy")

# Method 2: Check version (if imported)
print(f"\nVersion checking:")
# Most modules don't have __version__, but some do
# print(json.__version__)  # Would error for json

# ------------------------------------------------------------
# CREATING YOUR OWN MODULE
# ------------------------------------------------------------
print("\n=== Creating Your Own Module ===")

# You can create your own module by saving functions in a .py file
# Then import it like any other module

# Example: If you have mymodule.py with:
# def greet(name):
#     return f"Hello, {name}!"

# You can use it:
# import mymodule
# print(mymodule.greet("Alice"))

# Or:
# from mymodule import greet
# print(greet("Alice"))

print("To create a module:")
print("1. Create a .py file (e.g., mymodule.py)")
print("2. Add functions/classes to it")
print("3. Import it in other files")

# ------------------------------------------------------------
# __NAME__ == '__MAIN__' PATTERN
# ------------------------------------------------------------
print("\n=== __name__ == '__main__' Pattern ===")

# This pattern is used to make code run only when the file
# is run directly, not when imported


def main():
    print("This runs when the file is executed directly")

# When a file is run directly, __name__ is set to '__main__'
# When a file is imported, __name__ is set to the module name


print(f"__name__ in this file: {__name__}")

if __name__ == "__main__":
    # This code only runs if this file is executed directly
    # It won't run if this file is imported as a module
    print("File is being run directly!")
    # main()

# ------------------------------------------------------------
# PRACTICE EXERCISES
# ------------------------------------------------------------
print("\n=== Practice Exercises ===")

# Exercise 1: Import and use math library
radius = 5
area = math.pi * radius ** 2
print(f"Exercise 1 - Circle area (r={radius}): {area:.2f}")

# Exercise 2: Import specific functions
print(f"\nExercise 2:")
print(f"  Random int 1-100: {randint(1, 100)}")
colors = ["red", "green", "blue"]
print(f"  Random color: {choice(colors)}")

# Exercise 3: Check current directory
print(f"\nExercise 3:")
print(f"  Current directory: {os.getcwd()}")

# Exercise 4: Work with JSON
person = {"name": "Alice", "age": 25, "city": "NYC"}
json_str = json.dumps(person, indent=2)
print(f"\nExercise 4 - JSON:")
print(json_str)

# Exercise 5: Get current date/time
now = datetime.now()
print(f"\nExercise 5:")
print(f"  Current time: {now.strftime('%H:%M:%S')}")
print(f"  Today's date: {now.strftime('%B %d, %Y')}")

# Exercise 6: List comprehension with random
random_numbers = [random.randint(1, 100) for _ in range(5)]
print(f"\nExercise 6 - 5 random numbers: {random_numbers}")

# ------------------------------------------------------------
# WORKING WITH PACKAGES (PIP)
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("=== Working with Packages (pip) ===")
print("=" * 50)

# pip is Python's package installer
# Use it in the terminal (not in Python code)

print("""
INSTALLING PACKAGES:
--------------------
pip install package_name          # Install a package
pip install numpy                 # Example: install numpy
pip install pandas==2.0.0         # Install specific version
pip install "pandas>=2.0.0"       # Install minimum version
pip install package1 package2     # Install multiple packages

UNINSTALLING PACKAGES:
----------------------
pip uninstall package_name        # Remove a package
pip uninstall numpy               # Example: remove numpy

LISTING PACKAGES:
-----------------
pip list                          # Show all installed packages
pip show package_name             # Show details about a package
pip show numpy                    # Example: show numpy info

UPGRADING PACKAGES:
-------------------
pip install --upgrade package_name   # Upgrade to latest
pip install -U numpy                 # Short form
pip install --upgrade pip            # Upgrade pip itself

SEARCHING PACKAGES:
-------------------
pip search is deprecated, use https://pypi.org instead
""")

# ------------------------------------------------------------
# REQUIREMENTS.TXT
# ------------------------------------------------------------
print("\n=== requirements.txt ===")
print("""
A requirements.txt file lists all packages your project needs.
This makes it easy to share and reproduce your environment.

CREATING requirements.txt:
--------------------------
pip freeze > requirements.txt     # Export all installed packages

EXAMPLE requirements.txt file:
------------------------------
numpy==1.24.0
pandas>=2.0.0
requests
opencv-python
google-genai>=1.0.0

INSTALLING FROM requirements.txt:
---------------------------------
pip install -r requirements.txt   # Install all packages listed

BEST PRACTICE:
--------------
1. Create requirements.txt for every project
2. Include version numbers for reproducibility
3. Update it when you add new packages
""")

# Example: Reading requirements.txt programmatically
print("Example - Parse requirements.txt:")
example_requirements = """numpy==1.24.0
pandas>=2.0.0
requests
opencv-python"""

for line in example_requirements.strip().split('\n'):
    if line and not line.startswith('#'):
        print(f"  Package: {line}")

# ------------------------------------------------------------
# VIRTUAL ENVIRONMENTS
# ------------------------------------------------------------
print("\n=== Virtual Environments ===")
print("""
Virtual environments isolate your project's packages from
other projects. This prevents version conflicts!

WHY USE VIRTUAL ENVIRONMENTS:
-----------------------------
• Project A needs numpy 1.20
• Project B needs numpy 2.0
• Without venv, they would conflict!
• With venv, each project has its own numpy

CREATING A VIRTUAL ENVIRONMENT:
-------------------------------
python -m venv venv_name          # Create a virtual environment
python -m venv .venv              # Common: name it .venv

ACTIVATING THE ENVIRONMENT:
---------------------------
Windows:   .venv\\Scripts\\activate
Mac/Linux: source .venv/bin/activate

DEACTIVATING:
-------------
deactivate                        # Exit the virtual environment

TYPICAL WORKFLOW:
-----------------
1. python -m venv .venv           # Create environment
2. .venv\\Scripts\\activate        # Activate it (Windows)
3. pip install -r requirements.txt # Install packages
4. python main.py                 # Run your code
5. deactivate                     # When done
""")

# ------------------------------------------------------------
# CHECKING PACKAGE INFO PROGRAMMATICALLY
# ------------------------------------------------------------
print("\n=== Package Info Programmatically ===")


# Get list of installed packages
print("Some installed packages:")
installed_packages = []
try:
    # Get all installed distributions
    for dist in importlib.metadata.distributions():
        installed_packages.append(dist.metadata['Name'])
except Exception:
    pass

# Show first 10 packages (sorted)
for pkg in sorted(installed_packages)[:10]:
    print(f"  - {pkg}")

print(f"  ... and {len(installed_packages) - 10} more")

# Get info about a specific package
print("\nPackage details example:")
try:
    pkg_name = "pip"
    version = importlib.metadata.version(pkg_name)
    print(f"  {pkg_name} version: {version}")
except importlib.metadata.PackageNotFoundError:
    print(f"  {pkg_name} not found")

# ------------------------------------------------------------
# USEFUL PACKAGE CATEGORIES
# ------------------------------------------------------------
print("\n=== Useful Package Categories ===")
print("""
DATA SCIENCE:
  numpy       - Fast arrays and math
  pandas      - Data analysis
  matplotlib  - Plotting/charts
  scipy       - Scientific computing

MACHINE LEARNING:
  scikit-learn - ML algorithms
  tensorflow   - Deep learning
  pytorch      - Deep learning
  keras        - Neural networks

WEB DEVELOPMENT:
  flask        - Lightweight web framework
  django       - Full web framework
  fastapi      - Modern API framework
  requests     - HTTP requests

IMAGE/VIDEO:
  pillow       - Image processing
  opencv-python - Computer vision
  
AUDIO:
  pyaudio      - Audio I/O
  pydub        - Audio manipulation

UTILITIES:
  python-dotenv - Environment variables
  tqdm         - Progress bars
  colorama     - Colored terminal output
""")

# ------------------------------------------------------------
# ENVIRONMENT VARIABLES WITH DOTENV
# ------------------------------------------------------------
print("\n=== Environment Variables (Best Practice) ===")
print("""
Never put sensitive data (API keys, passwords) in code!
Use environment variables instead.

METHOD 1: .env file with python-dotenv
--------------------------------------
1. pip install python-dotenv
2. Create .env file:
   API_KEY=your_secret_key_here
   DATABASE_URL=postgres://...
   
3. In your Python code:
   from dotenv import load_dotenv
   import os
   
   load_dotenv()  # Load .env file
   api_key = os.getenv('API_KEY')

METHOD 2: System environment variables
--------------------------------------
Windows: set API_KEY=your_key
Mac/Linux: export API_KEY=your_key

Then in Python:
   import os
   api_key = os.environ.get('API_KEY')

IMPORTANT: Add .env to .gitignore!
""")

# Example: Reading environment variables
print("Current environment variables (sample):")
print(f"  PATH exists: {'PATH' in os.environ}")
print(
    f"  HOME/USERPROFILE: {os.environ.get('HOME', os.environ.get('USERPROFILE', 'Not set'))}")
