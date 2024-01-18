print("enter number 1 for multply, 2 for addition, 3 for division, 4 for subtraction")
operation=int(input("enter number:" ))
number1=int(input("enter number 1:" ))
number2=int(input("enter number 2:" )) 
if operation==1:
    result=number1*number2
    print("the product of ",number1,"and",number2,"is",result)
elif operation==2:
    result=number1+number2
    print("the sum of ",number1,"and",number2,"is",result)
elif operation==3:
    result=number1/number2
    print("the division of ",number1,"and",number2,"is",result)
elif operation==4:
    result=number1-number2
    print("the subtraction of ",number1,"and",number2,"is",result)
    