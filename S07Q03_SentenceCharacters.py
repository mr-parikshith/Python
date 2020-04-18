"""
S07Q03
Prompt the user to enter a long sentence
        - What is the last character in the sentence ?
        - What are the last 5 characters in the sentence ?
        - Print the characters that are present in 2nd and 5th position of the sentence
        - Print the character at the center of the string, along with the 2 adjoining characters. 
        Ex : If the string entered is "Web Browser”
        the character at its centre is "r" and so print "Bro"
"""
def enterLongSentence():
    LongSentence = input("Enter a long sentence: ")
    print("Last character in the sentence is", LongSentence[-1])
    print("Last 5 character in the sentence is", LongSentence[-5])
    print("2nd and 5th character in the sentence are", LongSentence[1]+", " + LongSentence[4], "respectively")
    print(LongSentence[int(len(LongSentence)/2)-1:int(len(LongSentence)/2)+2])

#Main starts here    
enterLongSentence()
