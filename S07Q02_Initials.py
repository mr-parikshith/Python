"""
S07Q02
Get the user’s first name and last name. 
        Assume the user provides “Dharmender” and “Singh” as inputs, 
        Find his best possible initials by eliminating the last character 
        from each of the name as shown in this sample output

        - Step 1 : Dharmender Singh
        - Step 2 : Dharmende Sing
        - Step 3 : Dharmend Sin
        - Step 4 : Dharmen Si
        - Step 5 : Dharme S

        Expected output :
        Best possible initials of "Dharmender Singh" is :
        Dharme S
"""
def getUserName():
    FirstName = input("What is your First Name: ")
    LastName  = input("What is your Last Name: ")
    #FirstName = "Dharmender"
    #LastName  = "Singh"
    
    print()
    
    FirstNameLength = len(FirstName)
    LastNameLength = len(LastName)

    if FirstNameLength <= LastNameLength:
        MinLength = FirstNameLength# + 1
        MaxLength = LastNameLength
    else:
        MinLength = LastNameLength# + 1
        MaxLength = FirstNameLength
        
    #print(MaxLength)
    #print(MinLength)

    iterator = 0
    while (MinLength > iterator):
        print(FirstName[0:FirstNameLength-iterator], LastName[0:LastNameLength -iterator])
        iterator += 1
    else:
        print()
        print("Best possible initials of", FirstName, LastName," is :")
        print(FirstName[0:FirstNameLength-iterator+1], LastName[0:LastNameLength-iterator+1])

#Main starts here
getUserName()
