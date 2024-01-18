limit=int(input("enter a number "))
def  fb (v2): 
    n1=0
    n2=1
    
    while n1+n2<v2:
        print(n1+n2)
        n1,n2=n2,(n1+n2)

fb(limit)    