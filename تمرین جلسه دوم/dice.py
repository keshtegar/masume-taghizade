import random
while True:
    user = input('Do you want to roll the dice??  (y/n) : ')
    if user == 'y':
        a = random.randint(1,6)
        print(a)
        if a==6:
            print("you won")
            for i in range(2):
                user = input("You are allowed to roll the dice two more times (y/n):")
                if user == "y":
                     a = random.randint(1,6)
                     print(a)
    else:
        print('Program Closed ! ')  
        break 
    