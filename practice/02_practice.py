def stars():
    a,b = input().split()
    a = int(a)
    if b == "s" or b == "S":
        for i in range(a):
            print("*"*a)
    elif b == "t" or b == "T":
        for j in range(a,0,-1):
            print(j*"*")
stars()