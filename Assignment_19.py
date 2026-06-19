User = "RAJ"
Pass = "as123"

InputUser = input("Enter your name:")
InputPass = input("Enter the pass:")

if(InputUser == User):
    if(InputPass == Pass):
        print("Access Granted.\nYOU ARE WELCOME!!")

    else:
        print("Wrong Password.\nTry again!!")

else:
    print("Invalid Username.Please try again!!")                                 