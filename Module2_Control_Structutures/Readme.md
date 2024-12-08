# Module 2: Control Structures

## Control Structures in Python

Control structures in Python determine the flow of execution of the program. They allow programmers to control the sequence in which statements are executed, enabling decision-making, looping, and breaking from execution under certain conditions.

---

### Types of Control Structures

1. **Conditional Statements**
2. **Loops**
3. **Branching Statements**

---

### 1. **Conditional Statements**

Conditional statements execute a block of code based on a condition.

#### **Syntax:**

```python
'''
1. if statement
'''
if condition:
    #code block for true condition

'''
2. if else statment
'''
if condition:
    # code block for true condition
else:
    # code block above condition is false


'''
3. if elif else statement
'''
if condition:
    # code block for true condition
elif another_condition:
    # code block for another true condition
else:
    # code block if none of the conditions are true
```

#### **Example of if elif else:**

```python
age = 20
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are just an adult.")
else:
    print("You are an adult.")
```

**Output:**

```
You are an adult.
```

---

### 2. **Loops**

Loops allow repeated execution of a block of code as long as a condition is true.

#### **Types of Loops:**

- **`for` loop**: Iterates over a sequence (like a list, tuple, or range).
- **`while` loop**: Repeats as long as a condition is true.

#### **Syntax (for loop):**

```python
for item in sequence:
    # code block
```

#### **Example (for loop):**

```python
for number in range(1, 6):
    print(number)
```

**Output:**

```
1
2
3
4
5
```

#### **Syntax (while loop):**

```python
while condition:
    # code block
```

#### **Example (while loop):**

```python
counter = 1
while counter <= 5:
    print(counter)
    counter += 1
```

**Output:**

```
1
2
3
4
5
```

---

### 3. **Branching Statements**

These three statements are used to control the flow of loops and conditional logic in Python. Each one has specific use cases for altering or managing the loop's execution behavior.

---

#### 1. **`break` Statement**

The `break` statement is used to exit from a loop prematurely, regardless of the loop’s condition. It is typically used when you have found what you're looking for or when an exit condition has been met.

#### **When to Use `break`:**

- **Exit the loop when a condition is met**: If you're searching for an item in a list and find it, you can break the loop to avoid unnecessary iterations.
- **End a loop early to improve performance**: For example, if you have found the correct result, there's no need to continue the loop.

#### **Example:**

```python
# Finding a number in a list
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    if num == 30:
        print("Found 30, exiting loop.")
        break  # Exit the loop when 30 is found
```

**Output:**

```
Found 30, exiting loop.
```

#### **Key Point:**

`break` immediately stops the loop, and no further iterations are done.

---

#### 2. **`continue` Statement**

The `continue` statement skips the current iteration of the loop and moves to the next iteration. It doesn’t stop the loop; instead, it just skips over part of the code and continues with the next loop cycle.

#### **When to Use `continue`:**

- **Skip certain iterations based on a condition**: If you want to ignore specific cases and continue with the rest of the loop.
- **Filter out unwanted items**: For example, skipping even numbers in a loop that processes only odd numbers.

#### **Example:**

```python
# Printing only odd numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
```

**Output:**

```
1
3
5
7
```

#### **Key Point:**

`continue` moves to the next iteration of the loop, skipping any remaining code below it in that iteration.

---

#### 3. **`pass` Statement**

The `pass` statement does nothing. It is used as a placeholder in code blocks where syntactically some code is required, but you don't want to write any logic yet. It allows you to define an empty loop, function, or class.

#### **When to Use `pass`:**

- **Placeholder for future code**: When you're writing the structure of your program and plan to fill in the logic later.
- **Empty function or class**: When you need to define a function or class, but haven’t implemented it yet.
- **In loops or conditionals**: When you want to create an empty loop or if condition without causing an error.

#### **Example 1: Placeholder for a function**

```python
def my_function():
    pass  # Placeholder for future implementation
```

#### **Example 2: Empty loop**

```python
# Loop with pass
for num in range(5):
    if num == 2:
        pass  # Do nothing for num == 2
    print(num)
```

**Output:**

```
0
1
2
3
4
```

#### **Key Point:**

`pass` does nothing and allows the code to run without errors. It's a way to indicate "do nothing" explicitly.

---

#### Summary:

- **`break`**: Use when you need to **exit the loop** early (e.g., when a condition is met or a search is completed).
- **`continue`**: Use when you want to **skip the current iteration** of the loop and proceed with the next one.
- **`pass`**: Use when you need a **placeholder** for future code or to define an empty block (e.g., an empty loop or function).

---

### Summary of Control Structures:

- **Conditionals**: Make decisions (`if`, `elif`, `else`).
- **Loops**: Repeat code (`for`, `while`).
- **Branching Statements**: Control loop execution (`break`, `continue`, `pass`).

Control structures are fundamental for writing efficient and flexible Python programs.
