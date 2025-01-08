isReapet = True

while isReapet == True: 
    name = input("Enter a name: ")
    print(f"Hi, {name}!")
    # stopping point
    if name.lower() == "rodelyn":
        print("LOOP TERMINATED")
        isReapet = False
        break