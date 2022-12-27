m=int(input("Please enter the number of rows"))
n=int(input("Please enter the number of column"))
x=1
for i in range(1,m+1):
    for j in range(1,n+1):
        if x==1:
        
            print("#", end="")
        else:
            print("*", end="")
        x=-x
    if i*j % 2 == 0: 
        x*=-1  
    print()            



        
