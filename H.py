#pattern for letter H

for row in range(8):
    for col in range(7):
        if row in [0,1,2] and col in [2,3,4]:
            print(" ",end=" ")
        elif row in [5,6,7] and col in [2,3,4]:
            print(" ",end =" ")
        else:
            print("X",end=" ")
    print()