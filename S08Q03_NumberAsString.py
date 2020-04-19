"""
S08Q03
Ask the user to enter a number.
- If the user enters a number as 5, then
generate the following string :
- 00001111222233334444

- If the user enters the number as 3, then
generate the following string :
- 001122
"""

def enterNumber():
    Number = int(input("Enter Number : "))
    while Number != 3 or Number != 5:
        Number = int(input("Enter Number : "))
        #continue
        if Number == 5:
            print("00001111222233334444")
            break
        elif Number == 3:
            print("001122")
            break


#Enter main here
enterNumber()
