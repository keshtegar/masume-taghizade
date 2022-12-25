import random
from collections import Counter
pc_number=random.randint(0,20)
Counter=0
while True:
    user_number=int(input("enter number:"))
    if pc_number==user_number:
        print("barande shodi")
        break
    if pc_number>user_number:    
        print("boro balatar")
        Counter=Counter+1
    if pc_number<user_number:
        print("boro paeintar")
        Counter=Counter+1
print(Counter)
