# Write a Python program using a function that takes five numbers from the user and prints their GCD

import math
def bmmdef():
    number = []
    for i in range(5):
        x = int(input("Enter Number : "))
        number.append(x)
    bmm = number[0]
    for j in range(1,5):
        bmm = math.gcd(bmm,number[i])
    print(bmm)
bmmdef()