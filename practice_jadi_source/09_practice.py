''' A magician has decided to increase the power of numbers using a special spell!
He chooses a number n as the number of steps and a number x on which the operation is to be performed.
Then he does the following:
If the number is odd, he doubles its value and subtracts 1 unit.
If the number is even, he halves its value.
The magician performs this operation exactly n times. '''

n = int(input())
x = int(input())
for i in range(n) :
    if x % 2 == 1:
        x = (x * 2) - 1
    else :
        x = x / 2
print(x)