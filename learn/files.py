# ============================================================
# 14. WORKING WITH FILES
# ============================================================
# Programs often need to:
# - Save data permanently (logs, settings, user data)
# - Read external data (configurations, input files)
# - Process large amounts of data

import os
import json
import io

# ------------------------------------------------------------
# OPENING AND READING FILES
# ------------------------------------------------------------
print("=== Opening and Reading Files ===")

# Create a sample file for demonstration
sample_content = """Hello, World!
This is line 2.
And this is line 3.
Final line here."""

with open("sample.txt", "w") as f:
    f.write(sample_content)
print("Created sample.txt for demonstration")

# Method 1: Basic way (NOT recommended)
# file = open("sample.txt", "r")  # "r" = read mode
# content = file.read()
# file.close()  # Always close when done!
# ⚠️ Problem: If error occurs, file.close() never runs!

# Method 2: Using 'with' (RECOMMENDED - auto-closes)
print("\nReading entire file:")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# ------------------------------------------------------------
# DIFFERENT WAYS TO READ
# ------------------------------------------------------------
print("\n=== Different Ways to Read ===")

# Read entire file as string
print("1. read() - entire file:")
with open("sample.txt", "r") as file:
    content = file.read()
    print(f"   Total characters: {len(content)}")

# Read all lines into a list
print("\n2. readlines() - list of lines:")
with open("sample.txt", "r") as file:
    lines = file.readlines()  # ['line1\n', 'line2\n', ...]
    for i, line in enumerate(lines):
        print(f"   Line {i}: {line.strip()}")

# Read one line at a time
print("\n3. readline() - one at a time:")
with open("sample.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()
    print(f"   First: {first_line.strip()}")
    print(f"   Second: {second_line.strip()}")

# Iterate directly (BEST for large files)
print("\n4. Iterate directly:")
with open("sample.txt", "r") as file:
    for line in file:
        print(f"   {line.strip()}")

# Read specific number of characters
print("\n5. read(n) - specific characters:")
with open("sample.txt", "r") as file:
    first_10 = file.read(10)
    print(f"   First 10 chars: '{first_10}'")

# ------------------------------------------------------------
# WRITING TO FILES
# ------------------------------------------------------------
print("\n=== Writing to Files ===")

# Write mode ("w") - OVERWRITES the file!
print("Writing with 'w' mode (overwrite):")
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2\n")
print("   Created output.txt with 2 lines")

# Append mode ("a") - ADDS to the end
print("\nAppending with 'a' mode:")
with open("output.txt", "a") as file:
    file.write("This is a new line (appended)\n")
print("   Added line to output.txt")

# Read what we wrote
with open("output.txt", "r") as file:
    print("   Content:")
    print(file.read())

# Write multiple lines at once
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("multiline.txt", "w") as file:
    file.writelines(lines)
print("Created multiline.txt with writelines()")

# Write with print (redirect to file)
with open("print_output.txt", "w") as file:
    print("Hello!", file=file)
    print("World!", file=file)
print("Created print_output.txt using print()")

# ------------------------------------------------------------
# WORKING WITH FILE PATHS
# ------------------------------------------------------------
print("\n=== Working with File Paths ===")

# Get current directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Join paths (works on any OS)
file_path = os.path.join("folder", "subfolder", "file.txt")
print(f"Joined path: {file_path}")

# Check if file exists
print(f"sample.txt exists: {os.path.exists('sample.txt')}")
print(f"nonexistent.txt exists: {os.path.exists('nonexistent.txt')}")

# Check if it's a file or directory
print(f"Is sample.txt a file: {os.path.isfile('sample.txt')}")
print(f"Is current dir a directory: {os.path.isdir('.')}")

# Get file info
print(f"Size of sample.txt: {os.path.getsize('sample.txt')} bytes")
print(
    f"Basename of '/path/to/file.txt': {os.path.basename('/path/to/file.txt')}")
print(
    f"Dirname of '/path/to/file.txt': {os.path.dirname('/path/to/file.txt')}")

# List files in directory
print(f"\nFiles in current directory:")
for f in os.listdir(".")[:5]:  # Show first 5
    print(f"   {f}")

# ------------------------------------------------------------
# WORKING WITH BINARY FILES
# ------------------------------------------------------------
print("\n=== Working with Binary Files ===")

# Write binary file
binary_data = b"Hello binary world!\x00\x01\x02"
with open("binary.bin", "wb") as file:  # "wb" = write binary
    file.write(binary_data)
print("Created binary.bin")

# Read binary file
with open("binary.bin", "rb") as file:  # "rb" = read binary
    data = file.read()
    print(f"Read binary data: {data}")
    print(f"Data length: {len(data)} bytes")

# Copy a file (simple method)


def copy_file(source, destination):
    with open(source, "rb") as src:
        with open(destination, "wb") as dst:
            dst.write(src.read())


copy_file("sample.txt", "sample_copy.txt")
print("Copied sample.txt to sample_copy.txt")

# ------------------------------------------------------------
# IN-MEMORY FILES WITH IO.BYTESIO
# ------------------------------------------------------------
print("\n=== In-Memory Files (io.BytesIO) ===")

# Create an in-memory "file"
memory_file = io.BytesIO()

# Write to it like a file
memory_file.write(b"Hello from memory!")

# Go back to the beginning (like rewinding a tape)
memory_file.seek(0)

# Read from it
content = memory_file.read()
print(f"Read from memory: {content}")

# This is useful when:
# - APIs expect file objects but you have data in memory
# - You want to avoid creating temporary files
# - You're processing data that will be sent elsewhere

# StringIO for text
text_file = io.StringIO()
text_file.write("Hello text!")
text_file.seek(0)
print(f"Read from StringIO: {text_file.read()}")

# ------------------------------------------------------------
# WORKING WITH JSON FILES
# ------------------------------------------------------------
print("\n=== Working with JSON Files ===")

# Write dictionary to JSON file
data = {
    "name": "Alice",
    "age": 25,
    "hobbies": ["reading", "coding"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=2)  # Pretty print with indent
print("Created data.json")

# Read JSON file to dictionary
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(f"Loaded from JSON: {loaded_data}")
    print(f"Name: {loaded_data['name']}")

# ------------------------------------------------------------
# CONTEXT MANAGERS (WITH STATEMENT)
# ------------------------------------------------------------
print("\n=== Context Managers ===")

# The 'with' statement ensures proper cleanup
# Even if an error occurs, the file gets closed

# Multiple files at once
with open("sample.txt", "r") as infile, open("output2.txt", "w") as outfile:
    content = infile.read()
    outfile.write(content.upper())
print("Created output2.txt with uppercase content")

# ------------------------------------------------------------
# CLEANUP DEMONSTRATION FILES
# ------------------------------------------------------------
print("\n=== Cleaning Up Demo Files ===")

# List of files we created
demo_files = [
    "sample.txt", "output.txt", "multiline.txt",
    "print_output.txt", "binary.bin", "sample_copy.txt",
    "data.json", "output2.txt"
]

for filename in demo_files:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Removed: {filename}")

# ------------------------------------------------------------
# PRACTICE EXERCISES
# ------------------------------------------------------------
print("\n=== Practice Exercises ===")

# Exercise 1: Write and read a file
print("Exercise 1 - Write and read:")
with open("test.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Python is fun!")

with open("test.txt", "r") as f:
    print(f.read())

os.remove("test.txt")

# Exercise 2: Count lines in a file


def count_lines(filename):
    with open(filename, "r") as f:
        return len(f.readlines())


# Create temp file for testing
with open("temp.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")
print(f"\nExercise 2 - Line count: {count_lines('temp.txt')}")
os.remove("temp.txt")

# Exercise 3: Save and load JSON settings
print("\nExercise 3 - JSON settings:")
settings = {"volume": 80, "language": "en", "dark_mode": True}

# Save
with open("settings.json", "w") as f:
    json.dump(settings, f, indent=2)

# Load
with open("settings.json", "r") as f:
    loaded = json.load(f)
    print(f"Loaded settings: {loaded}")

os.remove("settings.json")

# Exercise 4: Copy file in chunks (memory efficient)


def copy_large_file(source, dest, chunk_size=8192):
    """Copy file in chunks for memory efficiency"""
    with open(source, "rb") as src:
        with open(dest, "wb") as dst:
            while True:
                chunk = src.read(chunk_size)
                if not chunk:
                    break
                dst.write(chunk)
    return True


print("\nExercise 4 - Chunk copy function defined")
print("   copy_large_file(source, dest, chunk_size=8192)")
