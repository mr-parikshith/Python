def CensusToolBox():
    from numpy import random
    PassKey = random.randint(1,25)
    #PassKey = 12
    #print("PassKey is", PassKey)
    Password = 0 #This value is to just initialize to get into the loop
    iterator = 1
    condition =0
    while iterator <= 5:
        print()
        Password = int(input("Enter Login Number between 1 and 25: "))
        #Put logic to defferenciate between alpha vs numeric.
        
        #print("iterator", iterator)
        if Password == PassKey:
            print("Sucessful Login\nWelcome!!!")
            break
        elif iterator == 5:
            print("Login FAILED!!!")
        elif (PassKey + 2) >= Password and (PassKey - 2) <= Password:
            condition = 1
            print("InVaLiD PaSsCoDe")
        elif Password - PassKey >= 2:
            if iterator != 4:
                print("INVALID PASSCODE")
            else:
                print("Login FAILED!!!")
                break
        elif PassKey - Password >= 2:
            if iterator != 4:
                print("invalid passcode")
            else:
                print("Login FAILED!!!")
                break
        #print("condition is:", condition)
        iterator += 1
        print()

#Main starts here:
CensusToolBox()
