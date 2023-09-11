status=True


while status:
    menu="""

        1)First Name :
        2)Email Id :
        3)Password :
        4)Confirm Password:

    """
    
    print(menu)
    

    

    fname=input("Enter your name : ")
    email=input("Enter your email : ")
    password=input("Enter password: ")
    cpassword=input("Confirm your password : ")


    print("-------------------")
    if password==cpassword:

            print("Your name is ",fname)
            print("Your email id is  ",email)
            print("Your password is ",password)
            print("Your confirm password is ",cpassword)
    else:
             
        print("Password & Confirm Password doesnt match...")

    choice=input("Do you want to add more user?press y for yes and n for no : ")

    if choice=='n' or choice=='no':
        status=False
        print("Thank you for using")
