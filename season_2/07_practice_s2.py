# Practice - Season 2

# 1. check age
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

# 2. sum numbers with while
total = 0
i = 1
while i <= 5:
    total += i
    i += 1
print("Sum:", total)

# 3. for loop practice
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "even")
    else:
        print(i, "odd")