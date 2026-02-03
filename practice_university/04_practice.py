def prime(x):
    for i in range(x-1 ,1,-1):
        if x%i==0 :
            return False
    if x < 2 :
        return False
    return True
a = int(input())
b = int(input())
for number  in range(a,b+1):
    if prime(number):
        print(number)