# offer
buy = int(input())
if 50000 < buy :
    buy = 0.8 * buy
elif  20000<= buy < 50000:
    buy = 0.9 * buy
print(buy)