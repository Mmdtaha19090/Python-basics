'''
In the land of wizards , there is a spell that has the following properties:
if a number is divisible by 3, it is a magical number.
if it is divisible by 5 , it is a cursed number.
if it is divisible by both of them ,it is considered a legendry number.
Otherwise it is a normal number.
Write a program that determines the type of a number...
'''
n = int(input())
type_n = ""
if n%3 ==0 and n%5 == 0 :
    type_n = "legendry"
elif n%3 == 0 :
    type_n = "magical"
elif n%5 == 0 :
    type_n = "cursed"
else :
    type_n = "normal"
print(f"n type is {type_n}.")