---

### **1. Data Types Exercises**

#### **Exercise 1: Identify the Data Type**

Write a Python program that takes the following inputs from a user and prints their data types:

- An integer
- A float
- A string
- A boolean

Example:

```python
Input: 42, 3.14, "Hello", True
Output: int, float, str, bool
```

---

#### **Exercise 2: Type Conversion**

Write a Python program that:

1. Converts a string `"1234"` into an integer.
2. Converts a float `3.14` into an integer.
3. Converts an integer `10` into a float.
4. Converts an integer `1` into a boolean.

Print the results of all conversions.

---

#### **Exercise 3: Dictionary Manipulation**

Given the following dictionary:

```python
info = {"name": "Alice", "age": 25, "height": 5.5}
```

Write a program to:

1. Add a new key-value pair `"weight": 55`.
2. Update the value of `"age"` to `26`.
3. Remove the `"height"` key.
4. Print the updated dictionary.

---

### **2. Classes and Objects Exercises**

#### **Exercise 1: Create a Simple Class**

Create a class named `Rectangle` with:

1. Attributes: `length` and `width`.
2. A method `area()` that returns the area of the rectangle.
3. A method `perimeter()` that returns the perimeter of the rectangle.

Instantiate a `Rectangle` object with `length = 5` and `width = 3`, then calculate and print the area and perimeter.

---

#### **Exercise 2: Inheritance**

Create a class `Person` with:

1. Attributes: `name` and `age`.
2. A method `introduce()` that prints `Hi, my name is {name} and I am {age} years old.`

Then, create a subclass `Student` that inherits from `Person` and adds:

1. An attribute `grade`.
2. A method `study()` that prints `{name} is studying for grade {grade}.`

Create an object of the `Student` class and demonstrate the use of both methods.

---

#### **Exercise 3: Bank Account Class**

Create a class `BankAccount` with:

1. Attributes: `account_holder` and `balance` (default is 0).
2. Methods:
   - `deposit(amount)`: Adds `amount` to the balance.
   - `withdraw(amount)`: Deducts `amount` from the balance if there are sufficient funds, otherwise prints `"Insufficient balance."`
   - `get_balance()`: Prints the current balance.

Demonstrate the functionality with a `BankAccount` object.

---

### **3. Functions Exercises**

#### **Exercise 1: Simple Calculator**

Write a Python function named `calculator()` that:

1. Takes three inputs: two numbers and an operator (`+`, `-`, `*`, `/`).
2. Returns the result of the operation.
3. Prints `"Invalid operator"` if the operator is not one of the above.

Example:

```python
Input: 5, 3, "*"
Output: 15
```

---

#### **Exercise 2: Find the Maximum**

Write a function named `find_maximum()` that:

1. Accepts a list of numbers as input.
2. Returns the largest number in the list without using the `max()` function.

Example:

```python
Input: [5, 1, 9, 3, 7]
Output: 9
```

---

#### **Exercise 3: Count Vowels**

Write a function `count_vowels()` that:

1. Accepts a string as input.
2. Counts and returns the number of vowels (`a, e, i, o, u`) in the string (case-insensitive).

Example:

```python
Input: "Hello World"
Output: 3
```

---

Let me know if you want me to elaborate on or solve any of these exercises!
