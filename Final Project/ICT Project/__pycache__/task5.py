x=int(input("enter your number "))
limt=10
answer=1
while True:
    if x<limt:
        print(answer)
        break
    else:
        limt=limt*10
        answer=answer+1 
