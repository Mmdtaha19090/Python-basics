'''
We have a machine that takes n and if it is even , halve it , and if it is odd , multiply it by three and add one.
Print the spteps to convert this number to one...
'''
n = int(input())
while n != 1 :
    if n %2 == 0 :
        n = int(n / 2)
        if n==1:
            print(n)
            break
        print(n,end=" -> ")
        
    else :
        n = int((3 * n) + 1)
        print(n, end=" -> ")
