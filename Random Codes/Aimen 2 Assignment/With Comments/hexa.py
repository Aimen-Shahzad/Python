#making function to convert number to hexadecimal
def hexaconverter(decimal):
#we made a string showing all hexadecimal numbers
#remember keep in mind index number like on index number 1 it has 1 value
#index number 9 has value 9 and 10 index number has value A so on
    hexa_string="0123456789ABCDEF"
#we made an empty string wee will use this string to store results and print results
    new_string=" "
#if decimal number is zero it will enter in iff condition and will print statement
    if decimal==0:
        print("Hexa-Decimal Number of 0 is also 0")
#if number is greater than 0 it will enter is while statement 
    while decimal>0:
#first of all you should convert one decimal to hexadecimal on register
#now we will take reminder by dividing our number with 16
        reminder=decimal%16
#important: now new string is empty we will make it equall to nudex number equall to reminder in hexa string
#like if reminder is 10 it will go to index number 10 and will see value that is A and will store A in new string
#after that we will combine this A with empty string 
#now empty string named as new string will be equall to A

        new_string=hexa_string[reminder]+new_string
#now we will change original decimal number for next division we will see how many times
#16 is divided on it completely by writing decimal//16  we already have seen reminder
#now decimal number will be equall to 
        decimal=decimal//16
#now this will use as decimal number for further divsion untill it becomes zero
#now new string will store next character with old one as we wrote plus sign in upper code
#print statement is in parallel to while so when while will end it will print final value of new string
    print("Hexa-Decimal Number is ",new_string)
#we are taking input
decimal=int(input("Enter Number : "))
#we are calling function
hexaconverter(decimal)
