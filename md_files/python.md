# Python Notes

## 1. What is Python?
Python is a high-level, interpreted, general-purpose programming language known for its simple syntax and readability.

### Features
- Easy to learn and use
- Cross-platform
- Large standard library
- Supports multiple programming paradigms
- Popular in AI, ML, Web Development, Automation, and Data Science

---

## 2. Variables and Data Types

```python
name = "Alice"
age = 20
height = 5.7
is_student = True
```

### Common Data Types
| Type | Example |
|------|---------|
| int | 10 |
| float | 3.14 |
| str | "Hello" |
| bool | True |
| list | [1, 2, 3] |
| tuple | (1, 2, 3) |
| set | {1, 2, 3} |
| dict | {"name": "Alice"} |

---

## 3. Input and Output

```python
name = input("Enter your name: ")
print("Hello", name)
```

---

## 4. Operators

### Arithmetic
```python
+  -  *  /  //  %  **
```

### Comparison
```python
==  !=  >  <  >=  <=
```

### Logical
```python
and  or  not
```

---

## 5. Conditional Statements

```python
age = 18

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

---

## 6. Loops

### For Loop

```python
for i in range(5):
    print(i)
```

### While Loop

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

---

## 7. Functions

```python
def greet(name):
    return f"Hello {name}"

print(greet("Alice"))
```

### Default Arguments

```python
def greet(name="User"):
    print(name)
```

---

## 8. Lists

```python
numbers = [1, 2, 3, 4]
```

### Common Operations

```python
numbers.append(5)
numbers.remove(2)
numbers.pop()
len(numbers)
```

### List Comprehension

```python
squares = [x*x for x in range(5)]
```

---

## 9. Tuples

```python
point = (10, 20)
```

- Ordered
- Immutable

---

## 10. Sets

```python
nums = {1, 2, 3}
nums.add(4)
```

- No duplicates
- Fast lookup

---

## 11. Dictionaries

```python
student = {
    "name": "Alice",
    "age": 20
}
```

Access:

```python
print(student["name"])
```

---

## 12. Strings

```python
text = "Python"
```

Common Methods:

```python
text.upper()
text.lower()
text.strip()
text.split()
text.replace("P", "J")
```

---

## 13. Exception Handling

```python
try:
    num = int(input())
except ValueError:
    print("Invalid input")
```

---

## 14. File Handling

### Writing

```python
with open("file.txt", "w") as f:
    f.write("Hello")
```

### Reading

```python
with open("file.txt", "r") as f:
    data = f.read()
```

---

## 15. Object-Oriented Programming

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

s = Student("Alice")
s.display()
```

### OOP Concepts
- Class
- Object
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

---

## 16. Modules

```python
import math

print(math.sqrt(16))
```

### Create Your Own Module

```python
# mymodule.py
def greet():
    print("Hello")
```

```python
import mymodule
mymodule.greet()
```

---

## 17. Virtual Environments

Create:

```bash
python -m venv venv
```

Activate (Windows):

```powershell
venv\Scripts\activate
```

Deactivate:

```powershell
deactivate
```

---

## 18. Useful Libraries

### Data Science
- NumPy
- Pandas
- Matplotlib

### Machine Learning
- Scikit-learn
- TensorFlow
- PyTorch

### Web Development
- Flask
- FastAPI
- Django

### AI Applications
- LangChain
- LangGraph
- OpenAI SDK

---

## 19. Python Project Structure

```text
project/
│
├── main.py
├── requirements.txt
├── README.md
├── src/
└── tests/
```

---

## 20. Best Practices

- Use meaningful variable names.
- Follow PEP 8 style guidelines.
- Write functions for reusable code.
- Handle exceptions properly.
- Use virtual environments.
- Write comments and documentation.
- Learn data structures and algorithms.

---

## Quick Revision

1. Variables store data.
2. Lists are mutable, tuples are immutable.
3. Dictionaries store key-value pairs.
4. Functions improve code reusability.
5. Classes enable OOP.
6. Modules help organize code.
7. Virtual environments isolate dependencies.
8. Exception handling prevents crashes.
9. File handling reads and writes data.
10. Python is widely used in AI, ML, automation, and web development.
