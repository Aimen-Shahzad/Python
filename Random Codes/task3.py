"""Write a program to ask user input for a number. Check if it is a prime number. If it is, end the program 
but if it is not ask for the user input again till the user enters a prime number."""
status=True
while status==True:
    is_prime=True
    number=int(input("enter a number "))
    for i in range (2,number):
        if number%i==0:
            is_prime=False
    if is_prime==True:
        print("your number is prime")
        status=False
    else :
        print("your number is not prime")
