"""
S05Q02
     - Ask the user to enter a number till he enters 0. 
          Print the maximum and minimum values among all entered numbers. 
          Print the number of single, two and three digit numbers entered.
"""

def print_CurrentMaxMin(Max, Min):
    print("Current Maximum Number is ", Max)
    print("Current Minimum Number is ", Min)

def print_FinalMaxMin(Max, Min):
    print("Final Maximum Number is ", Max)
    print("Final Minimum Number is ", Min)

def EnterNumber():
    Number = input("Enter a Number : ")
    Number = int(Number)
    MaximumNumber = Number
    MinimumNumber = Number
    print_CurrentMaxMin(MaximumNumber, MinimumNumber)
    while Number != 0:
        Number = input("Enter a Number : ")
        Number = int(Number)
        if Number == 0:
            print_FinalMaxMin(MaximumNumber, MinimumNumber)
            break
        elif Number >= MaximumNumber :
            MaximumNumber = Number
            print_CurrentMaxMin(MaximumNumber, MinimumNumber)
        elif Number <= MinimumNumber:
            MinimumNumber = Number
            print_CurrentMaxMin(MaximumNumber, MinimumNumber)
        else :
            print_CurrentMaxMin(MaximumNumber, MinimumNumber)           
    else:
        print_FinalMaxMin(MaximumNumber, MinimumNumber)


# Main starts here
EnterNumber()
    
