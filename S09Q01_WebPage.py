"""
S09Q01

Write a program that generates a HTML webpage. 
Prompt the user for webpage title and webpage body contents. 
The webpage body should contain 
 - one main header, 
 - one sub header, and 
 - at least 2 paragraphs.

A sample output is shown below :
"""
def Webpage():
    MainHeader = input("Enter your Main Header: ")
    SubHeader  = input("Enter your Sub Header: ")
    Paragraph1 = input("Enter your 1st Paragraph: ")
    Paragraph2 = input("Enter your 2nd Paragraph: ")
    print(  "<html><head><title>", MainHeader,"</title></head><body><h1>", SubHeader, "</h1><p>", Paragraph1,"</p><p>", Paragraph2, "</p></body></html>")
                           
#Main starts here:
Webpage()
