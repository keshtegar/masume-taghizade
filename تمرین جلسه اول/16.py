name=input("please enter  your name")
family=input("please enter  your family")
lesson1=float(input("please enter  first lesson"))
lesson2=float(input("please enter second lesson"))
lesson3=float(input("please enter third lesson"))
average=(lesson1+lesson2+lesson3)/3
if average>17:
    print("status is greate")
if 12<=average<17:
    print("statuse is normal")
if average<12:
    print("status is fail")


