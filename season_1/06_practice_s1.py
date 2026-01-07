# Practice - Season 1 (Python Basics)

# 1. variables and types
name = "Taha"
age = 18
is_student = True

print(name)
print(age)
print(is_student)

print(type(name))
print(type(age))
print(type(is_student))

print("-" * 20)

# 2. numbers and operations
a = 15
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print("-" * 20)

# 3. string concatenation
message1 = "Hello " + name
message2 = f"My name is {name} and I am {age} years old"

print(message1)
print(message2)

print("-" * 20)

# 4. string methods
text = "   Python Programming Language   "

print(text.lower())
print(text.upper())
print(text.strip())
print(text.replace("Language", "Course"))
print(text.split())

print("-" * 20)

# 5. input and type casting
user_number = input("Enter a number: ")
user_number = int(user_number)

print("Double of your number:", user_number * 2)