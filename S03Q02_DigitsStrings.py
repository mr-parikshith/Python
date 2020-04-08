"""
S03Q02
     - Ask the user to enter a number.
            - If the number is a single digit number,
                 add 7 to it, and print the number in its unit’s place
            - If the number is a two digit number,
                raise the number to the power of 5, 
                and print the number in its unit’s place
            - If the number is a three digit number, 
                ask the user to enter another number. 
                Add the 2 numbers and print the number in its unit’s place

            Use the solution provided in S03Q01 as the template for this exercises.
            - Instead of doing a print to print the final result in "perform_check" function 
            call separate functions : 
               do_1digit_oper() and
               do_2digit_oper() and
               do_3digit_oper()
            that will perform the required operations based on the number of digits.
"""
def do_1digit_oper(number):
    number = number + 7
    last_char = str(number)[-1]
    print(last_char, "is the number in unit’s place.")

 
def do_2digit_oper(number):
    number = number ** 5
    last_char = str(number)[-1]
    print(last_char, "is the number in unit’s place.")
    
# do_2digit_oper(6)

def do_3digit_oper(number):
    AnotherNumber = input("Enter another number: ")
    AnotherNumber = int(AnotherNumber)
    number = number + AnotherNumber
    last_char = str(number)[-1]
    print(last_char, "is the number in unit’s place.")

# do_3digit_oper(6, 8)
    
def perform_check(number):
    num1 = int(number)
    if number < 10 :
        do_1digit_oper(num1)
    elif number >= 10 and number <= 99 :
        do_2digit_oper(num1)
    elif number >= 100 and number <= 999 :
        do_3digit_oper(num1)
    else :
        print("Number ", number, " is neither a 1,2 or 3 digit number.")

def get_number():
    """ This function prompts the user for a number
        It returns an integer [ and not a string ]
    """
    number = input("Enter 2 or 3 digit number : ")
    number = int(number)
    return number

# Main starts from here
num1 = get_number()
num2 = get_number()
perform_check(num1)
perform_check(num2)
