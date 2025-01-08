# SCHOLARSHIP GRANT APPLICATION SYSTEM
name =  input("Enter your name: ")
isEnrolled = input("Are you currently enrolled in DLL? (yes/no): ")

if isEnrolled.lower() == "yes":
    # is student age 18 to 35
    print(f"Hi, {name}! Welcome to the DLL Scholarship Grant System.")
    age = input("How old are you right now? ")

    if age >= 18 and 35:
        print("Your age complied with the age requirement.")

        grades = eval(input("What was your last GWA?"))

        if grades >= 86 and grades <= 100:
            print("Your grades pass the requirements.")

        else: 
            print("You are not qualified for the scholarship grant.")

            is4ps = input("Is your family currently enrolled/subscribed in 4ps program? ")

            if is4ps.lower() == "yes":
                print("Congratulations! You are now granted a scholarship.")
            else: 
                print("Sorry for 4ps member only.")

    else: 
        print("Sorry. You are not qualified for the scholarship grant.")

else:
    print("Thank you for using the system.")
