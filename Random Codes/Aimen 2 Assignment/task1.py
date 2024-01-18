#making function to convert number to hexadecimal
def hexaconverter(decimal):
#we made a string showing all hexadecimal numbers
    hexa_string="0123456789ABCDEF"
#we made an empty string wee will use this string to store results and print results
    new_string=" "
#if decimal number is zero it will enter in iff condition and will print statement
    if decimal==0:
        print("Hexa-Decimal Number of 0 is also 0")
        exit()
#if number is greater than 0 it will enter is while statement 
    while decimal>0:
        reminder=decimal%16
        new_string=hexa_string[reminder]+new_string
        decimal=decimal//16
    print("Hexa-Decimal Number is ",new_string)
#Starting Statement
print("Enter Your Decimal Number to See its output in Hexa-Decimal Form")
#we are taking input
decimal=int(input("Enter Number : "))
#we are calling function
hexaconverter(decimal)
