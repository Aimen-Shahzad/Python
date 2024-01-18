is_prime=True
x=int(input("enter your number "))
for i in range(2,x):
    if x%i==0:
        is_prime=False
if is_prime==False:
    print("your number is not prime")
else:
    print("your number is prime")       
            