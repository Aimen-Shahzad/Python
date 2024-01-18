def sum (n1,n2):
    result=n1+n2
    print("the sum of two numbers is:",result)
def product (n1,n2):
    result=(n1*n2)
    print("the product of two numbers is:" ,result)
def subtraction (n1,n2):
    result=n1-n2
    print=("the subtraction of two numbers is:" ,n1-n2)
def division(n1,n2):
    result=n1/n2
    print=("the division of two numbers is:" ,n1/n2)
      
print("enter + for sum, * for product, - for subtraction, / for diviosion")
operation=input("enter operation:" )
number1=int(input("enter number 1:" ))
number2=int(input("enter number 2:" )) 
if operation=="+":
    sum(number1,number2)
elif operation=="*":
     product(number1,number2)
elif operation=="-":
    subtraction(number1,number2)     
elif operation=="/":
     division(number1,number2)