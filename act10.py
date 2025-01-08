for loop in range(1, 7):
    for x in range(7-loop):
        print(" ", end=" ")
    for y in range(loop):
        print(loop, end=" ")
    for z in range(loop-1):
        print(loop, end=" ")
    print()