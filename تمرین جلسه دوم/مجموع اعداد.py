sum=0  
i=0  #شمارنده
c=0   
while True:
    a=input("please enter number\nTo exit and print the sum of input numbers, type exit5 ")
    
    if a=="exit":
        print(sum)
        break
    i=i+1
    c=int(a)  #متغیری که ورودی را از استرینگ به عدد صحیح تغییر میدهد
    sum=sum+c

