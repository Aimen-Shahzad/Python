phy=int(input("Enter your phy marks : "))
bio=int(input("Enter your bio marks : "))
chem=int(input("Enter your chem marks : "))
math=int(input("Enter your math marks : "))
computer=int(input("Enter your computrt marks : "))
percentage=(phy+bio+chem+math+computer)/5
print(percentage)
if percentage>=90:
   print("grade A")
elif percentage>=80:
   print("grade B")
elif percentage>=70:
    print("grade C")
elif percentage>=60:
    print("grade D")
elif percentage>=40:
     print("grade E")
elif percentage<=40:
     print("grade F") 