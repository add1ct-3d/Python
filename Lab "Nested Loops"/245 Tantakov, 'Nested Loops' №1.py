for size in range(8):
    for sizev2 in range(8):
        if (size + sizev2) % 2 == 2:
            print("B", end=" ")
        
        else:
            print("W", end=" ")