"""
Coding Exam Question 12
Brilliant School conducts an exam in subjects of English, Science and Mathematics.
Science exam is split up as Science Theory and Science Practical

The maximum marks for each subject is as follows : 
          -- English : 75 marks
          -- Science Theory : 75 marks
          -- Science Practical : 25 marks
          -- Science = Science Theory + Science Practical : 100 marks
          -- Mathematics : 100 marks

The pass marks for each subject is as follows :
          -- Pass marks for English : 25
          -- Pass marks for Science Theory : 25
          -- Pass marks for Science Practical : 8
          -- Pass marks for Science : 35
          -- Pass marks for Mathematics : 35

Write a Python program to collect the marks scored by a student in all the above 4 exams
Based on the marks scored by the student, grade them according to the following criteria :
          -- Grade A : if Total > 90%
          -- Grade B : if Total > 75%
          -- Fail is any score is less than pass marks
          -- Average otherwise

Note : A student who scores only Pass marks in Science Theory and Science Practical 
            will have a total of 33 [ 25 + 8 ] 
            and this still falls short of the Pass marks for Science [ 35 ]
            and is considered as Fail.
"""

def PassMark(Mark, Subject):
    1==1
    if Mark < 35:
        if Subject in ["Mathematics", "Science"]:
            #print(Subject, "Fail")
            Outcome = "Fail"
        elif Subject == "English":
            if Mark < 25:
                #print(Subject, "Fail")
                Outcome = "Fail"
            else :
                #print(Subject, "Pass")
                Outcome = "Pass"
        else:
            #print(Subject, "Pass")
            Outcome = "Pass"
    else :
        #print(Subject, "Pass")
        Outcome = "Pass"
    return Outcome

def MarksEntry(Subject):
    MarksScored = int(input("Enter " + Subject + " Marks: "))
    #if Mathematics check for integer
    #print(ScoredMarks)
    return MarksScored

def Percentage(Mathematics, Science, English):
    #Science = ScienceTheory + SciencePractical
    Total =  Mathematics + Science + English
    TotalMax = 100+(75+25)+75
    Percentage = Total/TotalMax*100
    #print(str(Percentage)+"%")
    return Percentage

def Grade(Percentage):
    if Percentage > 90:
        print("Student got Grade A")
    elif Percentage <= 90 and Percentage > 75:
        print("Student got Grade B")
    else:
        print("Student got Average")
    
"""
def Evaluate():
    Subjects = ["Mathematics", "ScienceTheory", "SciencePractical", "English"]
    for Marks in Subjects:
        Marks(Subject)
"""
#Main Start Here

Mathematics      = int(input("Enter Mathematics Marks scored for Max mark of 100: "))
MathematicsOutcome = PassMark(Mathematics, "Mathematics")
print("Mathematics", MathematicsOutcome)

ScienceTheory    = int(input("Enter Science Theory Marks scored for Max mark of 75: "))
SciencePractical = int(input("Enter Science Practical scored Marks for Max mark of 25: "))
Science = ScienceTheory + SciencePractical
print("Science total scored is", Science)
if ScienceTheory < 25 or SciencePractical < 8:
    ScienceOutcome = "Fail"
else:
    ScienceOutcome = PassMark(Science, "Science")
print("Science", ScienceOutcome)

English          = int(input("Enter English Marks for scored Max mark of 75: "))
EnglishOutcome = PassMark(English, "English")
print("English", EnglishOutcome)

#TotalOutcome = [MathematicsOutcome, ScienceOutcome, EnglishOutcome]
#print(TotalOutcome)
if MathematicsOutcome != "Fail":
    if EnglishOutcome != "Fail":
        if ScienceOutcome != "Fail":
            Percentage = Percentage(Mathematics, Science, English)
            Grade(Percentage)            
else:
    print("Student Failed")

"""
SubjectS = ["Mathematics", "ScienceTheory", "SciencePractical", "English"]
SubjectS = iter(SubjectS)
while (1):
    x = next(SubjectS, 'end')
    if x != 'end':
        SubjectScore = MarksEntry(x)
        #print(SubjectScore)
        #print(x)
        SubjectOutcome = PassMark(SubjectScore, x)
        print(SubjectOutcome)
        if SubjectOutcome == "Pass":
            continue
        else:
            print("Student Failed")
            break
    else:
        break
else:
    print("Student Failed")

"""
