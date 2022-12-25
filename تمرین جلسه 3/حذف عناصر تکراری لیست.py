m=[8,0,3,0,4,1,8,8,10,7]
def  delet_duplicate(itemes):
    unique=[]
    for item in itemes:
        if item not in unique:
            unique.append(item)
    return unique
print(delet_duplicate(m))        