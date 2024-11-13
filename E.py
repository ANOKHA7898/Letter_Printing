# patter for letter E

for row in range(num+1):
    for col in range(num+1):
        if row in [2,3,6,7] and col in [3,4,5,6,7,8,9]:
            print(" ",end =" ")
        else:
            print("X",end=" ")
    print()