"""
S03Q01
     - Take 2 numbers from the user. 
            Print which number is a 2 digit number, 
            and which number is a 3 digit number. 
            If it is neither, then print the number as it is


            You can use following code template to create your solution : https://git.io/vgoVG
            [ Click on "RAW" button if you find it difficult to download the code ]
"""

def perform_check(number):
    
    """ This function uses helper functions
        check_if_2digit
        check_if_3digit
        to perform the required operations
    """
    number = int(number)
    if number >= 10 and number <= 99 :
        print("Number ", number, " is a 2 digit number.")
    elif number >= 100 and number <= 999 :
        print("Number ", number, " is a 3 digit number.")
    else :
        print("Number ", number, " is neither a 2 or 3 digit number.")
        
def get_number():
    """ This function prompts the user for a number
        It returns an integer [ and not a string ]
    """
    number = input("Enter 2 or 3 digit number : ")
    return number
    # Question to Safraaz: How to check if it is an integer vs a string?


# Main starts from here
num1 = get_number()
num2 = get_number()
perform_check(num1)
perform_check(num2)
