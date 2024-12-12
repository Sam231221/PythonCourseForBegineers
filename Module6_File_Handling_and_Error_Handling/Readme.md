# File Handling

File handling in Python is a way to perform operations like creating, reading, writing, and manipulating files. Python provides built-in functions to make file handling simple and efficient.

Here’s a detailed explanation:

---

### **1. Opening a File**

The `open()` function is used to open a file. It returns a file object and takes two main arguments:

- **File name** (string): Path to the file.
- **Mode** (string): Specifies the purpose (e.g., reading, writing).

#### Modes:

| Mode   | Description                                                        |
| ------ | ------------------------------------------------------------------ |
| `'r'`  | Read-only mode (default). File must exist.                         |
| `'w'`  | Write mode. Overwrites the file if it exists or creates a new one. |
| `'a'`  | Append mode. Adds content at the end of the file.                  |
| `'r+'` | Read and write. File must exist.                                   |
| `'w+'` | Write and read. Overwrites if file exists.                         |
| `'a+'` | Append and read. File is created if it doesn't exist.              |

Example:

```python
file = open("example.txt", "r")
```

---

### **2. Reading Files**

You can read file content using:

- `read()`: Reads the entire file as a string.
- `readline()`: Reads one line at a time.
- `readlines()`: Returns all lines as a list of strings.

Example:

```python
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

Reading line-by-line:

```python
file = open("example.txt", "r")
for line in file:
    print(line.strip())  # Removes extra newline characters
file.close()
```

---

### **3. Writing to Files**

You can write content using the `write()` method. Ensure the file is opened in write (`'w'`) or append (`'a'`) mode.

Example:

```python
file = open("example.txt", "w")
file.write("Hello, world!")
file.close()
```

Appending:

```python
file = open("example.txt", "a")
file.write("\nAppending new content.")
file.close()
```

---

### **4. Closing Files**

Always close files after performing operations to free up system resources. Use `file.close()`.

Alternatively, you can use the `with` statement, which automatically closes the file:

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here.
```

---

### **5. Working with Binary Files**

For non-text files like images or PDFs, use binary modes:

- `'rb'`: Read binary.
- `'wb'`: Write binary.

Example:

```python
with open("image.jpg", "rb") as file:
    data = file.read()
    print(data[:10])  # Prints first 10 bytes
```

---

### **6. File Operations**

You can perform additional operations using the `os` and `shutil` modules:

- **Check if a file exists**: `os.path.exists()`
- **Delete a file**: `os.remove()`
- **Rename a file**: `os.rename()`
- **Copy a file**: `shutil.copy()`

Example:

```python
import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
else:
    print("File does not exist.")
```

---

### **7. Error Handling**

Always handle exceptions to avoid crashes when working with files.

Example:

```python
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
```

---

### Summary:

- Use `open()` to access files with the appropriate mode.
- Always close the file or use `with` for automatic cleanup.
- Use error handling for safe operations.

---

# Error Handling

Error handling in Python is a process of managing exceptions that occur during program execution to maintain program stability and improve user experience. Python uses a structured approach to handle errors and exceptions using the `try`, `except`, `else`, and `finally` blocks.

---

### **Error Handling Keywords in Python**

1. **`try` Block**

   - Code that might raise an exception is written inside the `try` block.

2. **`except` Block**

   - Specifies how to handle specific exceptions.
   - Runs only when an exception occurs in the `try` block.

3. **`else` Block**

   - Optional block that executes if no exceptions occur.

4. **`finally` Block**
   - Optional block that always executes, regardless of whether an exception occurred or not.
   - Useful for cleanup actions like closing files or releasing resources.

---

### **Basic Syntax**

```python
try:
    # Code that might raise an exception
    risky_operation()
except ExceptionType as e:
    # Code to handle the exception
    print(f"An error occurred: {e}")
else:
    # Code to run if no exceptions occur
    print("Operation was successful.")
finally:
    # Code that always executes
    print("Execution completed.")
```

---

### **Common Scenarios**

1. **Catching a Specific Exception**

   ```python
   try:
       result = 10 / 0
   except ZeroDivisionError:
       print("Cannot divide by zero!")
   ```

2. **Catching Multiple Exceptions**

   ```python
   try:
       num = int("abc")
   except ValueError:
       print("Invalid number format!")
   except TypeError:
       print("Type error occurred!")
   ```

3. **Catching All Exceptions**

   ```python
   try:
       risky_operation()
   except Exception as e:
       print(f"An unexpected error occurred: {e}")
   ```

4. **Using `else` and `finally`**
   ```python
   try:
       with open("file.txt", "r") as file:
           content = file.read()
   except FileNotFoundError:
       print("The file does not exist.")
   else:
       print("File read successfully.")
   finally:
       print("Finished attempting to read the file.")
   ```

---

### **Raising Exceptions**

Use the `raise` keyword to explicitly raise exceptions.

```python
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older.")
    return "Access granted!"

try:
    print(check_age(16))
except ValueError as e:
    print(e)
```

---

### **Custom Exceptions**

You can define your own exception classes by inheriting from the `Exception` base class.

```python
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    raise CustomError("This is a custom error!")
except CustomError as e:
    print(e)
```

---

### **Best Practices for Error Handling**

1. **Be Specific with Exceptions**: Handle only the exceptions you expect to occur.

   ```python
   try:
       risky_operation()
   except KeyError:
       print("Key not found!")
   ```

2. **Avoid Catching All Exceptions**: Do not use a bare `except:` unless absolutely necessary.

   ```python
   # Avoid this unless necessary:
   try:
       risky_operation()
   except:
       print("Something went wrong!")
   ```

3. **Use `finally` for Cleanup**: Ensure critical cleanup tasks are performed.

   ```python
   try:
       connection = db.connect()
   finally:
       connection.close()
   ```

4. **Log Exceptions**: Instead of just printing errors, log them for debugging.

   ```python
   import logging

   try:
       risky_operation()
   except Exception as e:
       logging.error(f"An error occurred: {e}")
   ```

5. **Do Not Suppress Exceptions Silently**: Always inform the user or developer about issues.
   ```python
   try:
       risky_operation()
   except Exception:
       pass  # Bad practice
   ```

---

### **Common Built-In Exceptions**

| Exception           | Description                                                                        |
| ------------------- | ---------------------------------------------------------------------------------- |
| `ValueError`        | Raised when a function gets an argument of the right type but inappropriate value. |
| `TypeError`         | Raised when an operation is performed on an inappropriate type.                    |
| `KeyError`          | Raised when a dictionary key is not found.                                         |
| `IndexError`        | Raised when a sequence index is out of range.                                      |
| `FileNotFoundError` | Raised when a file or directory is requested but doesn’t exist.                    |
| `ZeroDivisionError` | Raised when dividing by zero.                                                      |
| `AttributeError`    | Raised when an attribute reference or assignment fails.                            |

---
