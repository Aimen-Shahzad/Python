while True:
    number=int(input("enter a number "))
    status= True
    for n in range (2,number):
        if number%n==0:
            status= False
    if status==True:
        print("the number is prime")   
        break
    else:
        print("the number is not prime")   
        
    