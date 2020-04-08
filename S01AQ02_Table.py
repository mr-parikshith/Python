"""
Re-write the earlier question of S01Q02 using functions as mentioned below :

           You can use following code template to create your solution : https://git.io/vgoeT
           [ Click on "RAW" button if you find it difficult to download the code ]

   - Print the multiplication table of 17
"""

#table = input("Which table you want to print? :")

#table = int(table)


       

def print_mtable():
    table = 17
    PrintTable = [ 1 * table,
                   2 * table,
                   3 * table,
                   4 * table,
                   5 * table,
                   6 * table,
                   7 * table,
                   8 * table,
                   9 * table,
                  10 * table,
                  11 * table,
                  12 * table]
    print(PrintTable)
"""
Whats wrong with my code?

def print_mtable():
    table = 17
    x = 1
    y = 12
    if x <= y :
        PrintTable = [ x * table]
        print(PrintTable)
        x = x + 1
        print(x)
    else :
        print ("Reached end of table")
"""

# Main starts from here
print_mtable()
