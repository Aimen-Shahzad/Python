def hexaconversion (decimal):
    hexa_string="0123456789ABCDEF"
    new_string=" "
    if decimal==0:
        print("hexa_decimal number of 0 is also 0")
        exit()
    while decimal>0:
        remainder=decimal%16
        new_string=hexa_string[remainder]+new_string
        decimal=decimal//16
        print("Hexa_decimal number is", new_string)
print("enter your decimal number to see its output in hexa_decimal form")      
decimal=int(input("enter your number: ")) 
hexaconversion(decimal) 