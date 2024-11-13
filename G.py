# Code For printing letter G
for row in range(9):
    for col in range(10):
        if row in [2,3] and col in [2,3,4,5,6,7,8,9]:
            print(" ",end=" ")
        elif row in [4,5,6] and col in[2,3]:
            print(" ",end=" ")
        elif row in [6,7,8] and col in[6,7]:
            print(" ",end=" ")
        else:
            print("X",end=" ")
    print()