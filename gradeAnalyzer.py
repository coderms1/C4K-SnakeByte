# Project: Grade Analyzer
# Author: mr dude 

# INPUT (prompt user for Name & Tests)
sName = input("Enter student's name: ")
iTest1 = int(input("Enter Test Score 1: "))
iTest2 = int(input("Enter Test Score 2: "))
iTest3 = int(input("Enter Test Score 3: "))
iTest4 = int(input("Enter Test Score 4: "))
sDrop = input("Drop lowest score? (Y/N): ").lower()
# DETERMINE AVERAGE
if sDrop == "Y":
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        fAverage = (iTest2 + iTest3 + iTest4) / 3
    elif iTest2 <= iTest3 and iTest2 <= iTest4:
        fAverage = (iTest1 + iTest3 + iTest4) / 3
    elif iTest3 <= iTest4:
        fAverage = (iTest1 + iTest2 + iTest4) / 3
    else:
        fAverage = (iTest1 + iTest2 + iTest3) / 3
else:
    fAverage = (iTest1 + iTest2 + iTest3 + iTest4) / 4
# DETERMINE LETTER GRADE
if fAverage >= 90:
    sGrade = "A"
elif fAverage >= 80:
    sGrade = "B"
elif fAverage >= 70:
    sGrade = "C"
elif fAverage >= 60:
    sGrade = "D"
else:
    sGrade = "F"
# OUTPUT RESULTS TO USER 
print("GRADE REPORT:")
print(f"Student: {sName}")
print(f"Score: {fAverage}")
print(f"Grade: {sGrade}")
