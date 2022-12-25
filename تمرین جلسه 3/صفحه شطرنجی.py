import numpy as np
m=int(input("pleas enter row"))
n=int(input("pleas enter column"))
a=np.full((m,n),"#")
a[1::2, ::2]="*"
a[::2,1::2]="*"
print(a)

        