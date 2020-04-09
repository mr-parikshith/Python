"""
S04Q02
     - Brilliant School sets an exam wherein, 
                English exam is for 80 marks, 
                Science for 90 marks and 
                Mathematics for 100 marks. 

            Ask the student to enter the marks scored in each of these exams. 
            Calculate the total percentage marks and rank the student as below :
               - First Class if score is more than or equal to 90 %
               - Second Class if score is more than or equal to 75%
               - Average if student has not failed
               - Failed if score is less than or equal to 35 %

            Make sure your code uses the same principles 
                 as in the template codes of earlier exercises
"""

def get_Exam_Scores():
    EnglishScore = input("How much did you score in English for 80 marks? :")
    EnglishScore = int(EnglishScore)
    ScienceScore = input("How much did you score in Science for 90 marks? :")
    ScienceScore = int(ScienceScore)
    MathScore    = input("How much did you score in Mathematics for 100 marks? :")
    MathScore    = int(MathScore)
    TotalScore   = EnglishScore + ScienceScore + MathScore
    return TotalScore


def CalculatePercentage(TotalScore, FirstClass, SecondClass, Failed):
    if TotalScore >= FirstClass:
        print("You scored First Class")
    elif TotalScore >= SecondClass and TotalScore < FirstClass :
        print("You scored Second Class")
    elif TotalScore <= Failed :
        print("You have failed")
    else :
        print("You are Average")

# Main starts from here       
TotalScore = get_Exam_Scores()
TotalMarks = 270
FirstClass  = TotalMarks * 90/100
SecondClass = TotalMarks * 75/100
Failed      = TotalMarks * 35/100
CalculatePercentage(TotalScore, FirstClass, SecondClass, Failed)
