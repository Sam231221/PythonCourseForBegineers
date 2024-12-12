# Numbers

## **1. `abs()`**

Returns the absolute value of a number.

- **Syntax**:  
  `abs(number)`
- **Parameters**:
  - `number`: An integer or float. If complex, returns the magnitude.
- **Return Type**:

  - Returns a positive float or integer.

- **Examples**:
  ```python
  print(abs(-10))  # Output: 10
  print(abs(-3.14))  # Output: 3.14
  print(abs(3 + 4j))  # Output: 5.0
  ```

---

## **2. `round()`**

Rounds a number to the nearest integer or specified number of decimal places.

- **Syntax**:  
  `round(number, ndigits)`
- **Parameters**:
  - `number`: The number to be rounded (float or int).
  - `ndigits` (optional): Number of digits to round to.
- **Return Type**:

  - Rounded integer or float.

- **Examples**:
  ```python
  print(round(5.678, 2))  # Output: 5.68
  print(round(5.5))  # Output: 6
  print(round(3.14159, 3))  # Output: 3.142
  ```

---

## **3. `pow()`**

Calculates the power of a number (base raised to the exponent).

- **Syntax**:  
  `pow(base, exp, mod)`
- **Parameters**:
  - `base`: Base number (int or float).
  - `exp`: Exponent (int or float).
  - `mod` (optional): Modulus to return the result of `(base ** exp) % mod`.
- **Return Type**:

  - Integer or float.

- **Examples**:
  ```python
  print(pow(2, 3))  # Output: 8
  print(pow(2, 3, 5))  # Output: 3
  print(pow(1.5, 2))  # Output: 2.25
  ```

---

## **4. `divmod()`**

Returns a tuple containing the quotient and remainder of a division.

- **Syntax**:  
  `divmod(a, b)`
- **Parameters**:
  - `a`: Dividend (int or float).
  - `b`: Divisor (int or float).
- **Return Type**:

  - A tuple `(quotient, remainder)`.

- **Examples**:
  ```python
  print(divmod(10, 3))  # Output: (3, 1)
  print(divmod(9.5, 2))  # Output: (4.0, 1.5)
  ```

---

## **5. `int()`**

Converts a value to an integer.

- **Syntax**:  
  `int(x, base)`
- **Parameters**:
  - `x`: A number or string to convert.
  - `base` (optional): Base of the number (valid only if `x` is a string).
- **Return Type**:

  - Integer.

- **Examples**:
  ```python
  print(int(5.67))  # Output: 5
  print(int("10"))  # Output: 10
  print(int("1010", 2))  # Output: 10
  ```

---

## **6. `float()`**

Converts a value to a float.

- **Syntax**:  
  `float(x)`
- **Parameters**:
  - `x`: A number or string.
- **Return Type**:

  - Float.

- **Examples**:
  ```python
  print(float(10))  # Output: 10.0
  print(float("3.14"))  # Output: 3.14
  ```

---

## **7. `complex()`**

Creates a complex number.

- **Syntax**:  
  `complex(real, imag)`
- **Parameters**:
  - `real`: Real part (int or float). Defaults to 0.
  - `imag`: Imaginary part (int or float). Defaults to 0.
- **Return Type**:

  - Complex number.

- **Examples**:
  ```python
  print(complex(3, 4))  # Output: (3+4j)
  print(complex(5))  # Output: (5+0j)
  ```

---

## **8. `max()` and `min()`**

Find the maximum or minimum value from an iterable or arguments.

- **Syntax**:
  - `max(iterable, *args, key)`
  - `min(iterable, *args, key)`
- **Parameters**:
  - `iterable`: A sequence or iterable.
  - `*args`: Additional values.
  - `key` (optional): Function to customize sorting.
- **Return Type**:

  - Maximum or minimum value (same type as input).

- **Examples**:
  ```python
  print(max(10, 20, 30))  # Output: 30
  print(min([5, 2, 8]))  # Output: 2
  print(max("abc"))  # Output: 'c'
  ```

---

## **9. `sum()`**

Returns the sum of elements in an iterable.

- **Syntax**:  
  `sum(iterable, start)`
- **Parameters**:
  - `iterable`: List or tuple of numbers.
  - `start` (optional): Initial value (default is 0).
- **Return Type**:

  - Sum of the elements.

- **Examples**:
  ```python
  print(sum([1, 2, 3, 4]))  # Output: 10
  print(sum([1, 2, 3], 10))  # Output: 16
  ```

---

## **10. `type()`**

Returns the type of a number.

- **Syntax**:  
  `type(object)`
- **Parameters**:
  - `object`: Any Python object.
- **Return Type**:

  - Type object.

- **Examples**:
  ```python
  print(type(10))  # Output: <class 'int'>
  print(type(3.14))  # Output: <class 'float'>
  print(type(3 + 4j))  # Output: <class 'complex'>
  ```

---

# Strings

Python provides a rich set of methods for working with strings. These methods can manipulate, search, format, and analyze strings effectively. Below are details about commonly used string methods:

---

## **1. `len()`**

Returns the length of a string.

- **Syntax**:  
  `len(string)`
- **Parameters**:
  - `string`: The string whose length is to be calculated.
- **Return Type**:

  - Integer.

- **Examples**:
  ```python
  print(len("Hello"))  # Output: 5
  print(len(""))  # Output: 0
  ```

---

## **2. `lower()`**

Converts all characters in a string to lowercase.

- **Syntax**:  
  `string.lower()`
- **Parameters**:
  - None.
- **Return Type**:

  - String in lowercase.

- **Examples**:
  ```python
  print("HELLO".lower())  # Output: "hello"
  ```

---

## **3. `upper()`**

Converts all characters in a string to uppercase.

- **Syntax**:  
  `string.upper()`
- **Parameters**:
  - None.
- **Return Type**:

  - String in uppercase.

- **Examples**:
  ```python
  print("hello".upper())  # Output: "HELLO"
  ```

---

## **4. `strip()`**

Removes leading and trailing whitespace (or specified characters) from a string.

- **Syntax**:  
  `string.strip([chars])`
- **Parameters**:
  - `chars` (optional): Characters to remove. Default is whitespace.
- **Return Type**:

  - String with removed characters.

- **Examples**:
  ```python
  print("  hello  ".strip())  # Output: "hello"
  print("...hello...".strip("."))  # Output: "hello"
  ```

---

## **5. `replace()`**

Replaces occurrences of a substring with another substring.

- **Syntax**:  
  `string.replace(old, new, count)`
- **Parameters**:
  - `old`: The substring to replace.
  - `new`: The replacement substring.
  - `count` (optional): Number of occurrences to replace.
- **Return Type**:

  - Modified string.

- **Examples**:
  ```python
  print("hello world".replace("world", "Python"))  # Output: "hello Python"
  print("ababab".replace("a", "x", 2))  # Output: "xbxbab"
  ```

---

## **6. `split()`**

Splits a string into a list of substrings based on a delimiter.

- **Syntax**:  
  `string.split(sep, maxsplit)`
- **Parameters**:
  - `sep` (optional): Delimiter string. Default is whitespace.
  - `maxsplit` (optional): Maximum number of splits.
- **Return Type**:

  - List of substrings.

- **Examples**:
  ```python
  print("hello world".split())  # Output: ["hello", "world"]
  print("a,b,c".split(","))  # Output: ["a", "b", "c"]
  ```

---

## **7. `join()`**

Joins elements of an iterable into a single string, separated by the specified delimiter.

- **Syntax**:  
  `'delimiter'.join(iterable)`
- **Parameters**:
  - `iterable`: An iterable of strings.
- **Return Type**:

  - A string.

- **Examples**:
  ```python
  print(",".join(["a", "b", "c"]))  # Output: "a,b,c"
  ```

---

## **8. `find()`**

Searches for the first occurrence of a substring and returns its index. Returns `-1` if not found.

- **Syntax**:  
  `string.find(sub, start, end)`
- **Parameters**:
  - `sub`: Substring to search for.
  - `start` (optional): Start index. Default is `0`.
  - `end` (optional): End index. Default is the end of the string.
- **Return Type**:

  - Integer.

- **Examples**:
  ```python
  print("hello world".find("world"))  # Output: 6
  print("hello".find("x"))  # Output: -1
  ```

---

## **9. `startswith()`**

Checks if a string starts with the specified prefix.

- **Syntax**:  
  `string.startswith(prefix, start, end)`
- **Parameters**:
  - `prefix`: The prefix to check.
  - `start` (optional): Start index. Default is `0`.
  - `end` (optional): End index. Default is the end of the string.
- **Return Type**:

  - Boolean.

- **Examples**:
  ```python
  print("hello world".startswith("hello"))  # Output: True
  ```

---

## **10. `endswith()`**

Checks if a string ends with the specified suffix.

- **Syntax**:  
  `string.endswith(suffix, start, end)`
- **Parameters**:
  - `suffix`: The suffix to check.
  - `start` (optional): Start index. Default is `0`.
  - `end` (optional): End index. Default is the end of the string.
- **Return Type**:

  - Boolean.

- **Examples**:
  ```python
  print("hello world".endswith("world"))  # Output: True
  ```

---

## **11. `isalpha()`**

Checks if all characters in the string are alphabetic.

- **Syntax**:  
  `string.isalpha()`
- **Parameters**:
  - None.
- **Return Type**:

  - Boolean.

- **Examples**:
  ```python
  print("hello".isalpha())  # Output: True
  print("hello123".isalpha())  # Output: False
  ```

---

## **12. `isdigit()`**

Checks if all characters in the string are digits.

- **Syntax**:  
  `string.isdigit()`
- **Parameters**:
  - None.
- **Return Type**:

  - Boolean.

- **Examples**:
  ```python
  print("123".isdigit())  # Output: True
  print("123a".isdigit())  # Output: False
  ```

---

## **13. `title()`**

Converts the first character of each word to uppercase and the rest to lowercase.

- **Syntax**:  
  `string.title()`
- **Parameters**:
  - None.
- **Return Type**:

  - String.

- **Examples**:
  ```python
  print("hello world".title())  # Output: "Hello World"
  ```

---

## **14. `format()`**

Formats a string using placeholders.

- **Syntax**:  
  `string.format(*args, **kwargs)`
- **Parameters**:
  - `*args`: Positional arguments.
  - `**kwargs`: Keyword arguments.
- **Return Type**:

  - Formatted string.

- **Examples**:
  ```python
  print("Hello, {}".format("world"))  # Output: "Hello, world"
  print("{name} is {age} years old".format(name="John", age=30))  # Output: "John is 30 years old"
  ```

---

# Tuples

Python tuples are immutable sequences, meaning their contents cannot be changed after creation. They are commonly used to store related pieces of data. Python provides several methods and operations to work with tuples.

---

## **Key Tuple Methods and Operations**

### **1. `len()`**

Returns the number of elements in a tuple.

- **Syntax**:  
  `len(tuple)`
- **Parameters**:
  - `tuple`: The tuple whose length is to be determined.
- **Return Type**:

  - Integer.

- **Example**:
  ```python
  t = (1, 2, 3)
  print(len(t))  # Output: 3
  ```

---

### **2. `index()`**

Returns the index of the first occurrence of a specified element.

- **Syntax**:  
  `tuple.index(element, start, end)`
- **Parameters**:
  - `element`: The value to search for.
  - `start` (optional): The starting index for the search. Default is `0`.
  - `end` (optional): The ending index for the search. Default is the end of the tuple.
- **Return Type**:
  - Integer.
- **Raises**:

  - `ValueError` if the element is not found.

- **Example**:
  ```python
  t = (1, 2, 3, 2)
  print(t.index(2))  # Output: 1
  ```

---

### **3. `count()`**

Returns the number of occurrences of a specified element in the tuple.

- **Syntax**:  
  `tuple.count(element)`
- **Parameters**:
  - `element`: The value to count.
- **Return Type**:

  - Integer.

- **Example**:
  ```python
  t = (1, 2, 2, 3, 2)
  print(t.count(2))  # Output: 3
  ```

---

## **Tuple Operations**

### **1. Accessing Elements**

Elements in a tuple can be accessed using indexing.

- **Syntax**:  
  `tuple[index]`
- **Example**:
  ```python
  t = (1, 2, 3)
  print(t[0])  # Output: 1
  print(t[-1])  # Output: 3
  ```

---

### **2. Slicing**

Tuples support slicing to retrieve a subset of elements.

- **Syntax**:  
  `tuple[start:end:step]`
- **Example**:
  ```python
  t = (0, 1, 2, 3, 4, 5)
  print(t[1:4])  # Output: (1, 2, 3)
  print(t[::2])  # Output: (0, 2, 4)
  ```

---

### **3. Concatenation**

Tuples can be concatenated using the `+` operator.

- **Syntax**:  
  `tuple1 + tuple2`
- **Example**:
  ```python
  t1 = (1, 2)
  t2 = (3, 4)
  print(t1 + t2)  # Output: (1, 2, 3, 4)
  ```

---

### **4. Repetition**

The `*` operator can be used to repeat a tuple.

- **Syntax**:  
  `tuple * n`
- **Example**:
  ```python
  t = (1, 2)
  print(t * 3)  # Output: (1, 2, 1, 2, 1, 2)
  ```

---

### **5. Membership Test**

Check if an element exists in a tuple using `in`.

- **Syntax**:  
  `element in tuple`
- **Example**:
  ```python
  t = (1, 2, 3)
  print(2 in t)  # Output: True
  print(4 in t)  # Output: False
  ```

---

### **6. Iteration**

You can iterate through tuple elements using a loop.

- **Syntax**:
  ```python
  for element in tuple:
      # Do something
  ```
- **Example**:
  ```python
  t = (1, 2, 3)
  for item in t:
      print(item)
  # Output:
  # 1
  # 2
  # 3
  ```

---

### **7. Unpacking**

Tuples can be unpacked into individual variables.

- **Syntax**:  
  `var1, var2, ..., varn = tuple`
- **Example**:
  ```python
  t = (1, 2, 3)
  a, b, c = t
  print(a, b, c)  # Output: 1 2 3
  ```

---

## **Immutable Nature of Tuples**

Tuples are immutable, so elements cannot be modified after the tuple is created. However, if a tuple contains mutable elements (like lists), those elements can be changed.

- **Example**:
  ```python
  t = (1, [2, 3])
  t[1][0] = 4
  print(t)  # Output: (1, [4, 3])
  ```

---

# List

### 1. **`append()`**

#### Syntax:

```python
list.append(item)
```

#### Parameters:

- `item`: The element to be added to the end of the list.

#### Return Type:

- Returns `None` (modifies the list in place).

#### Example:

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ["apple", "banana", "cherry"]
```

---

### 2. **`extend()`**

#### Syntax:

```python
list.extend(iterable)
```

#### Parameters:

- `iterable`: Any iterable (e.g., list, tuple, set) whose elements will be added to the list.

#### Return Type:

- Returns `None` (modifies the list in place).

#### Example:

```python
fruits = ["apple", "banana"]
fruits.extend(["cherry", "date"])
print(fruits)  # Output: ["apple", "banana", "cherry", "date"]
```

---

### 3. **`insert()`**

#### Syntax:

```python
list.insert(index, item)
```

#### Parameters:

- `index`: The position at which to insert the item.
- `item`: The element to insert.

#### Return Type:

- Returns `None` (modifies the list in place).

#### Example:

```python
fruits = ["apple", "banana"]
fruits.insert(1, "cherry")
print(fruits)  # Output: ["apple", "cherry", "banana"]
```

---

### 4. **`remove()`**

#### Syntax:

```python
list.remove(item)
```

#### Parameters:

- `item`: The element to remove from the list. Raises `ValueError` if the item is not found.

#### Return Type:

- Returns `None` (modifies the list in place).

#### Example:

```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ["apple", "cherry"]
```

---

### 5. **`pop()`**

#### Syntax:

```python
list.pop([index])
```

#### Parameters:

- `index` (optional): The position of the element to remove and return. Defaults to the last element if not specified.

#### Return Type:

- Returns the removed element.

#### Example:

```python
fruits = ["apple", "banana", "cherry"]
item = fruits.pop(1)
print(item)   # Output: "banana"
print(fruits) # Output: ["apple", "cherry"]
```

---

### 6. **`clear()`**

#### Syntax:

```python
list.clear()
```

#### Parameters:

- None.

#### Return Type:

- Returns `None` (empties the list).

#### Example:

```python
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # Output: []
```

---

### 7. **`index()`**

#### Syntax:

```python
list.index(item[, start[, end]])
```

#### Parameters:

- `item`: The element to search for.
- `start` (optional): The starting index for the search.
- `end` (optional): The ending index for the search.

#### Return Type:

- Returns the index of the first occurrence of the item. Raises `ValueError` if the item is not found.

#### Example:

```python
fruits = ["apple", "banana", "cherry", "banana"]
index = fruits.index("banana")
print(index)  # Output: 1
```

---

### 8. **`count()`**

#### Syntax:

```python
list.count(item)
```

#### Parameters:

- `item`: The element to count occurrences of.

#### Return Type:

- Returns the number of occurrences of the item in the list.

#### Example:

```python
fruits = ["apple", "banana", "cherry", "banana"]
count = fruits.count("banana")
print(count)  # Output: 2
```

---

### 9. **`sort()`**

#### Syntax:

```python
list.sort(key=None, reverse=False)
```

#### Parameters:

- `key` (optional): A function to specify the sorting logic.
- `reverse` (optional): If `True`, sorts the list in descending order.

#### Return Type:

- Returns `None` (modifies the list in place).

#### Example:

```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)  # Output: [1, 1, 3, 4, 5]
```

---

### 10. **`reverse()`**

#### Syntax:

```python
list.reverse()
```

#### Parameters:

- None.

#### Return Type:

- Returns `None` (modifies the list in place).

#### Example:

```python
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)  # Output: ["cherry", "banana", "apple"]
```

---

### 11. **`copy()`**

#### Syntax:

```python
new_list = list.copy()
```

#### Parameters:

- None.

#### Return Type:

- Returns a shallow copy of the list.

#### Example:

```python
fruits = ["apple", "banana", "cherry"]
new_fruits = fruits.copy()
print(new_fruits)  # Output: ["apple", "banana", "cherry"]
```

---

### 12. **`join()`**

Lists do not have a `join` method, but strings can join lists of strings:

```python
", ".join(["apple", "banana", "cherry"])
```

### Summary Table

| **Method**  | **Parameters**         | **Return Type**    | **Description**                            |
| ----------- | ---------------------- | ------------------ | ------------------------------------------ |
| `append()`  | `item`                 | `None`             | Adds an element to the end of the list.    |
| `extend()`  | `iterable`             | `None`             | Appends items from another iterable.       |
| `insert()`  | `index`, `item`        | `None`             | Inserts an item at a specified index.      |
| `remove()`  | `item`                 | `None`             | Removes the first occurrence of an item.   |
| `pop()`     | `index` (optional)     | Removed element    | Removes and returns the item at the index. |
| `clear()`   | None                   | `None`             | Removes all elements from the list.        |
| `index()`   | `item`, `start`, `end` | Index (int)        | Returns the index of the first occurrence. |
| `count()`   | `item`                 | Count (int)        | Counts the occurrences of an item.         |
| `sort()`    | `key`, `reverse`       | `None`             | Sorts the list in place.                   |
| `reverse()` | None                   | `None`             | Reverses the order of the list in place.   |
| `copy()`    | None                   | New list (shallow) | Returns a shallow copy of the list.        |

---

# Dictionary

Dictionaries in Python are used to store data as key-value pairs. Python provides several built-in methods to manipulate and work with dictionaries. Below is a detailed guide to these methods.

---

### 1. **`get()`**

#### Syntax:

```python
dict.get(key[, default])
```

#### Parameters:

- `key`: The key to look up in the dictionary.
- `default` (optional): The value to return if the key is not found. Defaults to `None`.

#### Return Type:

- Returns the value associated with the key, or the `default` value if the key is not found.

#### Example:

```python
data = {"name": "Alice", "age": 25}
print(data.get("name"))       # Output: "Alice"
print(data.get("gender", "N/A"))  # Output: "N/A"
```

---

### 2. **`keys()`**

#### Syntax:

```python
dict.keys()
```

#### Parameters:

- None.

#### Return Type:

- Returns a view object that displays all the keys in the dictionary.

#### Example:

```python
data = {"name": "Alice", "age": 25}
print(data.keys())  # Output: dict_keys(['name', 'age'])
```

---

### 3. **`values()`**

#### Syntax:

```python
dict.values()
```

#### Parameters:

- None.

#### Return Type:

- Returns a view object containing all the values in the dictionary.

#### Example:

```python
data = {"name": "Alice", "age": 25}
print(data.values())  # Output: dict_values(['Alice', 25])
```

---

### 4. **`items()`**

#### Syntax:

```python
dict.items()
```

#### Parameters:

- None.

#### Return Type:

- Returns a view object containing tuples of key-value pairs.

#### Example:

```python
data = {"name": "Alice", "age": 25}
print(data.items())  # Output: dict_items([('name', 'Alice'), ('age', 25)])
```

---

### 5. **`update()`**

#### Syntax:

```python
dict.update([other])
```

#### Parameters:

- `other`: Another dictionary or iterable of key-value pairs to merge into the dictionary.

#### Return Type:

- Returns `None` (modifies the dictionary in place).

#### Example:

```python
data = {"name": "Alice"}
data.update({"age": 25, "gender": "Female"})
print(data)  # Output: {'name': 'Alice', 'age': 25, 'gender': 'Female'}
```

---

### 6. **`pop()`**

#### Syntax:

```python
dict.pop(key[, default])
```

#### Parameters:

- `key`: The key to remove from the dictionary.
- `default` (optional): The value to return if the key is not found. Raises a `KeyError` if no `default` is provided and the key is not found.

#### Return Type:

- Returns the value associated with the removed key.

#### Example:

```python
data = {"name": "Alice", "age": 25}
age = data.pop("age")
print(age)  # Output: 25
print(data) # Output: {'name': 'Alice'}
```

---

### 7. **`popitem()`**

#### Syntax:

```python
dict.popitem()
```

#### Parameters:

- None.

#### Return Type:

- Returns a tuple containing the last key-value pair removed. Raises `KeyError` if the dictionary is empty.

#### Example:

```python
data = {"name": "Alice", "age": 25}
item = data.popitem()
print(item)  # Output: ('age', 25)
print(data)  # Output: {'name': 'Alice'}
```

---

### 8. **`clear()`**

#### Syntax:

```python
dict.clear()
```

#### Parameters:

- None.

#### Return Type:

- Returns `None` (removes all items from the dictionary).

#### Example:

```python
data = {"name": "Alice", "age": 25}
data.clear()
print(data)  # Output: {}
```

---

### 9. **`setdefault()`**

#### Syntax:

```python
dict.setdefault(key[, default])
```

#### Parameters:

- `key`: The key to check in the dictionary.
- `default` (optional): The value to set if the key is not found. Defaults to `None`.

#### Return Type:

- Returns the value associated with the key. If the key is not found, sets it to `default` and returns `default`.

#### Example:

```python
data = {"name": "Alice"}
value = data.setdefault("age", 25)
print(value)  # Output: 25
print(data)   # Output: {'name': 'Alice', 'age': 25}
```

---

### 10. **`copy()`**

#### Syntax:

```python
new_dict = dict.copy()
```

#### Parameters:

- None.

#### Return Type:

- Returns a shallow copy of the dictionary.

#### Example:

```python
data = {"name": "Alice", "age": 25}
new_data = data.copy()
print(new_data)  # Output: {'name': 'Alice', 'age': 25}
```

---

### 11. **`fromkeys()`** (Class Method)

#### Syntax:

```python
dict.fromkeys(iterable[, value])
```

#### Parameters:

- `iterable`: An iterable specifying the keys for the dictionary.
- `value` (optional): The value to associate with each key. Defaults to `None`.

#### Return Type:

- Returns a new dictionary.

#### Example:

```python
keys = ["name", "age", "gender"]
default_dict = dict.fromkeys(keys, "unknown")
print(default_dict)  # Output: {'name': 'unknown', 'age': 'unknown', 'gender': 'unknown'}
```

---

### 12. **`del` Statement**

#### Usage:

To delete a key-value pair from the dictionary.

```python
del dict[key]
```

#### Example:

```python
data = {"name": "Alice", "age": 25}
del data["age"]
print(data)  # Output: {'name': 'Alice'}
```

---

### Summary Table

| **Method**     | **Parameters**      | **Return Type**    | **Description**                                      |
| -------------- | ------------------- | ------------------ | ---------------------------------------------------- |
| `get()`        | `key`, `default`    | Value or `default` | Returns value for key or default if not found.       |
| `keys()`       | None                | dict_keys view     | Returns a view of all keys.                          |
| `values()`     | None                | dict_values view   | Returns a view of all values.                        |
| `items()`      | None                | dict_items view    | Returns a view of all key-value pairs.               |
| `update()`     | `other`             | None               | Updates dictionary with another dictionary or pairs. |
| `pop()`        | `key`, `default`    | Removed value      | Removes and returns value for the key.               |
| `popitem()`    | None                | Tuple (key, value) | Removes and returns the last key-value pair.         |
| `clear()`      | None                | None               | Removes all items from the dictionary.               |
| `setdefault()` | `key`, `default`    | Value or `default` | Sets default if key is missing and returns value.    |
| `copy()`       | None                | New dictionary     | Returns a shallow copy of the dictionary.            |
| `fromkeys()`   | `iterable`, `value` | New dictionary     | Creates a dictionary with keys from iterable.        |

---

# Set

Sets in Python are unordered collections of unique elements. They provide several built-in methods for performing common set operations like union, intersection, and difference. Below is a detailed guide to Python set methods.

---

### 1. **`add()`**

#### Syntax:

```python
set.add(element)
```

#### Parameters:

- `element`: The element to add to the set.

#### Return Type:

- Returns `None` (modifies the set in place).

#### Example:

```python
s = {1, 2, 3}
s.add(4)
print(s)  # Output: {1, 2, 3, 4}
```

---

### 2. **`remove()`**

#### Syntax:

```python
set.remove(element)
```

#### Parameters:

- `element`: The element to remove from the set.

#### Return Type:

- Returns `None` (modifies the set in place). Raises a `KeyError` if the element is not found.

#### Example:

```python
s = {1, 2, 3}
s.remove(2)
print(s)  # Output: {1, 3}
```

---

### 3. **`discard()`**

#### Syntax:

```python
set.discard(element)
```

#### Parameters:

- `element`: The element to remove from the set.

#### Return Type:

- Returns `None` (modifies the set in place). Does not raise an error if the element is not found.

#### Example:

```python
s = {1, 2, 3}
s.discard(4)  # No error even though 4 is not in the set
print(s)  # Output: {1, 2, 3}
```

---

### 4. **`pop()`**

#### Syntax:

```python
set.pop()
```

#### Parameters:

- None.

#### Return Type:

- Returns the removed element. Raises a `KeyError` if the set is empty.

#### Example:

```python
s = {1, 2, 3}
removed = s.pop()
print(removed)  # Output: (e.g., 1)
print(s)        # Output: Remaining elements
```

---

### 5. **`clear()`**

#### Syntax:

```python
set.clear()
```

#### Parameters:

- None.

#### Return Type:

- Returns `None` (empties the set).

#### Example:

```python
s = {1, 2, 3}
s.clear()
print(s)  # Output: set()
```

---

### 6. **`union()`**

#### Syntax:

```python
set.union(*others)
```

#### Parameters:

- `*others`: One or more sets or iterables.

#### Return Type:

- Returns a new set containing all unique elements from the sets.

#### Example:

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
result = s1.union(s2)
print(result)  # Output: {1, 2, 3, 4, 5}
```

---

### 7. **`intersection()`**

#### Syntax:

```python
set.intersection(*others)
```

#### Parameters:

- `*others`: One or more sets or iterables.

#### Return Type:

- Returns a new set containing common elements.

#### Example:

```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}
result = s1.intersection(s2)
print(result)  # Output: {2, 3}
```

---

### 8. **`difference()`**

#### Syntax:

```python
set.difference(*others)
```

#### Parameters:

- `*others`: One or more sets or iterables.

#### Return Type:

- Returns a new set containing elements only in the original set.

#### Example:

```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}
result = s1.difference(s2)
print(result)  # Output: {1}
```

---

### 9. **`symmetric_difference()`**

#### Syntax:

```python
set.symmetric_difference(other)
```

#### Parameters:

- `other`: A set or iterable.

#### Return Type:

- Returns a new set containing elements not shared by both sets.

#### Example:

```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}
result = s1.symmetric_difference(s2)
print(result)  # Output: {1, 4}
```

---

### 10. **`issubset()`**

#### Syntax:

```python
set.issubset(other)
```

#### Parameters:

- `other`: A set or iterable.

#### Return Type:

- Returns `True` if the set is a subset of `other`, otherwise `False`.

#### Example:

```python
s1 = {1, 2}
s2 = {1, 2, 3}
print(s1.issubset(s2))  # Output: True
```

---

### 11. **`issuperset()`**

#### Syntax:

```python
set.issuperset(other)
```

#### Parameters:

- `other`: A set or iterable.

#### Return Type:

- Returns `True` if the set is a superset of `other`, otherwise `False`.

#### Example:

```python
s1 = {1, 2, 3}
s2 = {1, 2}
print(s1.issuperset(s2))  # Output: True
```

---

### 12. **`isdisjoint()`**

#### Syntax:

```python
set.isdisjoint(other)
```

#### Parameters:

- `other`: A set or iterable.

#### Return Type:

- Returns `True` if the sets have no elements in common, otherwise `False`.

#### Example:

```python
s1 = {1, 2, 3}
s2 = {4, 5}
print(s1.isdisjoint(s2))  # Output: True
```

---

### 13. **`copy()`**

#### Syntax:

```python
new_set = set.copy()
```

#### Parameters:

- None.

#### Return Type:

- Returns a shallow copy of the set.

#### Example:

```python
s = {1, 2, 3}
copy_s = s.copy()
print(copy_s)  # Output: {1, 2, 3}
```

---

### 14. **`update()`**

#### Syntax:

```python
set.update(*others)
```

#### Parameters:

- `*others`: One or more sets or iterables.

#### Return Type:

- Returns `None` (modifies the set in place).

#### Example:

```python
s = {1, 2}
s.update({2, 3, 4})
print(s)  # Output: {1, 2, 3, 4}
```

---

### Summary Table

| **Method**               | **Parameters** | **Return Type**   | **Description**                                  |
| ------------------------ | -------------- | ----------------- | ------------------------------------------------ |
| `add()`                  | `element`      | `None`            | Adds an element to the set.                      |
| `remove()`               | `element`      | `None`            | Removes an element; raises `KeyError` if absent. |
| `discard()`              | `element`      | `None`            | Removes an element; no error if absent.          |
| `pop()`                  | None           | Removed element   | Removes and returns an arbitrary element.        |
| `clear()`                | None           | `None`            | Removes all elements from the set.               |
| `union()`                | `*others`      | New set           | Returns a new set containing all elements.       |
| `intersection()`         | `*others`      | New set           | Returns common elements in all sets.             |
| `difference()`           | `*others`      | New set           | Returns elements unique to the original set.     |
| `symmetric_difference()` | `other`        | New set           | Returns elements unique to either set.           |
| `issubset()`             | `other`        | `True` or `False` | Checks if the set is a subset.                   |
| `issuperset()`           | `other`        | `True` or `False` | Checks if the set is a superset.                 |
| `isdisjoint()`           | `other`        | `True` or `False` | Checks if no elements are shared.                |
| `copy()`                 | None           | New set           | Returns a shallow copy.                          |
| `update()`               | `*others`      | `None`            | Updates the set with other elements.             |
