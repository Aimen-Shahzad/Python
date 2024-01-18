income=22000
tax=0
condition1=20000
condition2=10000
if income>condition1:
    tax=income*0.20
    print(tax)
elif income>condition2:
    tax=income*0.15
    print(tax)
else:
    print("Your amount is less than 10k")