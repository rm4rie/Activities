def menu():
    print("*MAIN MENU*")
    print("[1] Activities")
    print("[2] Code Challenges")
    print("[0] Exit the program")


def activities():
    act = input("Enter the number that you want to execute: ")
    print("Activity List")
    return

def cc():
    act = input("Enter the number that you want to execute: ")
    print("Code Challenge List")
    return

def exit():
    print("Thank you for visiting.")

while True:
    print("[1] Activity 1")
    print("[2] Activity 2")
    print("[3] Activity 3")
    print("[4] Activity 4")
    print("[5] Activity 5")
    print("[6] Activity 6")
    print("[7] Activity 7")
    print("[8] Activity 8")
    print("[9] Activity 9")
    print("[10] Activity 10")
    print("[11] Activity 11")
    print("[12] Activity 12")
    print("[13] Activity 13")
    print("[14] Activity 14")
    print("[15] Activity 15")
    print("[16] Activity 16")
    print("[17] Activity 17")
    print("[18] Activity 18")
    print("[19] Activity 19")
    print("[20] Activity 20")
    
    option = input("Select an option: ")
    if option == 1: 
            print("[1] Activity 1")
            print("Hello World")
            break
    elif option == 2: 
            print("[2] Activity 2")
            name = input("Input your name: ")
            age = input("Input your age:" )
            add = input("Input your email address: ")
            print(f"Hi", name, age, "years of age", "\n" + add)
            break
    else:
            print("Exit the program.")
            break
    
    print()