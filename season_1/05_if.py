# 05_conditions_if_else.py
# Learning if / elif /else in Python

# Example 1 : simple if
age = 18

if age >= 18 :
    print("you are an adult")

# Example 2 : if - else 
score = 15

if score >= 10:
    print("passed")
else:
    print("Failed")

# Example 3: if - elif - else
number = int(input("Enter a number : "))

if number > 0 :
    print("Positive")
elif number < 0 :
    print("Negative")
else:
    print("Zero")

# Example 4 : boolean conditions
is_student = True

if is_student :
    print("Student discount aplied")
else :
    print("No discount")

# Example 6 : logical operators
username = "admid"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")