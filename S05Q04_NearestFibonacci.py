"""
S05Q04
     - Check if a given number is a fibonacci number. 
           If not, then print the closest fibonacci number to the given number
"""
def NearestFibonacci():
    Number = input("Enter a Number : ")
    Number = int(Number)
    Fibonacci0 = 0
    Fibonacci1 = 1
    #print(Fibonacci0)
    #print(Fibonacci1)
    Fibonacci2 = Fibonacci1
    Fibonacci3 = Fibonacci0 + Fibonacci1
    while Fibonacci3 <= Number:
        Fibonacci3 = Fibonacci0 + Fibonacci1
        Fibonacci2 = Fibonacci1
        Fibonacci0 = Fibonacci1
        #print(Fibonacci2)
        Fibonacci1 = Fibonacci3
    else:
        if (Number - Fibonacci2) <= (Fibonacci3 - Number):
            print(Fibonacci2)
        else :
            print(Fibonacci3)

#Main starts here
NearestFibonacci()
