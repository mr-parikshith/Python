"""
S08Q01
Ask the user to enter a number. 
Find the number of digits in that number
"""

def enterNumber():
    Number = int(input("Enter Number: "))
    print(Number)

    Digits = len(str(Number))
    print("Number of digits in that number entered:", Digits)

#Main starts here
enterNumber()
