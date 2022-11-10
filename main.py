# The mark the user needs to get to the average
magicMark = 0;
# The calculation of all the marks
totalMarks = 0;
# Container to store mark for check befor used
checkMark = 0;
# Main
print("Welcome To BiteX")
print("A program to calculate the mark you need to get the average wanted\n")
amount = input("Please enter the amount of marks you have:\t\t")

amount = int(amount)

i = 0
while i != amount:
    checkMark = float(input("Please enter mark:\t\t"))
    if checkMark > 6:
        print("Mark isn't valid.")
    else:
        totalMarks += checkMark
        i += 1

wishedAverage = float(input("Please enter wished average:\t\t"))

#Formula
magicMark = (amount + 1) * wishedAverage - totalMarks

if magicMark > 6:
    print("The wished mark isn't possible")
else:
    print(f"You need the mark of {magicMark:.2f} to get the average of ", wishedAverage)