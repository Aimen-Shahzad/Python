n=4
for y in range(n+1): 
    for x in range(n-y):
        print(" ",end=" ")
    for z in range(y):
        print("*",end=" ")
    for z in range (y, 1, -1):   
        print("*",end=" ")
    print()    
            
    