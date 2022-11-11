# The mark the user needs to get to the average
magicMark = 0
# Container to store mark for check befor used
checkMark = 0

def typeMark():
    # The calculation of all the marks
    totalMarks = 0
    # To get amount of marks
    i = 0
    checkMark = 0
    while True:
        checkMark = input("Please enter mark (s for stop):\t\t")
        # Falls Zahl oder Kommazahl
        try:
            checkMark = float(checkMark)
            totalMarks += checkMark
            i += 1
        # Falls Buchstabe
        except:
            getMagicMark(i, totalMarks)
        
# Calculate mark for needed average
def getMagicMark(i, totalMarks):
    wishedAverage = float(input("Please enter wished average:\t\t"))

    print("amount ", i, " total ", totalMarks)
    #Formula
    magicMark = (i + 1) * wishedAverage - totalMarks

    if magicMark > 6:
        print("The wished mark isn't possible")
    else:
        print(f"You need the mark of {magicMark:.2f} to get the average of {wishedAverage:.2f}\n")

    wantContinue = input("Do you want to calculate new (Y for Yes, N for No)?\t\t")
    if wantContinue == "Y":
        typeMark()
    elif wantContinue == "N":
        exit()

# Main
print("Welcome To BiteX")
print("A program to calculate the mark you need to get the average wanted\n")

typeMark()