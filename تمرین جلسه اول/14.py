import math
print("welcome to my calculator")
a=int(input("please enter a number: "))
x=math.radians(a)
op=input("please enter operation: ")
if op=="sqrt":
    result=math.sqrt(a)
if op=="sin":  
    result=math.sin(a)
if op=="cos":   
    result=math.cos(a)
if op=="tan":   
    result=math.tan(a)
if op=="cot":  
    result=1/(math.tan(x))
if op=="factorial":  
    result=math.factorial(a)
if op=="+":
    b=int(input("please enter another number: ")) 
    result=a+b
if op=="-":
    b=int(input("please enter another number: ")) 
    result=a-b
if op=="*":
    b=int(input("please enter another number: ")) 
    result=a*b
if op=="/":
    b=int(input("please enter another number: ")) 
if b==0:
    result="error"
if b!=0:
    resulte=a/b
print(result)
