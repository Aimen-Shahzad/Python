#This will define number of rows 
n=5
#starrting for loop will print rows and inner foor loops will print pattern
for i in range(n):
    for x in range(n,i,-1):
#"""range start from 5 and goes to i with difference of -1 means move backward this loop is moving backward so
#loop value will decrease in each row as i value will increase and this loop is responsible for printing spaces 
# so loop value is decreasing than number of spaces is also decreasing in rows as we are going down"""
        print(" ",end="")
    for y in range(0,i+1,+1):
#this loop will print pattern range will be from 0 to i+1 as in first case i will be zero so i+1 will be 1 thats why range
#will be from 0 to 1 mean 1 value it will print one time
#in print statement we have * and space so it will print * and space
#when loop will run 2nd time i value will be 1 than i+1 will be 1+1 that is 2 so loop range will be from 0 to 2 that will have
#two values so loop will run two times and will print * than space and * and than space
        print("*","",end="")

    print()