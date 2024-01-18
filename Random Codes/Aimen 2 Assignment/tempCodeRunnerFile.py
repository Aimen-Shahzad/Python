#This will define number of rows 
n=5
#starrting for loop will print rows and inner foor loops will print pattern
for i in range(n):
    for x in range(n,i,-1):
        print(" ",end="")
    for y in range(0,i+1,+1):
        print("*","",end="")
    print()