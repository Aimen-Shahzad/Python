number1=int(input("enter number 1 "))
number2=int(input("enter number 2 "))
number3=int(input("enter number 3 "))
number4=int(input("enter number 4 "))

def maxfunction (n1,n2,n3,n4):
    if n1>n2 and n1>n3 and n1>n4:
        print(number1, "is greatest")
    if n2>n1 and n2>n3 and n2>n4:
        print(number2,"is greatest")
    if n3>n1 and n3>n2 and n3>n4:
        print(number3,"is greatest") 
    if n4>n1 and n4>n2 and n4>n3:
        print(number4,"is greatest")
maxfunction(number1,number2,number3,number4)        
    
