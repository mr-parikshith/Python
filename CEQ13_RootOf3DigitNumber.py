"""
Coding Exam Question 13
              Ask the user to enter a 3 digit number till he enters 0
              Print the square root of only 3 digit positive numbers.

              Make sure that the program does not print the square root of any number that is not a 3 digit number
"""

def RootOf3DigitNumber():
    ThreeDigitNumber = int(input("Enter 3 digit number: "))
    while ThreeDigitNumber != 0:
        if ThreeDigitNumber <= 999 and ThreeDigitNumber >= 100:
            Root = ThreeDigitNumber **2
            print(Root)
            ThreeDigitNumber = int(input("Enter 3 digit number: "))
        else:
            ThreeDigitNumber = int(input("Enter 3 digit number: "))
    print("Break")
        
RootOf3DigitNumber()
