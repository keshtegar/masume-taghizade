print("is it possible to draw atringle with the numbers or not?")
a=int(input("please enter first number"))
b=int(input("please enter second number"))
c=int(input("please enter third number"))
if a+b>c and a+c>b and b+c>a:
    print("is possible")
else:
    print("is not possible")
