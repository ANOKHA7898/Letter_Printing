# pattern for letter D
num = 9
for row in range(num):
    for col in range(num//3):
        if row in [0,1,7,8] and col in[0,1,2]:
            print("X",end =" ")
        else:
            print(" ",end =" ")
    for col in range(num):
        if row in [2,3,4,5,6]  and col in [2,3,4,5,6]:
            print(" ",end=" ")
        else:
            print("X",end=" ")
    print()
