number=str(input("Enter Number : "))
list1=[]
for i in number:
    list1.append(i)
print(list1)
while True:
    list1
    if "A" in list1:
        index=list1.index("A")
        list1[index]="10"
    elif "B" in list1:
        index=list1.index("B")
        list1[index]="11"
    elif "C" in list1:
        index=list1.index("C")
        list1[index]="12"
    elif "D" in list1:
        index=list1.index("D")
        list1[index]="13"
    elif "E" in list1:
        index=list1.index("E")
        list1[index]="14"
    elif "F" in list1:
        index=list1.index("F")
        list1[index]="15"
    else:
        break
print(list1)    
    
length=len(list1)
length=length-1
output=0
for i in range (0,length+1):
    x=list1[length-i]
    x=int(x)
    y=x*(16**(i))
    output=output+y
print(output)
