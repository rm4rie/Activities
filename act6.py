password = "lotie"
my_pw = input("Enter your password: ")

if my_pw.lower() == password: 
    print("Access Granted.")
    print("Enjoy.")
elif my_pw.lower() == "jaoming":
    print("tumpak!")
else:
    print("Access Denied>")