'''
S01AQ03
     - Modify program in S01Q02 to print the multiplication table 
           of any number desired by the user

           You can use following code template to create your solution : https://git.io/vgov6
           [ Click on "RAW" button if you find it difficult to download the code ]
'''

def get_number():
    """ 
        This function should fetch a number from user
        Input : None
        Return : an integer
    """
    number = input("Which multiplication table you want to print? : ")
    number = int(number)
    return number

def print_mtable(num):
    """ 
        This function prints the multiplication table of num
        Input : an integer
        Output : Display multiplication table of input integer
        Return : None
    """
    PrintTable = [ 1 * num,
                   2 * num,
                   3 * num,
                   4 * num,
                   5 * num,
                   6 * num,
                   7 * num,
                   8 * num,
                   9 * num,
                  10 * num,
                  11 * num,
                  12 * num]
    print(PrintTable)

def main():
    '''
        Main program
    '''
    inp = get_number()
    print_mtable(inp)
    
# Main starts from here
main()
