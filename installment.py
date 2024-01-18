amount=int(input())
if amount>20000:
    while amount>20000:
        print(amount)
        amount=amount-1000
else: 
    print("amount is less than 20000")    