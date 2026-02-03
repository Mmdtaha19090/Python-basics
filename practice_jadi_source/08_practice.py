'''
A store offers special discounts to its customers. The discount rules are as follows:
If the purchase amount is more than 50,000 Tomans, a 20% discount is applied.
If the purchase amount is between 20,000 and 50,000 Tomans, a 10% discount is applied.
If the purchase amount is less than 20,000 Tomans, no discount is applied.
Write a program that receives the purchase amount from the user and displays the final amount.
'''
buy = int(input())
if 50000 < buy :
    buy = 0.8 * buy
elif  20000<= buy < 50000:
    buy = 0.9 * buy
print(buy)