'''
S01AQ01
Re-write the earlier question of S01Q01 using functions as mentioned below :

           You can use following code template to create your solution : https://git.io/vgrjP
           [ Click on "RAW" button if you find it difficult to download the code ]

  - Modify the first “Hello World” program to prompt for user’s name 
           and then wish the user by saying Hello followed by his name

           Example :
           If user's name is Sam, then expected output is :
           Hello Sam !!!
'''
def get_username():
    name = input("Enter Your Name: ")
    return name
   
def say_hello(user):
    print("Hello " + user + " !!!")
    print("Hello", "World !!!") # This print statement appended per instructions in the code 

def main():
    user = get_username()
    say_hello(user)

# Main starts from below
main()
