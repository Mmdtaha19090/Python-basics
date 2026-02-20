def sum_of_squares(a,b):
    #Sum of squares : sos
    sos = a**2 + b**2
    return sos
a,b = map(int,input().split())
sos_2 = sum_of_squares(a,b)
print(sos_2)