#python code for printing letter A

for row in range(9):
    for col in range(8):
        if row in [2,3] and col in[2,3,4,5]:
            print(" ",end=" ")
        elif row in [6,7,8] and col in [2,3,4,5]:
            print(" ",end=" ")
        else:
            print("X",end=" ")
    print()