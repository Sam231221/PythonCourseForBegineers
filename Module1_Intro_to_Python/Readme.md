# Module 1: Introduction to Python

## What is Python?

Python is a high-level, interpreted programming language known for its simplicity and versatility. It is widely used in various fields, including web development, data science, artificial intelligence, automation, and more.

### Key Features of Python:

- Easy to learn and read (simple syntax similar to English)
- Open-source and community-driven
- Extensive libraries and frameworks for almost every task
- Platform-independent (works on Windows, Mac, Linux, etc.)
- Supports multiple programming paradigms: procedural, object-oriented, and functional

---

## Top Companies Using Python

Python’s simplicity, versatility, and rich ecosystem have made it a favorite choice for companies across industries. Here are some top companies that use Python extensively:

1. **Google**
2. **Netflix**
3. **Instagram**
4. **Spotify**
5. **Dropbox**
6. **NASA**
7. **Facebook (Meta)**
8. **Amazon**

---

## Applications of Python

Python's flexibility allows it to be used in nearly every field of technology. Below are some of its key applications:

### 1. **Web Development**

- Python provides frameworks like **Django**, **Flask**, and **FastAPI** for building scalable and robust web applications.
- Examples:
  - Social media platforms like Instagram.
  - E-commerce websites like Shopify.

### 2. **Data Science and Analytics**

- Python dominates the data science space with libraries like **Pandas**, **NumPy**, and **Matplotlib** for data manipulation and visualization.
- Examples:
  - Analyzing user behavior on platforms like Spotify.
  - Business intelligence dashboards.

### 3. **Artificial Intelligence (AI) and Machine Learning (ML)**

- Python offers popular libraries like **TensorFlow**, **PyTorch**, **scikit-learn**, and **Keras** for developing AI and ML models.
- Examples:
  - Recommendation systems (Netflix, Amazon).
  - Self-driving car algorithms (Tesla).

### 4. **Automation and Scripting**

- Python is widely used for automating repetitive tasks, such as file handling, web scraping, and testing.
- Tools like **Selenium** and **BeautifulSoup** make automation simple and efficient.
- Examples:
  - Automating email responses.
  - Scraping data from websites.

### 5. **Game Development**

- Libraries like **Pygame** allow developers to create 2D games.
- Examples:
  - Simple indie games.
  - Prototypes for larger game engines.

### 6. **Scientific Computing**

- Python’s libraries like **SciPy** and **SymPy** are used for simulations, complex calculations, and solving mathematical problems.
- Examples:
  - Analyzing large datasets in physics.
  - Computational biology research.

### 7. **Internet of Things (IoT)**

- Python runs on microcontrollers like Raspberry Pi, making it ideal for IoT projects.
- Examples:
  - Smart home devices.
  - DIY IoT prototypes.

### 8. **Cybersecurity**

- Python is used to create cybersecurity tools for scanning, penetration testing, and malware analysis.
- Tools like **Scapy** and **Paramiko** are widely used in this domain.

### 9. **Desktop GUI Applications**

- Frameworks like **Tkinter**, **PyQt**, and **Kivy** enable Python to build desktop apps.
- Examples:
  - Media players.
  - Finance management tools.

### 10. **Finance and Fintech**

- Python is used for building financial models, risk analysis tools, and trading algorithms.
- Libraries like **QuantLib** and **NumPy** are common in the finance industry.
- Examples:
  - Predictive stock market models.
  - Cryptographic applications.

## Installing Python and Setting up the Environment

### Step 1: Download Python

1. Visit the official Python website: [python.org](https://www.python.org/).
2. Download the latest version of Python (choose the version compatible with your OS).

### Step 2: Install Python

- On Windows:

  1. Run the installer.
  2. Check the box to **Add Python to PATH**.
  3. Follow the prompts to complete the installation.

- On macOS and Linux:
  - Use the system package manager (`brew`, `apt`, or `yum`) or download from the official website.

### Step 3: Verify Installation

Open a terminal or command prompt and run:

```bash
python --version
```

or

```bash
python3 --version
```

### Step 4: Install an IDE/Text Editor

Choose a tool for writing Python code:

- **IDEs**: PyCharm, Visual Studio Code
- **Text Editors**: Sublime Text, Atom

---

## Running Python Scripts

### Interactive Mode

You can run Python commands interactively in the terminal by typing:

```bash
python
```

This opens the Python shell where you can directly execute Python code.

Example:

```python
>>> print("Hello, World!")
Hello, World!
```

### Script Mode

Save your Python code in a `.py` file and run it using:

```bash
python your_script.py
```

Example:

1. Create a file `hello.py` with the following content:
   ```python
   print("Hello, Python!")
   ```
2. Run it in the terminal:
   ```bash
   python hello.py
   ```

## How Python Works ?

Python is an **interpreted language**, meaning it executes code line by line using an interpreter rather than compiling it into machine code before running. Here's a detailed breakdown of how Python processes and executes your code:

---

### 1. Writing the Code

When you write Python code, you typically save it in a `.py` file. For example:

```python
# hello.py
print("Hello, Python!")
```

---

### 2. Python Interpreter Overview

The Python interpreter is the software responsible for executing Python code. It performs the following steps:

1. **Lexical Analysis**:

   - The interpreter reads the code and breaks it down into a series of tokens.
   - For example, in the code `print("Hello, Python!")`, tokens are:
     - `print` (a keyword)
     - `"Hello, Python!"` (a string)
     - `()` (parentheses)

2. **Parsing**:

   - The tokens are analyzed to ensure they follow the rules of Python's syntax.
   - If there's a syntax error, the interpreter throws an error at this stage.

3. **Abstract Syntax Tree (AST) Generation**:

   - Python converts the parsed code into an **AST** (a tree-like representation of the program's structure).
   - This tree helps the interpreter understand the logical flow of the code.

4. **Bytecode Compilation**:

   - The AST is converted into **bytecode**, a lower-level, platform-independent representation of the code.
   - Bytecode is saved in `.pyc` files (cached versions of Python scripts) in the `__pycache__` directory.

   Example:

   ```python
   print("Hello, Python!")
   ```

   is converted into bytecode instructions like:

   ```
   LOAD_NAME       0 (print)
   LOAD_CONST      0 ('Hello, Python!')
   CALL_FUNCTION   1
   RETURN_VALUE
   ```

---

### 3. The Python Virtual Machine (PVM)

The **Python Virtual Machine (PVM)** is a part of the interpreter that executes the bytecode. It acts as the "engine" running the program.

- The PVM reads the bytecode instructions one by one and translates them into machine-level operations specific to your operating system.
- This step is where your program is actually executed.

---

### 4. Interpreted Execution

Since Python is interpreted:

- Execution happens line by line.
- You can modify and rerun code without needing a recompilation step.

Example:

```python
print("Line 1 executed!")
print("Line 2 executed!")
```

The interpreter processes and runs the first `print` statement, then moves to the next one.

---

### 5. Error Handling in Python

Python handles errors during execution (runtime errors) in a way that stops the program if an error is encountered. For example:

```python
# This will throw a ZeroDivisionError
print(10 / 0)
```

Errors are thrown at runtime because Python cannot predict them during the lexical or parsing stages.

---

### Key Advantages of Python's Execution Model

1. **Platform Independence**:
   - Bytecode can run on any system with a Python interpreter.
2. **Dynamic Typing**:
   - Variable types are determined during runtime, making Python flexible.
3. **Ease of Debugging**:
   - Line-by-line execution makes errors easier to pinpoint.

---

### Summary of the Execution Flow

1. Code written in `.py` file.
2. Python interpreter:
   - Performs lexical analysis and parsing.
   - Converts the code to bytecode.
3. Bytecode is executed by the Python Virtual Machine (PVM).
4. Output or results are displayed.

---

### A Visualization of Python's Execution Flow:

![python_execution_flow](https://res.cloudinary.com/dcgrv6shk/image/upload/v1733385412/Internal-working-of-Python-_1_nuu1s5.gif)

## Python Syntax Basics

### Variables and Data Types

Variables are used to store data. Python automatically determines the data type. No need to define let, var or const like in js.

Example:

```python
#Number
age = 25            # Integer
height = 5.6        # Float

#String
name = "Alice"      # String

# Empty tuple
empty_tuple = ()

# Tuple with multiple elements
multi_element_tuple = (1, 2, 3)

# Tuple with mixed data types
mixed_tuple = ("apple", 3.14, True)


#List
fruits_list=["Apple", "Banana", "Orange"]
list=[21, 3.9, "Sameer Shahi"];  # a list of 3 diff type of objects.


#Dictionaries
dictionary1={
    'name':"Sameer Shahi",
    "age":20,
    "Blood-group":'A+',
    "salary":70000000,
}

#Boolean
is_student = True


# Sets
my_set = {1, 2, 3}  # set of integers
print(my_set)

my_set = {1.0, "Hello", (1, 2, 3)}  # set of mixed datatypes
print(my_set)
```

### Input and Output

- **Input**: Use `input()` to take input from the user.
- **Output**: Use `print()` to display information.

Example:

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

---

## Comments in Python

Comments are used to explain code and are ignored by the Python interpreter.

- **Single-line comment**: Start with `#`.

  ```python
  # This is a single-line comment
  print("Comments are useful!")
  ```

- **Multi-line comment**: Use triple quotes (`'''` or `"""`).
  ```python
  """
  This is a multi-line comment.
  It spans multiple lines.
  """
  print("Python is awesome!")
  ```
