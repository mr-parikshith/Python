"""
S05Q01
- Print the multiplication table of a given number using “for” and “while” loops.
"""


def print_ForLoopMultiplicationTable(num):
    print("Following is printed of For Loop Function")
    for times in range(1,13):
        print( times, " x ", num, " = ", times * num)


def print_WhileLoopMultiplicationTable(num):
    print("Following is printed of For While Function")
    times = 1
    while times < 13:
        print( times, " x ", num, " = ", times * num)
        times += 1

# Main starts from here
num = 17    
print_ForLoopMultiplicationTable(num)
print()
print_WhileLoopMultiplicationTable(num)
