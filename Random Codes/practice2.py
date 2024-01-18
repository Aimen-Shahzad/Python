n=5
for i in range(n):
    for y in range(n,i,-1):
        print(" ", end=" ")    
    for x in range(0,i+1,+1)   :
        print("*"," ", end=" ")      
    print()    