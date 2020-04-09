"""
S04Q01
     - A Chemical plant has a tank for storing ethanol.
            - When the tank is more than 80% full, it
                 should raise an alarm to close the valve.
            - When the tank is less than 20% full, it
                 should send an SMS to buy more liquid.
            - The total tank capacity is 900 litres.
            - Write a program to simulate this.
            - Ask user to enter current level of ethanol in the tank.
            - Print the appropriate action based on value entered
            - Make sure that your program needs minimum changes
                 for a tank of different capacity.

            You can use following code template to create your solution : https://git.io/vgoKP
            [ Click on "RAW" button if you find it difficult to download the code ]
"""
def do_action(present, redmark, bluemark):
    if present > redmark:
        print("Raise an alarm to close the valve.")
    elif present < bluemark :
        print("Send an SMS to buy more ethanol.")
    else :
        print("No action needed.")



def get_current_level():
    CurrentLevel = input("What is the current quantity of the tank in Lts.? :")
    CurrentLevel = int(CurrentLevel)
    return CurrentLevel

# Main starts from here
capacity = 900
high = capacity * 80/100
low  = capacity * 20/100
level = get_current_level()
do_action(level, high, low)
