"""
S07Q01
Get the user’s first name and last name. 
        Assume the user provides “Dharmender” and “Singh” as inputs, 
          then print the user’s name in the following order and format

        - Name : dharmender, Surname : singh 
        - DHARMENDER SINGH
          ---------------------  ---------
        - Singh, Dharmender
"""

def getUserName():
    FirstName = input("What is your First Name: ")
    LastName  = input("What is your Last Name: ")
    print()
    print("Name :", str.lower(FirstName)+", Surname : ",str.lower(LastName))
    print(str.upper(FirstName), str.upper(LastName))
    print("---------------------", "---------")
    print(str.capitalize(FirstName), str.capitalize(LastName))


#Main starts here
getUserName()
