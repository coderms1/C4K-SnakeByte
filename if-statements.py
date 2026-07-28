# Project: Grade Analyzer
# Author: mr dude 

sName = input("Enter name: ")
iUserAge = int(input("Enter age: "))

# if (age >= 10):
#     print("Welcome!")
# else:
#     print("Goodbye!")

if (iUserAge >= 10 and iUserAge <= 100): 
    print(f"Congrats {sName} you can enter!👍")
elif (iUserAge <= 0):
    print(f"Sorry {sName}, you have not been born yet. ")
elif (iUserAge > 100):
    print(f"Sorry {sName}, you are WAYYYY TOO OLD! 🧟‍♂️")
else:
    print(f"Sorry, {sName} you can NOT enter!👎")



    # Project: Grade Analyzer
# Author: mr dude 

# STEP 1: Prompt User Name
sName = input("Enter student's name: ")
# ------------------------ #
# STEP 2: Prompt Test Scores (4 times)
iTest1 = int(input("Enter Test Score 1: "))
iTest2 = int(input("Enter Test Score 2: "))
iTest3 = int(input("Enter Test Score 3: "))
iTest4 = int(input("Enter Test Score 4: "))
# ------------------------ #
# STEP 3: Drop Lowest Test?
sDrop = input("Drop lowest test score? (Y/N)").lower()
# ------------------------ #
# STEP 4: Determine Lowest Test & Calculate Average
if sDrop == "y":
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        fAverage = (iTest2 + iTest3 + iTest4) / 3
    elif iTest2 <= iTest3 and iTest2 <= iTest4:
        fAverage = (iTest1 + iTest3 + iTest4) / 3
    elif iTest3 <= iTest4:
        fAverage = (iTest1 + iTest2 + iTest4) / 3
    else :
        fAverage = (iTest1 + iTest2 + iTest3) / 3
else:
    fAverage = (iTest1 + iTest2 + iTest3 + iTest4) / 4
# ------------------------ #
print(fAverage)
# STEP 5: Determine Letter Grade
# ------------------------ #
# STEP 6: Display Results to User
