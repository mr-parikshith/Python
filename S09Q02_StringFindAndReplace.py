"""
S09Q02
Write a search and replace program in Python. 
This should first take the original text as input by prompting the user for it. 
It should then, prompt the user for which word to search, 
and what new word it should be replaced with.
"""

def ReplaceText():
    OriginalText = input("Enter your Text: ")
    SearchText  = input("Enter the word that need to be replaced: ")
    if SearchText in OriginalText:
        ReplaceText = input("Enter the word to replace with: ")
        print(OriginalText.replace(SearchText, ReplaceText))
    else:
        print("Word '"+ SearchText+ "' don't exist in the Originl String!")

    
#Main starts here:
ReplaceText()
