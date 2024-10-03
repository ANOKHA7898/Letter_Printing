#python code for printing letter B

for row in range(12):
    for col in range(2):
        if row in [0,1,10,11]:
            print("X",end=" ")
        else:
            print(" ",end=" ")
    for  col in range(7):
        if row in[2,3,4,7,8,9] and col in [2,3,4]:
            print(" ",end=" ")
        else:
            print("X",end=" ")
            
    print()