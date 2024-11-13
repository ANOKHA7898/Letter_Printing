#Python code for printing C
for row in range(9):
    for col in range(7):
        if row in [2,3,4,5,6] and col in [2,3,4,5,6]:
            print(" ",end=" ")
        else:
            print("X",end=" ")
    print()