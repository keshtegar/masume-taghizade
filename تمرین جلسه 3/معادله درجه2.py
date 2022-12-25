import math
def moadele_daraje2():
    a=int(input("please enter a: "))
    b=int(input("please enter b: "))
    c=int(input("please enter c: "))
    delta=(b**2)-(4*a*c)
    if delta==0:
        x=(-b/2*a)
        print("moadele yek javab darad:",x)
    if delta>0:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        print("moadele 2 javab darad:",x1,x2)
    if delta<0:
        print("moadele javab nadarad")
   
moadele_daraje2()