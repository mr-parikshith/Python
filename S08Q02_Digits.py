"""
S08Q02
Ask the user to enter a number.
- If the number is a single digit number, add 7 to it, 
     and print the number in its unit’s place
- If the number is a two digit number, raise the number to the power of 5, 
     and print the last 2 digits
- If the number is a three digit number, ask user to enter another number. 
     Add the 2 numbers and print the last 3 digits
"""

def enterNumber():
    Number = int(input("Enter Number : "))

    if Number <= 9 and Number >= 0:
        Number = Number + 7
        Digits = Number % 10
        print("Number + 7 and its units digit : ", Digits)
    elif Number <= 99 and Number >= 10:
        Number = Number **5
        Digits = Number % 100
        print("Number ^ 5 and its last 2 digits : ", Digits)
    elif Number <= 999 and Number >= 100:
        OtherNumber = int(input("Enter another number : "))
        Number = Number + OtherNumber
        Digits = Number % 1000
        print("Number + OtherNumber : ", Digits)

#Main starts here
enterNumber()
