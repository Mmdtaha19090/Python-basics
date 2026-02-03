n , k , c = input().split()
n = int(n)
k = int(k)
while 0 < n - k :
    for i in range(n):
        print(n*c)
    n = n - k