### **Classes and Objects**

- **Class**: A blueprint for creating objects. It defines the attributes (data) and methods (functions) that the objects created from the class will have.
- **Object**: An instance of a class. It is created by calling the class and can have its own unique data, while sharing the structure and behavior defined by the class.

Example:

```python
class Dog:
    species = "Canine"  # Class attribute shared by all objects

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name)  # Output: Buddy
print(dog2.species)  # Output: Canine
```

---

### **Attributes and Methods**

- **Attributes**: Variables that hold data associated with a class and its objects. They can be instance attributes (specific to an object) or class attributes (shared across all objects of a class).
- **Methods**: Functions defined inside a class that describe the behaviors of the objects. Methods operate on the attributes of the class or instance.

Example:

```python
class Circle:
    pi = 3.14  # Class attribute

    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    def area(self):  # Instance method
        return Circle.pi * self.radius ** 2

# Using attributes and methods
circle = Circle(5)
print(circle.area())  # Output: 78.5
```

---

### **Constructor (`__init__` Method)**

The `__init__` method is a special method used to initialize new objects. It is called automatically when an object is created.

Example:

```python
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

student = Student("Alice", 101)
print(student.name)  # Output: Alice
```

---

### **Inheritance**

Inheritance allows a class (child or derived class) to inherit the attributes and methods of another class (parent or base class). It promotes code reuse and extensibility.

Example:

```python
class Animal:
    def sound(self):
        return "This is a generic sound."

class Dog(Animal):  # Dog inherits from Animal
    def sound(self):  # Overriding the parent method
        return "Bark!"

dog = Dog()
print(dog.sound())  # Output: Bark!
```

---

### **Polymorphism**

Polymorphism allows methods in different classes to have the same name but behave differently depending on the object calling them. This is typically achieved via method overriding.

Example:

```python
class Cat:
    def sound(self):
        return "Meow!"

class Cow:
    def sound(self):
        return "Moo!"

animals = [Cat(), Cow()]
for animal in animals:
    print(animal.sound())
# Output:
# Meow!
# Moo!
```

---

### **Encapsulation**

Encapsulation is the bundling of data (attributes) and methods into a single unit (class). It restricts direct access to some attributes and methods to prevent accidental modification. This is achieved using access modifiers:

- **Public**: Accessible anywhere (default).
- **Protected**: Prefix with `_` (convention to indicate limited access).
- **Private**: Prefix with `__` to hide from outside access.

Example:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Public attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return self.__balance

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.__balance}"

account = BankAccount("John", 1000)
print(account.deposit(500))  # Output: 1500
# print(account.__balance)  # AttributeError: '__balance' is private
```

---

These principles form the foundation of OOP in Python, enabling modular, reusable, and maintainable code.
