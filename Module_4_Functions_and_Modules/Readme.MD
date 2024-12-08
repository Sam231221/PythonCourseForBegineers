### **Functions**

A **function** is a reusable block of code that performs a specific task. Functions are used to reduce code repetition and make programs more modular.

---

#### **Defining Functions**

Functions are defined using the `def` keyword, followed by the function name and parentheses `()`.

Example:

```python
def greet():
    print("Hello, World!")

greet()  # Output: Hello, World!
```

---

#### **Parameters and Return Values**

- **Parameters**: Inputs a function takes to perform its operation.
- **Return Value**: The output a function sends back using the `return` statement.

Example:

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

---

#### **Default and Keyword Arguments**

- **Default Arguments**: Provide default values for parameters if no value is passed.
- **Keyword Arguments**: Pass arguments by explicitly naming them in the function call, allowing flexibility.

Example:

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Output: Hello, Guest!
greet(name="Alice")  # Output: Hello, Alice!
```

---

In Python, `*args` and `**kwargs` are used to pass a variable number of arguments to a function. They provide flexibility in function definitions by allowing you to handle a dynamic number of arguments.

---

### **`*args`**

- Stands for "arguments."
- Allows you to pass **any number of positional arguments** to a function.
- The arguments are stored as a tuple, which means they are ordered and iterable.

#### **When to Use `*args`**

Use `*args` when:

1. You don’t know in advance how many arguments will be passed.
2. You want to iterate over a list of arguments within a function.

#### **Example of `*args`**

```python
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4))  # Output: 10
print(sum_numbers(10, 20))      # Output: 30
```

- Here, `*args` allows the function to accept any number of arguments. These arguments are collected in a tuple.

---

### **`**kwargs`\*\*

- Stands for "keyword arguments."
- Allows you to pass **any number of named (key-value pair) arguments** to a function.
- The arguments are stored as a dictionary, where keys are argument names and values are their corresponding values.

#### **When to Use `**kwargs`\*\*

Use `**kwargs` when:

1. You don’t know in advance which keyword arguments will be passed.
2. You want to handle named arguments dynamically.

#### **Example of `**kwargs`\*\*

```python
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York
```

- Here, `**kwargs` allows the function to accept any number of named arguments. These arguments are collected in a dictionary.

---

### **Using `*args` and `**kwargs` Together\*\*

You can use both `*args` and `**kwargs` in the same function definition to handle both positional and keyword arguments.

#### **Example**

```python
def show_arguments(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

show_arguments(1, 2, 3, name="Alice", age=25)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 25}
```

---

### **Order of `*args` and `**kwargs`\*\*

When defining a function with both `*args` and `**kwargs`, they must appear in this order:

def funtion_name( `*args`, `**kwargs`)
:
Example:

```python
def example_function(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

example_function(1, 2, 3, 4, 5, key1="value1", key2="value2")
# Output:
# 1 2
# (3, 4, 5)
# {'key1': 'value1', 'key2': 'value2'}
```

---

### **Key Differences Between `*args` and `**kwargs`\*\*

| Feature       | `*args`                       | `**kwargs`                          |
| ------------- | ----------------------------- | ----------------------------------- |
| Purpose       | Handles positional arguments  | Handles keyword arguments           |
| Stored as     | Tuple                         | Dictionary                          |
| Usage         | For variable-length arguments | For variable-length named arguments |
| Example Input | `func(1, 2, 3)`               | `func(a=1, b=2, c=3)`               |

---

### **Practical Use Cases**

- **`*args`**: When you need a function to handle lists or tuples of arguments dynamically, such as summing numbers or formatting multiple strings.
- **`**kwargs`\*\*: When you need a function to handle dynamic configuration options or parameters, such as styling UI components or building API requests.

---

By using `*args` and `**kwargs`, you can make your functions more flexible and adaptable for diverse use cases.

---

### **Modules**

A **module** is a Python file containing code (variables, functions, classes) that can be reused in other Python programs. Modules help organize and manage code effectively.

---

#### **Introduction to Modules**

- A module can be a built-in module (provided by Python) or a user-defined module (created by you).
- To use a module, you need to **import** it.

---

#### **Importing Modules**

Modules are imported using the `import` statement. You can:

1. Import the entire module:
   ```python
   import math
   print(math.sqrt(16))  # Output: 4.0
   ```
2. Import specific components:
   ```python
   from math import sqrt
   print(sqrt(16))  # Output: 4.0
   ```
3. Use an alias:
   ```python
   import math as m
   print(m.sqrt(16))  # Output: 4.0
   ```

---

#### **Using Standard Modules**

Python provides a rich library of built-in modules. Here are examples using some commonly used modules:

1. **`math`**: Provides mathematical functions and constants.

   ```python
   import math

   print(math.pi)  # Output: 3.141592653589793
   print(math.factorial(5))  # Output: 120
   ```

2. **`random`**: Used to generate random numbers and perform random operations.

   ```python
   import random

   print(random.randint(1, 10))  # Random integer between 1 and 10
   print(random.choice(['apple', 'banana', 'cherry']))  # Random choice
   ```

3. **`datetime`**: Used to work with dates and times.

   ```python
   from datetime import datetime

   now = datetime.now()
   print(now)  # Current date and time
   print(now.strftime("%Y-%m-%d"))  # Output: 2024-12-08 (example format)
   ```

---

### **User-Defined Modules**

You can create your own module by saving functions and variables in a `.py` file and importing it into another file.

**Example**:
Create a file `my_module.py`:

```python
def greet(name):
    return f"Hello, {name}!"
```

Use it in another file:

```python
import my_module

print(my_module.greet("Alice"))  # Output: Hello, Alice!
```

---

Functions and modules are fundamental for writing clean, organized, and reusable Python code. Together, they enhance productivity and maintainability.
