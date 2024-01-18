while True:
    octal_number=str(input("Enter Your Octal Number :"))
    length=len(octal_number)
    result=0
    status=True
    for x in range(length):
        checker=octal_number[x]
        checker=int(checker)
        if checker>7:
            print("You Can not enter Number Greater than 7 in Octal.\nEnter Number Again")
            status=False
    if status==True:
        for i in range(length):
            integer=octal_number[length-(i+1)]
            integer=int(integer)
            integer=integer*(8**(i))
            result=integer+result
        print("Your Decimal Output is ",result)
        break