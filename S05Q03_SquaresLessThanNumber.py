"""
S05Q03
     - Take a number as input from the user. 
           Print all the squares of numbers from 1 to any large number. 
           The numbers printed should be less than 
                 the number given as input by the user
"""

def Print_Squares(Number):
    Number = int(Number)
    Counter = 0
    while Counter * Counter <= Number:
        print(Counter * Counter)
        Counter+= 1

Number = input("Enter a Number : ")
Print_Squares(Number)

"""
def EnterNumber(Number):    
    Number = int(Number)
    #NumberRange = range(0, Number+1)
    #while 
    for Number in range(0, Number+1):
        Square = Number * Number
        print(Square)
        #Number+= 1
"""
